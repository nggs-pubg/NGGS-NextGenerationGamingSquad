# NVIDIA — Ajustes Legítimos para FPS Competitivo

## Painel de Controle NVIDIA
- **Descrição:** em **Gerenciar as configurações 3D**, ajuste **Modo de gerenciamento de energia** para *Preferir máximo desempenho*.  
- **Por que fazer:** garante clocks elevados durante partidas intensas.  
- **Como reverter:** retorne para *Otimização adaptativa* para reduzir consumo no uso diário.  
- **Impacto esperado:** redução de quedas bruscas de FPS em finais de partida.

## Limitar máximo de frames
- **Descrição:** defina o **Max Frame Rate** em 0 ou em valor ligeiramente acima da taxa do monitor (ex.: 165 Hz -> 170 FPS).  
- **Por que fazer:** evita stutter causado por excesso de frames quando o PC não acompanha.  
- **Como reverter:** ajuste de volta para *Usar configuração global* ou 0.  
- **Impacto esperado:** frame time mais uniforme, facilitando tracking.

## G-SYNC + V-SYNC no driver
- **Descrição:** para monitores compatíveis, habilite G-SYNC em janelas e tela cheia e deixe o V-SYNC ativado apenas no driver (off dentro do jogo).  
- **Por que fazer:** sincroniza frames sem adicionar input lag extra.  
- **Como reverter:** desmarque G-SYNC ou altere o modo de V-SYNC conforme preferência.  
- **Impacto esperado:** elimina tearing mantendo resposta rápida.

## Preferir cache em SSD
- **Descrição:** garanta que a pasta de cache da NVIDIA (`%ProgramData%\NVIDIA Corporation\NV_Cache`) esteja em SSD. Caso contrário, mova usando junction (`mklink /J`).  
- **Por que fazer:** acelera recompilação de shaders após updates do PUBG.  
- **Como reverter:** exclua o link simbólico e recrie a pasta original.  
- **Impacto esperado:** loadings de mapa mais curtos.

> **Referências oficiais:** [NVIDIA Support](https://nvidia.com/en-us/geforce/guides/) para cada ajuste descrito.
