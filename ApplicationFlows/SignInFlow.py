from time import sleep
from CheckFlowAndProceed import CheckFlow_ContinueReg_Showme
from GetStartedScreen import GetStartedScreen_SignIn
from SignInScreen import SignInScreen_Test


def SignInFlow(driver,ReportDriver, Credentials):
    GetStartedScreen_SignIn(driver,ReportDriver)
    SignInScreen_Test(driver,ReportDriver, Credentials["Email"],Credentials["Password"])
    try:CheckFlow_ContinueReg_Showme(driver,ReportDriver,Credentials)
    except:sleep(0.1)