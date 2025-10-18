# Armazenamento — SSDs prontos para o PUBG

## Liberar espaço em SSD
- **Descrição:** utilize `Configurações > Sistema > Armazenamento` para executar a **Limpeza de Disco** e remover arquivos temporários.  
- **Por que fazer:** SSD com menos de 10% livre pode causar quedas de performance e travamentos em loading.  
- **Como reverter:** nenhum impacto permanente; caso remova algo necessário, restaure a partir da Lixeira (se disponível).  
- **Impacto esperado:** telas de carregamento mais rápidas e menos stutter ao entrar em prédios.

## Habilitar TRIM manual (para SSD SATA)
- **Descrição:** execute o comando `Optimize-Volume -DriveLetter C -ReTrim -Verbose` no PowerShell com permissões elevadas.  
- **Por que fazer:** mantém a performance consistente ao longo do tempo, removendo blocos marcados para exclusão.  
- **Como reverter:** TRIM é seguro; não há reversão necessária. Apenas evite executar repetidamente em SSDs já otimizados.  
- **Impacto esperado:** entrega constante de velocidade de leitura/escrita.

## Verificar integridade do disco
- **Descrição:** rode `chkdsk /scan` no Prompt de Comando.  
- **Por que fazer:** detecta clusters corrompidos que podem resultar em falhas durante quedas de energia.  
- **Como reverter:** nenhuma mudança permanente. Caso o comando peça agendamento na próxima inicialização, aceite apenas quando puder reiniciar.  
- **Impacto esperado:** redução de crashes relacionados a arquivos do jogo.

## Certificar localização do PUBG
- **Descrição:** mantenha o PUBG instalado em SSD NVMe ou SATA rápido, evitando discos externos via USB 2.0/3.0.  
- **Por que fazer:** assets carregam mais rápido, resultando em texturas nítidas imediatamente ao cair no mapa.  
- **Como reverter:** se precisar mover o jogo, utilize a opção **Mover** da Steam/Epic para outro drive.  
- **Impacto esperado:** renderização sem delay em hot drops.
