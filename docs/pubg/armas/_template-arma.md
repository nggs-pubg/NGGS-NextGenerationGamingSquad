# {{ nome_da_arma | default("Nome da Arma") }}

- **Tipo:** {{ tipo | default("Defina o tipo (AR, DMR, SMG, SR)") }}
- **Função no squad:** {{ funcao | default("Ex.: avanço, suporte utilitário, cobertura") }}

## Configuração recomendada

| Slot | Anexo | Observações |
|------|-------|-------------|
| Cano | {{ cano | default("Compensador / Supressor") }} | |
| Empunhadura | {{ empunhadura | default("Vertical / Leve / Thumb") }} | |
| Munição | {{ municao | default("5.56 / 7.62 / 9mm") }} | |
| Ótica | {{ otica | default("Holo / Scope 3x / Scope 4x") }} | |

## Observações táticas
- **Descrição:** {{ descricao | default("Conte quando usar, alcance preferido e com que outras armas combina.") }}
- **Por que fazer:** {{ motivo | default("Qual a vantagem para o squad?") }}
- **Como reverter:** {{ reverter | default("O que trocar se a ideia não encaixar.") }}
- **Impacto esperado:** {{ impacto | default("O que muda na jogatina.") }}
