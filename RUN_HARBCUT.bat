@echo off
title HarbCut Launcher
cd /d "%~dp0"
echo Starting HarbCut...
"C:\Users\a7med\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe" src/harbcut.py
echo.
echo Process exited with code %ERRORLEVEL%.
pause