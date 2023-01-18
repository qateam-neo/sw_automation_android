cd C:\Users\Roy\OneDrive\Desktop\Roy Personal\Appium Automation Python
:while
	set /P Pull=Do you want to pull code from GIT before running?(y or n): 
	if %Pull% == y git pull origin main
	if %Pull% == n echo "Starting Code... " 
	IF NOT %Pull%==n (
		IF NOT %Pull% == y (
		goto :while
		)
		)