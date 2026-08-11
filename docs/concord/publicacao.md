# Publicacao Do Concord

O Concord tem duas partes com necessidades diferentes.

## Frontend

O frontend e um app React/Vite e pode ser publicado como site estatico.

Variaveis esperadas:

```env
VITE_API_URL=https://sua-api.com/api
VITE_WS_URL=wss://sua-api.com/ws
VITE_FIREBASE_API_KEY=
VITE_FIREBASE_AUTH_DOMAIN=
VITE_FIREBASE_PROJECT_ID=
VITE_FIREBASE_APP_ID=
```

## Backend

O backend precisa de um ambiente com Python, banco PostgreSQL e suporte a WebSocket. GitHub Pages nao hospeda essa parte.

Variaveis principais:

```env
DATABASE_URL=
JWT_SECRET=
CORS_ORIGINS=https://seu-site-nggs.com
FIREBASE_SERVICE_ACCOUNT_JSON=
FIREBASE_SERVICE_ACCOUNT_JSON_CONTENT=
```

Use `FIREBASE_SERVICE_ACCOUNT_JSON_CONTENT` quando o provedor permitir salvar o conteudo JSON como secret. Use `FIREBASE_SERVICE_ACCOUNT_JSON` quando o servidor montar o arquivo da service account em disco.

## Login

O login nao pertence ao site NGGS inteiro. Ele pertence somente ao Concord. Isso significa que paginas como guias de PC, GPU, mouse, PUBG e Discord continuam publicas.

## Checklist Para Ir Ao Ar

1. Publicar backend FastAPI com HTTPS.
2. Configurar PostgreSQL persistente.
3. Configurar Firebase Authentication com provider Google.
4. Adicionar dominio do site aos dominios autorizados do Firebase.
5. Definir `CORS_ORIGINS` com a URL publica do site NGGS.
6. Definir `VITE_API_URL` e `VITE_WS_URL` no build do frontend.
7. Testar login, listagem de salas, criacao de sala e chat.
