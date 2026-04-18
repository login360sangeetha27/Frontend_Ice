@echo off
REM Activate the Python virtual environment and start PowerShell
cd /d "%~dp0"
call venv\Scripts\activate.bat
powershell -NoExit
