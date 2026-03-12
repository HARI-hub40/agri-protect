@echo off
title AgriDetect - Starting...

:: Check if backend is already running on port 8001
netstat -ano | findstr ":8001" | findstr "LISTENING" >nul 2>&1
if %errorlevel% == 0 (
    echo [AgriDetect] Backend already running. Opening app...
    goto OPEN_APP
)

echo [AgriDetect] Cleaning up old processes...
taskkill /f /im python.exe /t >nul 2>&1
echo [AgriDetect] Starting Backend Server...

:: Start the backend server silently in background
start /min "" cmd /c "cd /d D:\agri && python -m uvicorn backend.app:app --host 0.0.0.0 --port 8001"

:: Wait for the server to be ready (max 30 seconds)
echo [AgriDetect] Waiting for server to start...
set /a count=0
:WAIT_LOOP
timeout /t 1 /nobreak >nul
netstat -ano | findstr ":8001" | findstr "LISTENING" >nul 2>&1
if %errorlevel% == 0 goto OPEN_APP
set /a count+=1
if %count% lss 30 goto WAIT_LOOP

echo [AgriDetect] Server took too long. Check your Python setup.
pause
exit

:OPEN_APP
echo [AgriDetect] Opening AgriDetect App...
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --app=http://127.0.0.1:8001 --start-maximized
exit
