# WebSocket

Conecte em `/ws/rooms/{id}?token=JWT`. Envie eventos JSON com `type`; mensagens de chat usam `content`. Eventos desconhecidos são retransmitidos para participantes, permitindo sinalização WebRTC sem acoplamento.
