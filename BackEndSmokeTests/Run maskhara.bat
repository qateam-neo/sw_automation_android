if not "%1" == "max" start /MAX cmd /c %0 max & exit/b

cd C:\Users\Roy Braish\Roy Personal\Appium-Automation-Python\BackEndSmokeTests
pytest test_pytest_maskhara.py --self-contained-html --html="C:\Users\Roy Braish\Roy Personal\Appium-Automation-Python\BackEndSmokeTests\BasicReport.html"

pytest test_pytest_maskhara_copy.py -n 4 --self-contained-html --html="C:\Users\Roy Braish\Roy Personal\Appium-Automation-Python\BackEndSmokeTests\BasicReport.html"

cmd /k
