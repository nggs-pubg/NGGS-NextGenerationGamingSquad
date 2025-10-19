# Comandos NGGS — manutenção rápida no PC

## Otimizador NGGS (comandos CMD)

- Download automático: [`nggs-otimizador.bat`](../assets/scripts/nggs-otimizador.bat) — execute como administrador.
- Execução manual passo a passo: [`nggs-passos-manual.txt`](../assets/scripts/nggs-passos-manual.txt)

> **Aviso estilo NGGS:** use apenas no seu PC pessoal, com conta de administrador. O script segue recomendações oficiais e não toca em registros sensíveis, mas sempre faça backup do que for importante.

### O que o script faz

| Etapa | Descrição | Por que fazer | Como reverter | Impacto esperado |
| --- | --- | --- | --- | --- |
| Limpeza de temporários | Remove arquivos do `%TEMP%` e `C:\Windows\Temp`. | Libera espaço e limpa caches que ficam pesados após updates do jogo. | Não há reversão; o Windows recria os arquivos sozinho. | Menos stutter causado por arquivos travados. |
| Otimização de rede | `ipconfig /flushdns`, `ipconfig /release`, `ipconfig /renew`, `netsh int ip reset`, `netsh winsock reset`. | Restaura a pilha TCP/IP e renova DNS para estabilizar conexões. | Reinicie o roteador ou use `netsh winsock reset catalog` se quiser restaurar manualmente. | Ping mais consistente e menos queda de pacote. |
| Plano de energia | `powercfg /setactive SCHEME_MIN`. | Ativa o plano **Alto desempenho** antes da jogatina. | Abra as configurações de energia e selecione o plano antigo (ex.: Balanceado). | Clocks firmes em sessões longas com os amigos. |

## Como usar

### Opção A — Arquivo `.bat`

1. Baixe o arquivo `nggs-otimizador.bat`.
2. Clique com o botão direito e escolha **Executar como administrador**.
3. Aguarde a conclusão e reinicie o PC.

### Opção B — Comandos manuais

1. Abra o Prompt de Comando como administrador.
2. Execute os comandos na ordem indicada no arquivo `nggs-passos-manual.txt` ou utilize a referência abaixo.
3. Reinicie o PC ao finalizar.

### Recomendações

- Rode a rotina no máximo 1 vez por semana ou quando notar que o PC ficou estranho.
- Combine com o [checklist geral](checklist.md) para garantir drivers e updates em dia.
- Evite alterar os comandos sem conversar com a equipe técnica ou entender bem cada etapa.

## Conteúdo do arquivo `.bat`

```bat
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
```

## Referência completa de comandos

> Para quem gosta de se aventurar além do script: use apenas se compreender cada parâmetro. Anote mudanças para poder desfazer depois.

### Prompt de Comando (CMD)

```cmd
bcdedit /set useplatformtick yes
bcdedit /set disabledynamictick yes
bcdedit /deletevalue useplatformclock false
bcdedit /set nx AlwaysOff
bcdedit /set tscsyncpolicy Enhanced FPS
bcdedit /set tscsyncpolicy Legacy input
```

### PowerShell

```powershell
reg add "HKCU\System\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f
reg add "HKCU\Software\Microsoft\GameBar" /v AllowAutoGameMode /t REG_DWORD /d 0 /f
reg add "HKCU\Software\Microsoft\GameBar" /v AutoGameModeEnabled /t REG_DWORD /d 0 /f
```

### Editor de Registro (Regedit)

- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`
  - Criar chave `Scheduler`
  - Definir `EnablePreemption` como `0`
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR`
  - Definir valor como `0`
- `HKEY_CURRENT_USER\Control Panel\Accessibility\MouseKeys`
  - Definir `Flags` como `0`
- `HKEY_CURRENT_USER\Control Panel\Accessibility\StickyKeys`
  - Definir `Flags` como `0`
- `HKEY_CURRENT_USER\Control Panel\Accessibility\Keyboard Response`
  - Definir `Flags` como `0`
- `HKEY_CURRENT_USER\Control Panel\Accessibility\ToggleKeys`
  - Definir `Flags` como `0`
