@ECHO OFF
:start
title howtopronounce
echo [STARTER] Starting...
python cli.py
if %errorlevel% == 1212 (
	echo Installing Requirements...
	pip install -r requirements.txt
	cls
	goto :start
)
pause
exit
