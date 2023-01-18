for /L %%p in (0,1,15) do (
	set Status="False"
	adb kill-server
	adb start-server
	for /f %%i in ('adb devices') do (
		set RESULT=%%i
		echo %%i
			if %%i == emulator-5554 (
				set Status="True"
				echo "ABCD"
				goto :eof
			)

		)
	adb reconnect
	if Status=="True" (
		echo "EFGH"
		goto :eof
	)
	
)


cmd -k