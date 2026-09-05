@echo off
pushd %~dp0

if not "%1"=="am_admin" (
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList 'am_admin'"
    exit /b
)

set "exe=%cd%\exe\"
set "src=%cd%\src\"

echo Updating UIs
for %%f in ("%exe%\*.ui") do (
    "C:\Users\a7med\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe" -m PyQt6.uic.pyuic "%%f" -o "%src%\ui\%%~nf.py"
)

echo Running script
"C:\Users\a7med\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe" "%src%harbcut.py"

pause