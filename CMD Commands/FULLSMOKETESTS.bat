echo off
start /min cmd.exe  /k "call cd C:\Users\Roy Braish\AppData\Local\Android\Sdk\emulator && emulator.exe -avd Pixel_4_XL_API_33 -no-boot-anim -gpu on"
start /min cmd.exe  /k "call appium -a 127.0.0.1 -p4723 --allow-cors --session-override --bootstrap-port 4723 --relaxed-security"

cd C:\Users\Roy Braish\Roy Personal\Appium-Automation-Python\GUI
python GUI.py
SET /A a = %ERRORLEVEL% 
echo %a%
start /min cmd.exe  /k "call python GUIProgressBar.py"

cd C:\Users\Roy Braish\Roy Personal\Appium-Automation-Python\BaseClasses

set T=
SETLOCAL EnableDelayedExpansion
for /f "Tokens=* Delims=" %%x in (KYC_3.0_JSON_File.json) do set T=!T!%%x
SET SUBSTRING=!T:~36,4!
echo %SUBSTRING%
if %SUBSTRING% == True (
	echo Pulling Code from Github...
	git pull origin main
	)
if %SUBSTRING% == Fals echo No need to pull code!

if %a% == 1 (python FullUserBaseClass.py)
if %a% == 4 (python SmokeTests.py)



cmd \k