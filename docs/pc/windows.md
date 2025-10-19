# Windows 10/11 — Preparação Realista para FPS

Todos os ajustes abaixo são suportados oficialmente pela Microsoft. Siga na ordem sugerida e sempre leia as seções **Como reverter** para voltar ao estado anterior.

## Desativar apps em segundo plano
- **Descrição:** limite a execução de aplicativos UWP em segundo plano em `Configurações > Privacidade > Aplicativos em segundo plano`.  
- **Por que fazer:** diminui consumo de RAM e CPU por processos que não impactam a jogabilidade.  
- **Como reverter:** reabilite aplicativos específicos ativando novamente o toggle.  
- **Impacto esperado:** estabilidade maior em lobbies grandes.

## Ajustar efeitos visuais
- **Descrição:** em `Painel de Controle > Sistema > Configurações Avançadas > Desempenho`, selecione **Ajustar para obter um melhor desempenho**, preservando suavização de fontes se necessário.  
- **Por que fazer:** remove animações que consomem recursos, priorizando o motor do PUBG.  
- **Como reverter:** escolha **Deixar o Windows escolher a melhor opção** para restaurar o padrão.  
- **Impacto esperado:** pequena redução na latência de abertura de programas.

## Habilitar Game Mode
- **Descrição:** abra `Configurações > Jogos > Modo de Jogo` e deixe ativado.  
- **Por que fazer:** o Game Mode prioriza recursos para o jogo em execução e reduz notificações.  
- **Como reverter:** desative o toggle se estiver usando aplicativos que precisam de multitarefa intensa.  
- **Impacto esperado:** mitigação de quedas de FPS quando processos em background exigem CPU.

## Programador GPU acelerado (Hardware Accelerated GPU Scheduling)
- **Descrição:** em `Configurações > Sistema > Tela > Configurações de gráficos`, ative o agendador de GPU acelerado por hardware. Disponível para GPUs compatíveis (NVIDIA série 10+, AMD 5600+).  
- **Por que fazer:** reduz a latência de renderização, deixando o jogo mais responsivo mesmo em partidas casuais.  
- **Como reverter:** desative a opção e reinicie o PC; útil para troubleshooting caso ocorram artefatos.  
- **Impacto esperado:** melhoria leve na resposta de frame-time.

## Atualizações automáticas
- **Descrição:** pause atualizações por até 7 dias antes de eventos ou corujões com os amigos via `Configurações > Windows Update > Pausar`.  
- **Por que fazer:** evita reinicializações ou downloads pesados durante as jogatinas.  
- **Como reverter:** clique em **Retomar atualizações** após a sessão.  
- **Impacto esperado:** sessões ininterruptas, sem perda de foco.

> **Fonte recomendada:** [Documentação oficial do Windows](https://learn.microsoft.com/windows/client-management/)
