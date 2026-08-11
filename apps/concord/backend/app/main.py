from datetime import datetime, timedelta, timezone
from typing import Annotated
import json
import logging
import os

import firebase_admin
import jwt
from fastapi import Depends, FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
from pydantic import BaseModel, EmailStr, Field
from pwdlib import PasswordHash
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

logging.basicConfig(level=logging.INFO)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./opentalk.db")
SECRET = os.getenv("JWT_SECRET", "dev-secret-change-me")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
EXPIRE = int(os.getenv("JWT_EXPIRE_MINUTES", "60"))

engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)
Session = async_sessionmaker(engine, expire_on_commit=False)
hashing = PasswordHash.recommended()
oauth = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

firebase_content = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON_CONTENT")
firebase_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON")
if firebase_content:
    firebase_admin.initialize_app(credentials.Certificate(json.loads(firebase_content)))
elif firebase_path and os.path.exists(firebase_path):
    firebase_admin.initialize_app(credentials.Certificate(firebase_path))


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(40), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80))
    description: Mapped[str] = mapped_column(Text, default="")
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))


class Member(Base):
    __tablename__ = "room_members"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    joined_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    content: Mapped[str] = mapped_column(String(2000))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))


class Register(BaseModel):
    username: str = Field(min_length=3, max_length=40)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class RoomIn(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    description: str = Field(default="", max_length=500)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class Hub:
    def __init__(self):
        self.rooms: dict[int, dict[int, WebSocket]] = {}

    async def send(self, room_id: int, event: dict, exclude: int | None = None):
        for user_id, ws in list(self.rooms.get(room_id, {}).items()):
            if user_id == exclude:
                continue
            try:
                await ws.send_json(event)
            except Exception:
                self.rooms[room_id].pop(user_id, None)


hub = Hub()


async def db():
    async with Session() as session:
        yield session


async def unique_username(session: AsyncSession, raw: str):
    base = "".join(c for c in raw.lower().replace(" ", "-") if c.isalnum() or c in "-_").strip("-_") or "user"
    candidate = base[:40]
    counter = 1
    while (await session.execute(select(User).where(User.username == candidate))).scalar_one_or_none():
        suffix = f"-{counter}"
        candidate = f"{base[:40 - len(suffix)]}{suffix}"
        counter += 1
    return candidate


async def user_from_token(token: str, session: AsyncSession):
    try:
        if firebase_admin._apps:
            decoded = firebase_auth.verify_id_token(token)
            email = decoded.get("email")
            if not email:
                raise ValueError("Firebase account has no email")
            user = (await session.execute(select(User).where(User.email == email))).scalar_one_or_none()
            if not user:
                username = await unique_username(session, decoded.get("name") or email.split("@")[0])
                user = User(username=username, email=email, password_hash="firebase-managed")
                session.add(user)
                await session.commit()
                await session.refresh(user)
        else:
            user_id = jwt.decode(token, SECRET, algorithms=[ALGORITHM])["sub"]
            user = await session.get(User, int(user_id))
    except Exception:
        raise HTTPException(401, "Token invalido ou expirado")

    if not user or not user.is_active:
        raise HTTPException(401, "Usuario invalido")
    return user


async def current(token: Annotated[str, Depends(oauth)], session: Annotated[AsyncSession, Depends(db)]):
    return await user_from_token(token, session)


def make_token(user_id: int):
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE)
    return jwt.encode({"sub": str(user_id), "exp": expires_at}, SECRET, algorithm=ALGORITHM)


app = FastAPI(title="OpenTalk API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/api/auth/register", response_model=Token)
async def register(data: Register, session: Annotated[AsyncSession, Depends(db)]):
    existing = (
        await session.execute(select(User).where((User.email == data.email) | (User.username == data.username)))
    ).scalar_one_or_none()
    if existing:
        raise HTTPException(409, "Usuario ou email ja cadastrado")
    user = User(username=data.username, email=data.email, password_hash=hashing.hash(data.password))
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return Token(access_token=make_token(user.id))


@app.post("/api/auth/login", response_model=Token)
async def login(form: Annotated[OAuth2PasswordRequestForm, Depends()], session: Annotated[AsyncSession, Depends(db)]):
    user = (
        await session.execute(select(User).where((User.username == form.username) | (User.email == form.username)))
    ).scalar_one_or_none()
    if not user or not hashing.verify(form.password, user.password_hash):
        raise HTTPException(401, "Credenciais invalidas")
    return Token(access_token=make_token(user.id))


@app.post("/api/auth/firebase")
async def firebase_login(user: Annotated[User, Depends(current)]):
    return {"id": user.id, "username": user.username, "email": user.email}


@app.get("/api/auth/me")
async def me(user: Annotated[User, Depends(current)]):
    return {"id": user.id, "username": user.username, "email": user.email}


@app.get("/api/rooms")
async def rooms(user: Annotated[User, Depends(current)], session: Annotated[AsyncSession, Depends(db)]):
    rows = (await session.execute(select(Room).order_by(Room.name))).scalars()
    return [{"id": room.id, "name": room.name, "description": room.description, "owner_id": room.owner_id} for room in rows]


@app.post("/api/rooms")
async def create_room(data: RoomIn, user: Annotated[User, Depends(current)], session: Annotated[AsyncSession, Depends(db)]):
    room = Room(**data.model_dump(), owner_id=user.id)
    session.add(room)
    await session.commit()
    await session.refresh(room)
    return {"id": room.id, "name": room.name, "description": room.description, "owner_id": user.id}


@app.post("/api/rooms/{room_id}/join")
async def join(room_id: int, user: Annotated[User, Depends(current)], session: Annotated[AsyncSession, Depends(db)]):
    if not await session.get(Room, room_id):
        raise HTTPException(404, "Sala nao encontrada")
    member = (
        await session.execute(select(Member).where(Member.room_id == room_id, Member.user_id == user.id))
    ).scalar_one_or_none()
    if not member:
        session.add(Member(room_id=room_id, user_id=user.id))
        await session.commit()
    return {"status": "joined"}


@app.post("/api/rooms/{room_id}/leave")
async def leave(room_id: int, user: Annotated[User, Depends(current)], session: Annotated[AsyncSession, Depends(db)]):
    member = (
        await session.execute(select(Member).where(Member.room_id == room_id, Member.user_id == user.id))
    ).scalar_one_or_none()
    if member:
        await session.delete(member)
        await session.commit()
    return {"status": "left"}


@app.get("/api/rooms/{room_id}/members")
async def members(room_id: int, user: Annotated[User, Depends(current)], session: Annotated[AsyncSession, Depends(db)]):
    rows = (
        await session.execute(select(User.id, User.username).join(Member, Member.user_id == User.id).where(Member.room_id == room_id))
    ).all()
    return [{"id": user_id, "username": username} for user_id, username in rows]


@app.delete("/api/rooms/{room_id}")
async def delete_room(room_id: int, user: Annotated[User, Depends(current)], session: Annotated[AsyncSession, Depends(db)]):
    room = await session.get(Room, room_id)
    if not room:
        raise HTTPException(404, "Sala nao encontrada")
    if room.owner_id != user.id:
        raise HTTPException(403, "Somente o proprietario pode remover a sala")
    await session.delete(room)
    await session.commit()
    return {"status": "deleted"}


@app.get("/api/rooms/{room_id}/messages")
async def messages(room_id: int, user: Annotated[User, Depends(current)], session: Annotated[AsyncSession, Depends(db)]):
    rows = (
        await session.execute(
            select(Message, User.username)
            .join(User, User.id == Message.user_id)
            .where(Message.room_id == room_id)
            .order_by(Message.created_at)
        )
    ).all()
    return [{"id": message.id, "username": username, "content": message.content, "created_at": message.created_at} for message, username in rows]


@app.websocket("/ws/rooms/{room_id}")
async def websocket(ws: WebSocket, room_id: int, token: str):
    async with Session() as session:
        try:
            user = await user_from_token(token, session)
        except HTTPException:
            await ws.close(code=1008)
            return

    await ws.accept()
    hub.rooms.setdefault(room_id, {})[user.id] = ws
    await hub.send(room_id, {"type": "user_joined", "user_id": user.id, "username": user.username}, user.id)

    try:
        while True:
            data = await ws.receive_json()
            data["user_id"] = user.id
            data["username"] = user.username
            if data.get("type") == "chat_message" and data.get("content"):
                async with Session() as session:
                    session.add(Message(room_id=room_id, user_id=user.id, content=str(data["content"])[:2000]))
                    await session.commit()
            await hub.send(room_id, data, user.id)
    except WebSocketDisconnect:
        hub.rooms.get(room_id, {}).pop(user.id, None)
        await hub.send(room_id, {"type": "user_left", "user_id": user.id, "username": user.username})
