# Arquitetura

Nginx encaminha frontend, API e WebSocket. FastAPI usa SQLAlchemy assíncrono e PostgreSQL. O WebSocket mantém conexões em memória no MVP; a interface para futura evolução é a classe `Hub`, que pode ser trocada por Redis pub/sub. WebRTC transporta mídia diretamente entre navegadores; o backend apenas sinaliza.
