# NVIDIA — ajustes legítimos para jogar de boa

## Painel de Controle NVIDIA
- **Descrição:** em **Gerenciar as configurações 3D**, defina **Modo de gerenciamento de energia** como *Preferir desempenho máximo*.  
- **Por que fazer:** mantém clocks altos enquanto você está no lobby ou em trocação intensa.  
- **Como reverter:** volte para *Otimização adaptativa* quando quiser economizar energia no dia a dia.  
- **Impacto esperado:** menos quedas bruscas de FPS em momentos agitados.

## Ajuste do limite de frames
- **Descrição:** configure o **Max Frame Rate** para 0 ou um valor um pouco acima da taxa do monitor (ex.: 165 Hz → 170 FPS).  
- **Por que fazer:** evita stutter causado por variações grandes de frame quando o PC não acompanha.  
- **Como reverter:** retorne para *Usar configuração global* ou 0.  
- **Impacto esperado:** tempo de frame mais uniforme e mira mais suave.

## G-SYNC com V-SYNC no driver
- **Descrição:** se o monitor suportar, habilite G-SYNC em modo janela + tela cheia e deixe o V-SYNC ativado só no driver (desligue dentro do jogo).  
- **Por que fazer:** sincroniza os frames sem adicionar atraso perceptível.  
- **Como reverter:** desative G-SYNC ou ajuste o V-SYNC para o modo que preferir.  
- **Impacto esperado:** fim do tearing com resposta rápida.

## Cache em SSD
- **Descrição:** confirme se a pasta `%ProgramData%\NVIDIA Corporation\NV_Cache` está num SSD. Caso esteja em um HDD, mova usando `mklink /J`.  
- **Por que fazer:** acelera a recompilação de shaders após updates.  
- **Como reverter:** apague o link simbólico e recrie a pasta original.  
- **Impacto esperado:** loadings de mapa mais curtos e menos travadinhas.

> **Referências oficiais:** [NVIDIA Support](https://nvidia.com/en-us/geforce/guides/)
