:: NGGS - Manutenção conservadora e opcional
@echo off
color 0b
setlocal

Title NGGS - Otimizador seguro para jogatinas

echo =====================================================
echo  NGGS - Manutencao conservadora
echo  Nenhuma etapa apaga arquivos ou redefine a rede.

echo.
choice /c SN /n /m "Limpar apenas o cache DNS? [S/N] "
if errorlevel 2 goto energia
ipconfig /flushdns || echo [AVISO] Nao foi possivel limpar o DNS.

:energia
echo.
choice /c SN /n /m "Ativar o plano Alto Desempenho? [S/N] "
if errorlevel 2 goto fim
powercfg /getactivescheme
powercfg /setactive SCHEME_MIN || echo [AVISO] Plano indisponivel neste computador.

:fim
echo.
echo Operacao concluida. Nao e necessario reiniciar.
echo Pressione qualquer tecla para fechar...
pause >nul
endlocal
