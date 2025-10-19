# Rede — Ping tranquilo para jogar com os amigos

## Prefira o bom e velho cabo
- **Descrição:** use cabo Ethernet (CAT5e ou superior) sempre que possível.  
- **Por que fazer:** o Wi-Fi é prático, mas o cabo evita interferências e flutuações de ping.  
- **Como reverter:** se precisar voltar ao Wi-Fi, conecte na rede de 5 GHz e mantenha o roteador por perto, sem obstáculos.  
- **Impacto esperado:** conexão mais estável para cair nos mapas sem medo de lag.

## Mantenha os drivers de rede atualizados
- **Descrição:** baixe versões recentes direto da fabricante (Intel, Realtek, Killer) ou pelo Windows Update.  
- **Por que fazer:** atualizações resolvem quedas aleatórias e melhoram o consumo de energia da placa.  
- **Como reverter:** `Gerenciador de Dispositivos > Adaptadores de rede > Propriedades > Driver > Reverter`.  
- **Impacto esperado:** menos perda de pacotes e reconexões durante a call no Discord.

## Ajuste o modo de energia da placa
- **Descrição:** no `Gerenciador de Dispositivos`, abra seu adaptador de rede e desmarque **Permitir que o computador desligue este dispositivo para economizar energia**.  
- **Por que fazer:** impede que o Windows “cochile” com a conexão em sessões longas.  
- **Como reverter:** marque novamente a caixa se estiver longe do PC e quiser economizar uns watts.  
- **Impacto esperado:** conexão firme durante noites inteiras de jogatina.

## Faça um teste rápido antes do drop
- **Descrição:** rode `ping -n 50 8.8.8.8` (Windows) ou `ping -c 50 8.8.8.8` (Linux/macOS).  
- **Por que fazer:** monitora se há perda de pacotes ou picos de ping antes de chamar o squad.  
- **Como reverter:** o comando não muda nada; é só fechar a janela.  
- **Impacto esperado:** diagnóstico rápido para decidir se vale reiniciar modem/roteador ou acionar o provedor.
