@echo off
cd /d %~dp0
if exist venv rmdir /s /q venv
python-3.12.7-amd64.exe -m venv venv
.
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install -r requirements.txt
