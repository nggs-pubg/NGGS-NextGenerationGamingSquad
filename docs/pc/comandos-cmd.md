# Otimizador NGGS (comandos CMD)

- Download automático: [`nggs-otimizador.bat`](../assets/scripts/nggs-otimizador.bat) — execute como administrador.  
- Execução manual passo a passo: [`nggs-passos-manual.txt`](../assets/scripts/nggs-passos-manual.txt)

> **Aviso:** use apenas em sessões locais no Windows com privilégios de administrador. O script segue recomendações oficiais e não altera registros críticos.

## O que o script faz

| Etapa | Descrição | Por que fazer | Como reverter | Impacto esperado |
| --- | --- | --- | --- | --- |
| Limpeza de temporários | Remove arquivos do `%TEMP%` e `C:\Windows\Temp`. | Libera espaço e evita caches corrompidos entre atualizações do PUBG. | Não há reversão; arquivos temporários são regenerados automaticamente. | Reduz stutter causado por arquivos travados. |
| Otimização de rede | `ipconfig /flushdns`, `ipconfig /release`, `ipconfig /renew`, `netsh int ip reset`, `netsh winsock reset`. | Restaura pilha TCP/IP e renova DNS para conexões mais estáveis. | Reinicie o roteador ou utilize `netsh winsock reset catalog` caso queira restaurar manualmente. | Menos perda de pacotes e ping mais consistente. |
| Plano de energia | `powercfg /setactive SCHEME_MIN`. | Força o plano **Alto Desempenho** antes dos treinos. | Reabra as configurações de energia e escolha o plano anterior (ex.: Balanceado). | Clocks mais estáveis em partidas longas. |

## Como usar

### Opção A — Arquivo `.bat`
1. Baixe o arquivo `nggs-otimizador.bat`.  
2. Clique com o botão direito e escolha **Executar como administrador**.  
3. Aguarde a conclusão e reinicie o PC.

### Opção B — Comandos manuais
1. Abra o Prompt de Comando como administrador.  
2. Execute os comandos na ordem indicada no arquivo `nggs-passos-manual.txt`.  
3. Reinicie o PC ao finalizar.

### Recomendações
- Utilize o procedimento no máximo 1 vez por semana ou quando notar instabilidade.  
- Combine com o [checklist geral](checklist.md) para garantir que drivers e updates estão em dia.  
- Não edite os comandos sem validação prévia do staff técnico.

## Conteúdo do arquivo `.bat`

```bat
:: NGGS - Otimização rápida de rede e limpeza temporária
@echo off
color 0b
setlocal enabledelayedexpansion

Title NGGS - Otimizador seguro para treinos

:: Solicita execução como administrador
openfiles >nul 2>&1 || (
  echo [NGGS] Execute este arquivo como Administrador antes de continuar.
  pause
  exit /b 0
)

echo =====================================================
echo  NGGS - Rotina legítima de manutenção
echo 1) Limpeza de temporários do Windows
if exist "%TEMP%" (
  echo    >> Removendo arquivos temporários do usuario
  del /q /f /s "%TEMP%\*" >nul 2>&1
)
if exist "C:\Windows\Temp" (
  echo    >> Limpando temporarios do sistema
  del /q /f /s "C:\Windows\Temp\*" >nul 2>&1
)

echo.
echo 2) Otimizacao de rede (DNS + Winsock)
ipconfig /flushdns
ipconfig /release
ipconfig /renew
netsh int ip reset
netsh winsock reset

echo.
echo 3) Ajuste de energia para alto desempenho
powercfg /setactive SCHEME_MIN

echo.
echo Operacao concluida. Reinicie o computador antes do proximo treino.
echo Pressione qualquer tecla para fechar...
pause >nul
endlocal
```
