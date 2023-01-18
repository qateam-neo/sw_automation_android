 if not "%1" == "max" start /MAX cmd /c %0 max & exit/b

 cd C:\Users\Roy Braish\Roy Personal\Appium-Automation-Python\BackEndSmokeTests
pytest test_pytest_smoke.py --self-contained-html --env "internal" --html="C:\Users\Roy Braish\Roy Personal\Appium-Automation-Python\BackEndSmokeTests\BasicReport.html"

pytest test_pytest_specific_scenarios.py -n 4 --self-contained-html --env "internal" --html="C:\Users\Roy Braish\Roy Personal\Appium-Automation-Python\BackEndSmokeTests\BasicReport.html"

cmd /k