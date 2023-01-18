from datetime import datetime
import SystemPath
import json
import os
from pathlib import Path
import sys 
from time import sleep

from AnalyzeFinalResults_SendEmail import AnalyzeFinalResults
from colorama import Fore
from CheckAndRunExternalPrograms import RunProgramsonMAC
from ChooseBuildtoRunOn import ChooseBuild
from ClosePrograms import ClosePrograms
from EmailCount import EmailCountAPI
from FullOfflineUserSmokeTests import FullOffineSmokeTests
from FullUserSmokeTests import FullUserSmokeTests
from HTMLFunctions import InitializeHTMLReport
from ManualReport import ReportResults
from Platform_OS import getplatform_OS
from TestRailReporting import GetCases
ReportDriver=None

operating_system=getplatform_OS()
if operating_system == "MAC":
    RunProgramsonMAC()
elif operating_system == "Windows":
    print("The programs are already running from batch file")

sleep(5)


print("")
print(Fore.GREEN+"Full Smoke Tests"+Fore.RESET)
print("Full Smoke Tests",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
print("")
sleep(2)

# InitializeHTMLReport()

with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
# Load its content and make a new dictionary
    JSON=json.load(file)
FeatureName=JSON["TechnicalVariables"]["FeatureName"].lower()
if JSON["TestRailSmokeTests"]["Status"].lower() == "enabled":
    TestRail=True
    run_id=JSON["TestRailSmokeTests"]["run_id"]
else : TestRail=False

if TestRail==True:GetCases(int(run_id))


##################################################################
Credentials = { 
    "FirstName":"test",
    "LastName":"test",
    "Email": "roy.braish+"+FeatureName+str(1)+"@neo.ae",
    "Password": "Password123",
    "MobileNumber":"5900 0098",
    "RiskScore":"5",
    "User_Type":"Islamic",
    "BuildName":JSON["TechnicalVariables"]["BuildName"]
}
##################################################################

Statuses=[]

if JSON["TechnicalVariables"]["Time_in_Tkinter"]<=85:
    t=85-JSON["TechnicalVariables"]["Time_in_Tkinter"]
    print("Please wait "+str(t)+" seconds for the emulator to run...",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Please wait "+timer+" seconds for the emulator to run...", end="\r")
        sleep(1)
        
        t -= 1
        
    ERASE_LINE = '\x1b[2K' 
    sys.stdout.write(ERASE_LINE) 

    
now = datetime.now()

TestStarted= now.strftime("%d/%m/%Y %H:M:%S")
print("Test Started at: \n", TestStarted)	 
# print(1)
ReportResults(ReportDriver,"N/A",True,"Test Started at: " + TestStarted,"N/A","N/A")


Passed=FullUserSmokeTests(ReportDriver,Credentials,FeatureName,"ETF","5","Predefined","Bank Transfer","Bank Transfer")
sleep(1)
Statuses.append(Passed)

Passed=FullUserSmokeTests(ReportDriver,Credentials,FeatureName,"ETF","10","Customized","Bank Transfer","Bank Transfer")
sleep(1)
Statuses.append(Passed)

Passed=FullUserSmokeTests(ReportDriver,Credentials,FeatureName,"Islamic","7","Predefined","Bank Transfer","Bank Transfer")
sleep(1)
Statuses.append(Passed)

Passed=FullUserSmokeTests(ReportDriver,Credentials,FeatureName,"Islamic","3","Customized","Bank Transfer","Bank Transfer")
sleep(1)
Statuses.append(Passed)

Passed=FullOffineSmokeTests(ReportDriver,Credentials,"offline","1000")
sleep(1)
Statuses.append(Passed)



now = datetime.now()
TestEnded= now.strftime("%d/%m/%Y %H:%M:%S")
print("Test Ended at: \n", TestEnded)	
ReportResults(ReportDriver,"N/A",True,"Test Ended at: " + TestEnded,"N/A","N/A")


if ReportDriver!=None:ReportDriver.quit()
AnalyzeFinalResults(Statuses)
# ClosePrograms()



os.system("pause")
# Open Test Results in chrome tab
#url = "file:\\C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\TestResults.html"
#webbrowser.open(url,new=2)


