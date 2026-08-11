# Concord

Concord e o novo espaco de conexao da comunidade NGGS. O site principal continua aberto para guias, ferramentas e conteudo publico. O login so aparece quando a pessoa entra no Concord, porque ali existem identidade de usuario, salas, mensagens e presenca em tempo real.

## O Que Entra No Concord

- Login com Google usando Firebase Authentication.
- Perfil local criado automaticamente no backend.
- Salas de conversa da comunidade.
- Chat em tempo real via WebSocket.
- Base tecnica para chamadas WebRTC no futuro.

## Como Ele Foi Integrado

O codigo do Concord foi adicionado dentro deste repositorio em:

```txt
apps/concord/
```

Essa escolha preserva o site NGGS como ele ja funciona hoje. O MkDocs continua cuidando da documentacao e das paginas publicas, enquanto o Concord fica isolado como aplicacao propria, com frontend React/Vite e backend FastAPI.

## Fluxo De Acesso

1. Visitante abre o site NGGS normalmente.
2. Ele navega por guias, ferramentas e paginas publicas sem login.
3. Quando decide entrar no Concord, abre a area do app.
4. O Concord mostra login com Google.
5. Depois do login, o usuario acessa salas e chat.

## Onde Esta O Codigo

```txt
apps/concord/backend/        API FastAPI, Firebase Admin, banco e WebSocket
apps/concord/frontend/       Interface React/Vite com login Google
apps/concord/nginx/          Proxy local para Docker
apps/concord/docker-compose.yml
apps/concord/.env.example
```

## Status

Esta integracao coloca o Concord dentro da plataforma NGGS sem misturar responsabilidades. O proximo passo e publicar o backend em um host com HTTPS e apontar o frontend para ele usando as variaveis `VITE_API_URL` e `VITE_WS_URL`.
