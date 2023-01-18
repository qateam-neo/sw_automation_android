from datetime import datetime
import json
import SystemPath
from time import sleep
from ActivateUser import ActivateUser
from AddFundstoPortfolio import AddFundsFlow
from AnalyzeFinalResults_SendEmail import AnalyzeFinalResults
from colorama import Fore
from ApproveUserByCivilID import ApproveUserByCivilID
from BookaCall import BookaCall
from CheckFlowAndProceed import CheckFlow_ContinueReg_Showme
from ClosePrograms import ClosePrograms
from ConfigureDevices import ConfigureDeviceEmulator, ConfigureDeviceEmulatorNoApp
from ConfirmMobileScreen import ConfirmMobileScreen_Test
from FingerPrintScreen import FingerPrintScreen_Test
from GesturesAndMotions import RefreshScreenusingswipe
from GetProfileAPIReturnID import GetProfileAPIReturnID
from GetTokenAPI import GetTokenAPI
from KYC import KYC_FillAll


from ManualReport import ReportResults, ReportUserFinalResults
from PendingDashboard import PendingDashboard
from PerformInitialDepositFlow import InitialDepositFlow
from SignContractAPI import SignContractAPI
from SignInFlow import SignInFlow
from TestRailReporting import AnalyzeTestTrailResults
from UploadIDs import UploadIDusingAPI_SmokeTest
from VerifyEmail import VerifyEmailusingAPI
from WithdrawalFlow import WithdrawalFlow
sleep(3)


print("")
print(Fore.GREEN+"Full Smoke Tests"+Fore.RESET)
print("Full Smoke Tests",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
print("")

sleep(2)

with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
# Load its content and make a new dictionary
    JSON=json.load(file)
FeatureName=JSON["TechnicalVariables"]["FeatureName"].lower()


##################################################################
Credentials = {
    "FirstName":"test",
    "LastName":"test",
    "Email": "roy.braish+test275@neo.ae",
    "Password": "Password123",
    "MobileNumber":"5900 0098",
    "RiskScore":"5",
    "User_Type":"Islamic",
    "BuildName":JSON["TechnicalVariables"]["BuildName"]
}
##################################################################

ReportDriver=None
    
now = datetime.now()

TestStarted= now.strftime("%d/%m/%Y %H:%M:%S")
print("Test Started at: \n", TestStarted)	
print(1)
ReportResults(ReportDriver,"N/A",True,"Test Started at: " + TestStarted,"N/A","N/A")


driver=ConfigureDeviceEmulator(ReportDriver,Credentials)
SignInFlow(driver,ReportDriver,Credentials)
            
Authorization=GetTokenAPI(Credentials["Email"])
# print(Authorization)
# User_ID=UploadIDusingAPI_SmokeTest(driver,ReportDriver,Credentials,Auth)
User_ID=GetProfileAPIReturnID(Authorization,ReportDriver,Credentials["Email"],Credentials["Password"])
# print(User_ID)
# VerifyEmailusingAPI(driver,ReportDriver,Credentials["Email"],Credentials["Password"],Authorization)
# User_ID=UploadIDusingAPI_SmokeTest(driver,ReportDriver,Credentials,Authorization)

# BookaCall(driver,ReportDriver,False,True)
# SignContractAPI(driver, ReportDriver,User_ID)
# ApproveUserByCivilID(driver,ReportDriver,Credentials)


# PendingDashboard(driver,ReportDriver)


# # InitialDepositFlow(driver,ReportDriver,User_ID,"bank","islamic")
# InitialDepositFlow(driver,ReportDriver,User_ID,"knet","etf")
# ActivateUser(ReportDriver,driver,User_ID)

try:
    ConfirmMobileScreen_Test(driver,ReportDriver,Credentials["MobileNumber"])
    FingerPrintScreen_Test (driver,ReportDriver)
except:  
    try:RefreshScreenusingswipe(driver)
    except:print("Can't Refresh Screen")
    
    
# PendingDashboard(driver,ReportDriver)
# KYC_FillAll(driver,ReportDriver,JSON)
# BookaCall(driver,ReportDriver,False,True)
# SignContractAPI(driver, ReportDriver,User_ID)
# ApproveUserByCivilID(driver,ReportDriver,Credentials)


# Step 3: Initial Deposit flow + Activation 
PendingDashboard(driver,ReportDriver)
InitialDepositFlow(driver,ReportDriver,User_ID,"knet","etf")
ActivateUser(ReportDriver,driver,User_ID)

# # AddFundsFlow(driver,ReportDriver,"bank","islamic",10000)
# AddFundsFlow(driver,ReportDriver,"knet","etf",10000)

WithdrawalFlow(driver,ReportDriver,"Full",User_ID,1000)

WithdrawalFlow(driver,ReportDriver,"Partial",User_ID,1000)



TestDone=True
TestRail="enabled"
if TestDone==True:
    ReportUserFinalResults(ReportDriver,TestDone,"ETF","5","Predefined")
    if TestRail == "enabled":
        AnalyzeTestTrailResults("etf","predefined")    

now = datetime.now()
TestEnded= now.strftime("%d/%m/%Y %H:%M:%S")
print("Test Ended at: \n", TestEnded)	
ReportResults(ReportDriver,"N/A",True,"Test Ended at: " + TestEnded,"N/A","N/A")


if ReportDriver!=None:ReportDriver.quit()

