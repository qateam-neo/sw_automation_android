import SystemPath
import os
import sys
from time import sleep
sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests")

from SendSlack import slack_backend
SlackReporting=slack_backend()


smoke=os.system('cd C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\smoke && pytest -x --env "UAT INTERNAL" --self-contained-html --html="C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\smoke\\SmokeTests_Report.html" ')
# if smoke!=0:
#     SlackReporting.send_results(False,"Smoke Tests")
#     raise ValueError('Smoke Tests Failed!!')

admin=os.system('cd C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\Admin && pytest --self-contained-html --html="C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\Admin\\Admin_Report.html" ')
# if admin!=0:
#     SlackReporting.send_results(False,"Admin Tests")
#     raise ValueError('Admin Tests Failed!!')


specific_scenarios=os.system('cd C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\specific_scenarios && pytest -x --env "UAT INTERNAL" -n 4 --self-contained-html  --html="C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\specific_scenarios\\SpecificTests_Report.html" ')
# if specific_scenarios!=0:
#     SlackReporting.send_results(False,"Specific Tests")
#     raise ValueError("Specific Scenarios Failed!!")

# if specific_scenarios==0 and smoke ==0 and admin==0:
#     SlackReporting.send_results(True)

# # os.system('cd C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\smoke && pytest --env "UAT INTERNAL" --self-contained-html --html="C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\smoke\\SmokeTests_Report.html" ')
# os.system('cd C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\specific_scenarios && pytest --env "UAT INTERNAL" -n 4 --self-contained-html  --html="C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\specific_scenarios\\SpecificTests_Report.html" ')


