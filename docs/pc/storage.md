# Armazenamento — SSDs prontos para qualquer lobby

## Liberar espaço em SSD
- **Descrição:** abra `Configurações > Sistema > Armazenamento` e use a limpeza de arquivos temporários.  
- **Por que fazer:** SSD quase cheio (menos de 10% livre) pode causar travadinhas em loadings e texturas.  
- **Como reverter:** se apagar algo sem querer, restaure pela Lixeira ou backup.  
- **Impacto esperado:** telas de carregamento mais rápidas e quedas suaves em qualquer mapa.

## Rodar TRIM manual em SSD SATA
- **Descrição:** no PowerShell (administrador) execute `Optimize-Volume -DriveLetter C -ReTrim -Verbose`.  
- **Por que fazer:** mantém a performance consistente ao limpar blocos marcados para exclusão.  
- **Como reverter:** não precisa — TRIM é um processo seguro, apenas evite rodar repetidamente na mesma sessão.  
- **Impacto esperado:** leitura/escrita estável mesmo após longas maratonas de jogo.

## Conferir integridade do disco
- **Descrição:** execute `chkdsk /scan` no Prompt de Comando.  
- **Por que fazer:** diagnostica erros que podem causar crash em atualizações ou quedas de energia.  
- **Como reverter:** o comando não altera arquivos. Se pedir agendamento, aceite quando puder reiniciar.  
- **Impacto esperado:** menos surpresas com arquivos corrompidos no meio do fim de semana.

## Mantenha o PUBG no SSD
- **Descrição:** instale o PUBG (e outros jogos mais pesados) em um SSD NVMe ou SATA rápido.  
- **Por que fazer:** assets carregam rápido, texturas aparecem no tempo certo e você não chega atrasado no loot.  
- **Como reverter:** para mover o jogo, use a opção **Mover** da Steam/Epic para outro drive.  
- **Impacto esperado:** renderização imediata em hot drops e menos “borrachudos” no chão.
