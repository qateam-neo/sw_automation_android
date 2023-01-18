import SystemPath

from time import sleep
from ConfigureDevices import ConfigureDeviceEmulator
from ConfirmMobileScreen import ConfirmMobileScreen_Test
from FingerPrintScreen import FingerPrintScreen_Test
from GesturesAndMotions import RefreshScreenusingswipe
from GetProfileAPIReturnID import GetProfileAPIReturnID
from GetStartedScreen import GetStartedScreen_SignIn
from GetTokenAPI import GetTokenAPI
from Intensive_Tests.deposits.flows.wire_transfer.main import WireTransferFlow
from SignInFlow import SignInFlow




##################################################################
Credentials = { 
    "FirstName":"test",
    "Email":"roy.braish+testisbackend39@neo.ae",
    "LastName":"test",
    "Password": "Password123",
    "MobileNumber":"5900 0098",
    "RiskScore":"5",
    "User_Type":"Islamic",
}
##################################################################

ReportDriver=None
while True:
    try:
        driver=ConfigureDeviceEmulator(None,Credentials)
        break
    except:
        sleep(2)

 
# GetStartedScreen_SignIn(driver,ReportDriver)
SignInFlow(driver,ReportDriver,Credentials)
            
Authorization=GetTokenAPI(Credentials["Email"])

User_ID=GetProfileAPIReturnID(Authorization,ReportDriver,Credentials["Email"],Credentials["Password"])

try:
    ConfirmMobileScreen_Test(driver,ReportDriver,Credentials["MobileNumber"])
    FingerPrintScreen_Test (driver,ReportDriver)
except:  
    try:RefreshScreenusingswipe(driver)
    except:print("Can't Refresh Screen")
