# {{ nome_da_arma | default("Nome da Arma") }}

- **Tipo:** {{ tipo | default("Defina o tipo (AR, DMR, SMG, SR)") }}
- **Função na squad:** {{ funcao | default("Ex.: entrada, suporte, âncora") }}

## Configuração recomendada

| Slot | Anexo | Observações |
|------|-------|-------------|
| Cano | {{ cano | default("Compensador / Supressor") }} | |
| Empunhadura | {{ empunhadura | default("Vertical / Leve") }} | |
| Munição | {{ municao | default("5.56 / 7.62 / 9mm") }} | |
| Ótica | {{ otica | default("Holo / Scope 3x / Scope 4x") }} | |

## Observações táticas
- **Descrição:** {{ descricao | default("Explique quando usar, range ideal e combinações de armas.") }}
- **Por que fazer:** {{ motivo | default("Qual benefício estratégico?") }}
- **Como reverter:** {{ reverter | default("O que mudar se o plano não funcionar.") }}
- **Impacto esperado:** {{ impacto | default("Resultados esperados nas partidas.") }}

> Gere arquivos baseados neste template via CLI: `nggs gen weapon`.
