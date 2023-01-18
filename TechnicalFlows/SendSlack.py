    
# Install Courier SDK: pip install trycourier
import os
from zipfile import ZipFile

from slack import WebClient
from slack.errors import SlackApiError
class slack_frontend():
    def __init__(self):
        self.client = WebClient(token='xoxb-134023292596-4252125743892-UP6YGMgXLH8hVdwJK0BMOXYl')
        
    def zip_results(self):
        zipObj = ZipFile('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\Reports\\frontend_html_results.zip', 'w')
        # Add multiple files to the zip
        zipObj.write('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\Reports\\frontend_html_results.html')
        # close the Zip File
        zipObj.close()

    def send_results(self,Passed,EmailTO="roy.braish@neo.ae",User_Type="N/A", RiskScore="N/A",OnboardingFlow="N/A",EmailFROM="roy.braish@neo.ae"):
        
        if Passed: # Final test Passed!!

            
            self.comment="""
:white_check_mark: :white_check_mark: :white_check_mark:
Welcome Tester! :tada:\n
*Your Frontend Test has ended Successfully!!* \n\n
Great Build, Keep it up :muscle: :rocket:
            """
                
        elif Passed==False and (User_Type =="N/A" or OnboardingFlow == "N/A" or RiskScore=="N/A"): # Final test Failed!!

            self.comment="""
:x: :x: :x:
Welcome Tester!\n
*Your Frontend Test Failed!!*

Please Try Again...
                        """
                
        else: #User test failed and retrying!!

            self.comment="""
:x: :x: :x:
Welcome Tester!\n
*An %s user with Risk Score %s and going through the %s Test has Failed...*
Retrying Again!!\n
The test hasn't ended yet!
Keep up hope :crossed_fingers:
"""% (User_Type,RiskScore,OnboardingFlow)
        self.zip_results()
        new_file = self.client.files_upload(
        channels="C04CZNN6DT7",  # You can specify multiple channels here in the form of a string array
        title="Android Frontend Test Results", 
        file="C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\Reports\\frontend_html_results.zip",
        filetype="zip",
        # content="Hi there! This is a text file!",
        initial_comment=self.comment)

        
from slack import WebClient
from slack.errors import SlackApiError
class slack_backend():

    def zipallreports(self):
        zipObj = ZipFile('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Reports.zip', 'w')
        # Add multiple files to the zip
        zipObj.write('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Tests\\smoke\\SmokeTests_Report.html')
        zipObj.write('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\BackEndSmokeTests\Tests\specific_scenarios\SpecificTests_Report.html')
        zipObj.write('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\BackEndSmokeTests\Tests\Admin\Admin_Report.html')
        # close the Zip File
        zipObj.close()

    def zip_smoketests_report(self):
        self.zipObj = ZipFile('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Reports.zip', 'w')
        # Add multiple files to the zip
        self.zipObj.write('BackEndSmokeTests\\Tests\\smoke\\SmokeTests_Report.html')
        # self.zipObj.write('BackEndSmokeTests\\Tests\\specific_scenarios\\SpecificTests_Report.html')
        # close the Zip File
        self.zipObj.close()

    def zip_specifictests_report(self):
        self.zipObj = ZipFile('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Reports.zip', 'w')
        # Add multiple files to the zip
        # self.zipObj.write('BackEndSmokeTests\\Tests\\smoke\\SmokeTests_Report.html')
        self.zipObj.write('BackEndSmokeTests\\Tests\\specific_scenarios\\SpecificTests_Report.html')
        # close the Zip File
        self.zipObj.close()
  
    def zip_admin_report(self):
        self.zipObj = ZipFile('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Reports.zip', 'w')
        # Add multiple files to the zip
        # self.zipObj.write('BackEndSmokeTests\\Tests\\smoke\\SmokeTests_Report.html')
        self.zipObj.write('BackEndSmokeTests\\Tests\\Admin\\Admin_Report.html')
        # close the Zip File
        self.zipObj.close()

  
    def send_results(self,Passed,FailedStep="N/A",EmailTO="roy.braish@neo.ae",EmailFROM="roy.braish@neo.ae"):
        
        if Passed:
            self.zipallreports()
            self.comment="""
:white_check_mark: :white_check_mark: :white_check_mark:
Welcome Tester! :tada:\n
*Your Backnend Test is Successful*
Please find your Reports attached!\n\n
Great Build, Keep it up :muscle: :rocket:
"""
        elif Passed ==False and "smoke" in FailedStep.lower():
            self.zip_smoketests_report()
            self.comment="""
:x: :x: :x:
Welcome Tester!\n
*Your backend test has Failed on smoke tests...*
Please find the error attached in the report below! \n
"""
            
        elif Passed ==False and "specific" in FailedStep.lower():
            self.zip_specifictests_report()
            self.comment="""
:x: :x: :x:
Welcome Tester!\n
*Your backend test has Failed on specific tests...*
Please find the error attached in the report below! \n
"""
        elif Passed ==False and "admin" in FailedStep.lower():
            self.zip_admin_report()
            self.comment="""
:x: :x: :x:
Welcome Tester!\n
*Your backend test has Failed on specific tests...*
Please find the error attached in the report below! \n
"""

    
        # ID of channel you want to post message to
        client = WebClient(token='xoxb-134023292596-4252125743892-UP6YGMgXLH8hVdwJK0BMOXYl')
        new_file = client.files_upload(
        channels="C04CZNN6DT7",  # You can specify multiple channels here in the form of a string array
        title="Backend Reports",
        file="C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests\\Reports.zip",
        filetype="zip",
        # content="Hi there! This is a text file!",
        initial_comment=self.comment)

