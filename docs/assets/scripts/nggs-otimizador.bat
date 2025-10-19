:: NGGS - Otimização rápida de rede e limpeza temporária
@echo off
color 0b
setlocal enabledelayedexpansion

Title NGGS - Otimizador seguro para jogatinas

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
echo Operacao concluida. Reinicie o computador antes da proxima jogatina.
echo Pressione qualquer tecla para fechar...
pause >nul
endlocal
