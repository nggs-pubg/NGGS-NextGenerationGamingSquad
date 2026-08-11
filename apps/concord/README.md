# OpenTalk

OpenTalk e um MVP de comunidade em tempo real. A ideia e permitir que pessoas entrem com Google, criem salas, conversem por chat e evoluam isso para chamadas WebRTC com audio, video e compartilhamento de tela.

Este repositorio esta sendo montado como base publica do projeto: simples o bastante para qualquer pessoa rodar, mas com uma arquitetura que nao nos prenda quando a comunidade crescer.

## O Que Estamos Fazendo

Estamos separando o produto em duas partes:

- Frontend React/Vite: interface web publicada como site estatico, ideal para GitHub Pages.
- Backend FastAPI: API, autenticacao, salas, membros, mensagens, WebSocket e integracao com Firebase Admin.

O login principal e pelo Firebase Authentication com Google. No navegador, o usuario entra com Gmail e recebe um ID token do Firebase. O frontend envia esse token para o backend. O backend valida o token com Firebase Admin e cria automaticamente um usuario local quando aquele email aparece pela primeira vez.

O backend tambem mantem login tradicional por usuario/senha durante a migracao, mas o caminho desejado para a comunidade e o Google.

## Estado Atual

Ja temos:

- Login com Google via Firebase no frontend.
- Validacao de ID token Firebase no backend.
- Criacao automatica de usuario local a partir do email do Google.
- Salas com criacao, entrada, saida, listagem e remocao pelo dono.
- Chat em tempo real por WebSocket.
- Persistencia de mensagens no banco.
- Docker Compose com PostgreSQL, backend, frontend e Nginx.
- GitHub Actions para CI.
- GitHub Actions para deploy do frontend no GitHub Pages.
- Documentacao inicial em `docs/`.

Ainda e MVP:

- As tabelas sao criadas com `Base.metadata.create_all`; em producao devemos migrar para Alembic.
- WebRTC ainda esta na camada de sinalizacao/base, nao como experiencia completa de chamada.
- Falta TURN server para chamadas confiaveis fora de redes simples.
- Falta bateria real de testes automatizados.
- Falta observabilidade, rate limit e politicas mais fortes de seguranca.

## Rodar Localmente

Crie o `.env`:

```bash
cp .env.example .env
```

Suba tudo com Docker:

```bash
docker compose up -d --build
```

Acesse:

- App: `http://localhost`
- API docs: `http://localhost/docs`
- Healthcheck: `http://localhost/health`

## Firebase

No Firebase Console:

1. Crie um projeto Firebase.
2. Ative `Authentication`.
3. Ative o provider `Google`.
4. Crie um app web e copie as variaveis para o frontend.
5. Crie uma service account para o backend.

Variaveis do frontend:

```env
VITE_FIREBASE_API_KEY=
VITE_FIREBASE_AUTH_DOMAIN=
VITE_FIREBASE_PROJECT_ID=
VITE_FIREBASE_APP_ID=
```

Variaveis do backend:

```env
FIREBASE_SERVICE_ACCOUNT_JSON=
FIREBASE_SERVICE_ACCOUNT_JSON_CONTENT=
```

Use apenas uma das duas formas no backend:

- `FIREBASE_SERVICE_ACCOUNT_JSON`: caminho para um arquivo JSON local ou montado no servidor.
- `FIREBASE_SERVICE_ACCOUNT_JSON_CONTENT`: conteudo JSON completo da service account, ideal para ambiente com secrets.

Nunca commite o JSON da service account. O `.gitignore` ja bloqueia `firebase-service-account.json`.

## Publicar No GitHub Pages

GitHub Pages publica apenas o frontend. O backend FastAPI, PostgreSQL e WebSocket precisam ficar em outro host, como Render, Railway, Fly.io, Cloud Run ou uma VPS.

No GitHub:

1. Abra `Settings` -> `Pages`.
2. Em `Build and deployment`, selecione `Source: GitHub Actions`.
3. Abra `Settings` -> `Secrets and variables` -> `Actions` -> `Variables`.
4. Crie as variaveis:

```env
VITE_API_URL=https://sua-api-publica.com/api
VITE_WS_URL=wss://sua-api-publica.com/ws
VITE_FIREBASE_API_KEY=
VITE_FIREBASE_AUTH_DOMAIN=
VITE_FIREBASE_PROJECT_ID=
VITE_FIREBASE_APP_ID=
```

Depois faca push na branch `main`. O workflow `Deploy GitHub Pages` vai gerar o build do frontend e publicar o conteudo de `frontend/dist`.

Para repositorios publicados como `https://usuario.github.io/nome-do-repo/`, o workflow define automaticamente:

```env
VITE_BASE_PATH=/<nome-do-repo>/
```

## API Principal

Autenticacao:

- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/firebase`
- `GET /api/auth/me`

Salas:

- `GET /api/rooms`
- `POST /api/rooms`
- `POST /api/rooms/{room_id}/join`
- `POST /api/rooms/{room_id}/leave`
- `GET /api/rooms/{room_id}/members`
- `DELETE /api/rooms/{room_id}`
- `GET /api/rooms/{room_id}/messages`

Sistema:

- `GET /health`
- `GET /docs`

WebSocket:

```txt
/ws/rooms/{room_id}?token=<firebase-id-token-ou-jwt-local>
```

Eventos atuais:

- `chat_message`
- `user_joined`
- `user_left`
- eventos de sinalizacao WebRTC, como `webrtc_offer`, `webrtc_answer` e `webrtc_ice_candidate`

## Estrutura

```txt
backend/
  app/main.py          API FastAPI, modelos, auth, salas, mensagens e WebSocket
frontend/
  src/main.tsx         App React
  src/style.css        Estilos da interface
nginx/
  nginx.conf           Proxy local para frontend, API e WebSocket
docs/
  *.md                 Documentacao tecnica inicial
.github/workflows/
  ci.yml               Validacao backend/frontend
  deploy.yml           Publicacao do frontend no GitHub Pages
docker-compose.yml     Stack local completa
```

## Proximos Passos

1. Colocar o backend em um host publico com HTTPS.
2. Configurar `CORS_ORIGINS` com a URL do GitHub Pages.
3. Preencher as variaveis do GitHub Actions.
4. Adicionar Alembic para migracoes.
5. Criar testes de API e testes basicos do frontend.
6. Evoluir WebRTC para chamadas reais com TURN server.
