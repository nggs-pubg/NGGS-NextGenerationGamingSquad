import React, {useEffect, useState} from 'react';
import {createRoot} from 'react-dom/client';
import {initializeApp} from 'firebase/app';
import {getAuth, GoogleAuthProvider, signInWithPopup} from 'firebase/auth';
import './style.css';

type Room = {id: number; name: string; description: string};
type Msg = {username: string; content: string};
type CurrentUser = {id: number; username: string; email: string};

const API = import.meta.env.VITE_API_URL || '/api';

function websocketUrl() {
  if (import.meta.env.VITE_WS_URL) return import.meta.env.VITE_WS_URL;
  if (API.startsWith('http')) return API.replace(/^http/, 'ws').replace(/\/api\/?$/, '/ws');
  return `${location.protocol === 'https:' ? 'wss' : 'ws'}://${location.host}/ws`;
}

const WS = websocketUrl();
const firebaseApp = initializeApp({
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID
});
const firebaseAuth = getAuth(firebaseApp);

function App() {
  const [token, setToken] = useState(localStorage.getItem('token') || '');
  const [user, setUser] = useState<CurrentUser>();
  const [rooms, setRooms] = useState<Room[]>([]);
  const [room, setRoom] = useState<Room>();
  const [msgs, setMsgs] = useState<Msg[]>([]);
  const [text, setText] = useState('');
  const [socket, setSocket] = useState<WebSocket>();
  const [auth, setAuth] = useState({username: '', password: ''});

  async function googleLogin() {
    const result = await signInWithPopup(firebaseAuth, new GoogleAuthProvider());
    const idToken = await result.user.getIdToken();
    localStorage.setItem('token', idToken);
    setToken(idToken);
  }

  async function request(path: string, opts: RequestInit = {}) {
    const requestHeaders = new Headers(opts.headers);
    requestHeaders.set('Content-Type', 'application/json');
    requestHeaders.set('Authorization', `Bearer ${token}`);
    const response = await fetch(API + path, {
      ...opts,
      headers: requestHeaders
    });
    if (!response.ok) {
      const body = await response.json().catch(() => ({detail: 'Erro'}));
      throw Error(body.detail || 'Erro');
    }
    return response.json();
  }

  async function enter(nextRoom: Room) {
    socket?.close();
    setRoom(nextRoom);
    await request(`/rooms/${nextRoom.id}/join`, {method: 'POST'});
    setMsgs(await request(`/rooms/${nextRoom.id}/messages`));
    const nextSocket = new WebSocket(`${WS}/rooms/${nextRoom.id}?token=${encodeURIComponent(token)}`);
    nextSocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'chat_message') setMsgs((items) => [...items, data]);
    };
    setSocket(nextSocket);
  }

  function send() {
    if (!text.trim() || !socket || !user) return;
    socket.send(JSON.stringify({type: 'chat_message', content: text}));
    setMsgs((items) => [...items, {username: user.username, content: text}]);
    setText('');
  }

  async function login(event: React.FormEvent) {
    event.preventDefault();
    const response = await fetch(API + '/auth/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: new URLSearchParams({username: auth.username, password: auth.password})
    });
    const data = await response.json();
    if (data.access_token) {
      localStorage.setItem('token', data.access_token);
      setToken(data.access_token);
    }
  }

  async function createRoom() {
    const name = prompt('Nome da sala');
    if (!name) return;
    const created = await request('/rooms', {
      method: 'POST',
      body: JSON.stringify({name})
    });
    setRooms((items) => [...items, created]);
  }

  useEffect(() => {
    if (!token) return;
    request('/auth/me')
      .then(setUser)
      .then(() => request('/rooms').then(setRooms))
      .catch(() => {
        localStorage.removeItem('token');
        setToken('');
      });
  }, [token]);

  if (!token) {
    return (
      <main className="auth">
        <form onSubmit={login}>
          <h1>OpenTalk</h1>
          <p>Entre com sua conta Google para participar da comunidade.</p>
          <button type="button" onClick={googleLogin}>Continuar com Google</button>
          <small>O login tradicional permanece disponivel durante a migracao.</small>
          <input placeholder="Usuario ou email" onChange={(event) => setAuth({...auth, username: event.target.value})} />
          <input type="password" placeholder="Senha" onChange={(event) => setAuth({...auth, password: event.target.value})} />
          <button>Entrar</button>
        </form>
      </main>
    );
  }

  return (
    <div className="app">
      <header>
        <b>OpenTalk</b>
        <span>
          {user?.username}
          <button onClick={() => { localStorage.removeItem('token'); location.reload(); }}>Sair</button>
        </span>
      </header>
      <aside>
        <h3>Salas</h3>
        {rooms.map((item) => (
          <button className="room" onClick={() => enter(item)} key={item.id}># {item.name}</button>
        ))}
        <button onClick={createRoom}>+ Nova sala</button>
      </aside>
      <section>
        <h2>{room ? `# ${room.name}` : 'Selecione uma sala'}</h2>
        <div className="messages">
          {msgs.map((msg, index) => <p key={index}><strong>{msg.username}</strong> {msg.content}</p>)}
        </div>
        {room && (
          <div className="composer">
            <input
              value={text}
              onChange={(event) => setText(event.target.value)}
              onKeyDown={(event) => event.key === 'Enter' && send()}
              placeholder="Escreva uma mensagem..."
            />
            <button onClick={send}>Enviar</button>
          </div>
        )}
      </section>
    </div>
  );
}

createRoot(document.getElementById('root')!).render(<App />);
