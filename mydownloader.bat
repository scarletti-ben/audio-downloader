@ECHO off

@REM Set the current working directory to the directory of this .bat file
CD /d "%~dp0"

@REM Activate the virtual environment and run main.py
CALL venv\Scripts\activate & venv\Scripts\python.exe main.py %*

@REM Open a Windows explorer window in the downloads directory
START downloads

@REM Virtual environments still append global system path, causing conflicts
@REM For production it is advised to clean sys.path in main.py manually
@REM Example: sys.path = [path for path in sys.path if 'venv' in path]
@REM THIS STILL DIDN'T FUCKING WORK
@REM PATH and other things are clearly strung together and you can't clean them all
@REM retval = subprocess.call(args)