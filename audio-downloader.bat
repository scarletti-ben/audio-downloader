@ECHO off

@REM Set the current working directory to the directory of this .bat file
CD /d "%~dp0"

@REM Activate the virtual environment and run main.py
CALL venv\Scripts\activate & venv\Scripts\python.exe main.py %*

@REM Open a Windows explorer window in the downloads directory
START downloads