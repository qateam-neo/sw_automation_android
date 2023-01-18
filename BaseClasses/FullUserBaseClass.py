from datetime import datetime
import SystemPath
import json
import os
import sys 
from time import sleep
from AnalyzeFinalResults_SendEmail import AnalyzeFinalResults
from ClosePrograms import ClosePrograms
from FullSingleUser import FullUserTest
from HTMLFunctions import GenerateReport, InitializeHTMLReport
from ManualReport import ReportResults
from colorama import Fore 

from TestRailReporting import SaveTestsIDJSON



sleep(5)
print(Fore.GREEN+"\nSingle User Test\n"+Fore.RESET)
print("\nSingle User Test\n",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
sleep(2)

InitializeHTMLReport()

with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
# Load its content and make a new dictionary
    JSON=json.load(file)

if "enabled" in JSON["TestRailSmokeTests"]["Status"]:
        # print("Please wait while we gather your TestRail Info...",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
    SaveTestsIDJSON()

##################################################################
EmailCount=1
Credentials = {
    "FirstName":"test",
    "LastName":"test",
    "Email": JSON["SingleUserDetails"]["Email"].lower(),
    "Password": "Password123",
    "MobileNumber":JSON["KYC_3.0"]["AddressInfo_Fields"]["Mobile number"].lower(),
    "RiskScore":JSON["SingleUserDetails"]["RiskScore"].lower(),
    "User_Type":JSON["SingleUserDetails"]["User_Type"].lower(),
    "BuildName":JSON["TechnicalVariables"]["BuildName"]
}
##################################################################
ReportDriver=None


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

TestStarted= now.strftime("%d/%m/%Y %H:%M:%S")
print("Test Started at: \n", TestStarted)	

ReportResults(ReportDriver,"N/A",True,"Test Started at: " + TestStarted,"N/A","N/A")

Passed=FullUserTest(ReportDriver,Credentials)

now = datetime.now()
TestEnded= now.strftime("%d/%m/%Y %H:%M:%S")
print("Test Ended at: \n", TestEnded)	
ReportResults(ReportDriver,"N/A",True,"Test Ended at: " + TestEnded,"N/A","N/A")

GenerateReport()
AnalyzeFinalResults(Passed)
ClosePrograms()



os.system("pause")
# Open Test Results in chrome tab
#url = "file:\\C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\TestResults.html"
#webbrowser.open(url,new=2)


