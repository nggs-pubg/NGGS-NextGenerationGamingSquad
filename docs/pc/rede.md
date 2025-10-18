# Rede — Latência Estável para Lobbies Cheios

## Usar conexão cabeada
- **Descrição:** sempre priorize cabo Ethernet CAT5e ou superior.  
- **Por que fazer:** reduz interferências e jitter presentes em Wi-Fi.  
- **Como reverter:** caso precise voltar ao Wi-Fi, escolha a banda de 5 GHz e mantenha linha de visão com o roteador.  
- **Impacto esperado:** ping mais consistente em rotas críticas.

## Atualizar drivers de rede
- **Descrição:** utilize o site da fabricante (Intel, Realtek, Killer) ou o Windows Update para instalar drivers recentes.  
- **Por que fazer:** corrige bugs de desconexão e melhora gerenciamento de energia da placa de rede.  
- **Como reverter:** acesse `Gerenciador de Dispositivos > Adaptadores de rede > Propriedades > Driver > Reverter` se notar instabilidade.  
- **Impacto esperado:** quedas de pacote minimizadas.

## Ajustar configuração de energia
- **Descrição:** em `Gerenciador de Dispositivos`, desative a opção **Permitir que o computador desligue este dispositivo para economizar energia** na aba **Gerenciamento de Energia**.  
- **Por que fazer:** evita que o Windows suspenda a interface durante longas filas.  
- **Como reverter:** reative a caixa caso deseje economizar energia em uso diário.  
- **Impacto esperado:** conexões persistentes em scrims extensas.

## Testar estabilidade
- **Descrição:** rode `ping -n 50 8.8.8.8` (Windows) ou `ping -c 50 8.8.8.8` (Linux/macOS).  
- **Por que fazer:** monitora perda de pacotes e variação do ping antes de treinos.  
- **Como reverter:** comando não modifica nada; basta encerrar.  
- **Impacto esperado:** identificação rápida de problemas para acionar a provedora.
