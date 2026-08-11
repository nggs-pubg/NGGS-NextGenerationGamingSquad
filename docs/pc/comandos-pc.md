# Comandos NGGS — manutenção rápida no PC

## Otimizador NGGS (comandos CMD)

- Download: [`nggs-otimizador.bat`](../assets/scripts/nggs-otimizador.bat). Revise o conteúdo antes de executar.
- Execução manual passo a passo: [`nggs-passos-manual.txt`](../assets/scripts/nggs-passos-manual.txt)

!!! warning "Antes de executar"
    Leia o arquivo, feche downloads e partidas em andamento e crie um ponto de restauração. O script não precisa de privilégios de administrador para exibir as opções; o Windows solicitará permissão apenas se uma operação precisar dela.

### O que o script faz

| Etapa | Descrição | Por que fazer | Como reverter | Impacto esperado |
| --- | --- | --- | --- | --- |
| Cache DNS | Oferece `ipconfig /flushdns` como opção. | Pode corrigir resolução de nomes desatualizada; não reduz o ping por si só. | O cache é recriado automaticamente. | Reconexão a serviços cujo endereço mudou. |
| Plano de energia | Mostra o plano atual e oferece `powercfg /setactive SCHEME_MIN`. | Pode reduzir economia agressiva de energia em desktops. | Selecione o plano anterior nas Configurações do Windows. | Efeito variável; pode elevar consumo e temperatura. |

## Como usar

### Opção A — Arquivo `.bat`

1. Baixe o arquivo `nggs-otimizador.bat`.
2. Abra o arquivo em um editor e confira os comandos.
3. Execute normalmente e confirme somente as etapas desejadas.

### Opção B — Comandos manuais

1. Abra o Prompt de Comando; eleve para administrador apenas quando o Windows exigir.
2. Execute os comandos na ordem indicada no arquivo `nggs-passos-manual.txt` ou utilize a referência abaixo.
3. Reinicie o PC ao finalizar.

### Recomendações

- Use a rotina somente para resolver um sintoma específico; manutenção periódica não melhora FPS automaticamente.
- Combine com o [checklist geral](checklist.md) para garantir drivers e updates em dia.
- Evite alterar os comandos sem conversar com a equipe técnica ou entender bem cada etapa.

## Conteúdo do arquivo `.bat`

O [arquivo publicado](../assets/scripts/nggs-otimizador.bat) é a fonte única e revisável. Ele pede confirmação antes de cada mudança e não apaga arquivos nem redefine a pilha de rede.

## O que não recomendamos

Não desative DEP/NX, não altere temporizadores de boot (`bcdedit`) e não aplique ajustes genéricos no Registro. Essas mudanças podem reduzir proteções do sistema, causar instabilidade e não oferecem ganho de FPS garantido. Prefira as opções documentadas na interface do Windows e mantenha drivers atualizados.
