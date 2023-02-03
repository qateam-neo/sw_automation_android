import os
print
import base64
from time import sleep
import traceback
from AddFundstoPortfolio import AddFundsFlow
from GetTokenAPI import GetTokenAPI
from ManualReport import ReportResultsUserSmokeTest, ReportUserFinalResults
from SendEmail import SendEmail
from SendSlack import slack_frontend
from SignInFlow import SignInFlow
from TestRailReporting import AnalyzeTestTrailResults
from WithdrawalFlow import WithdrawalFlow
from ConfigureDevices import ConfigureDeviceEmulator
from GetProfileAPIReturnID import GetProfileAPIReturnID
slack=slack_frontend()

def FullOffineSmokeTests(ReportDriver,Credentials,User_Type,AdditionalDeposit="Bank Transfer",AdminAuthorization=None):
    
    TestRailCases=[False,False,False]
    User_Type = "offline"
    AdditionalDeposit = AdditionalDeposit.lower()
    
    ReportDriver=None

    TestDone=False
    Credentials["Email"]="bilal.sleiman+uatoffline27@neo.ae"
    ReportResultsUserSmokeTest(ReportDriver,True,User_Type,"X","X")

   
    try:
        while True:
            try:
                driver=ConfigureDeviceEmulator(ReportDriver,Credentials)
                break
            except:
                sleep(2)
             
                
        driver.start_recording_screen()
            
        SignInFlow(driver,ReportDriver,Credentials)
        sleep(5)
        Auth=GetTokenAPI("bilal.sleiman+uatoffline27@neo.ae")
        User_ID=GetProfileAPIReturnID(Auth,ReportDriver,"bilal.sleiman+uatoffline27@neo.ae",Credentials["Password"])
        # try:CheckFlow_ContinueReg_Showme(driver,ReportDriver,Credentials)
        # except:sleep(0.1)
        # PendingDashboard(driver,ReportDriver)
        # InitialDepositFlow(driver,ReportDriver,User_ID,"Bank Transfer","etf")
        # ActivateUser(ReportDriver,driver,User_ID)

        video_rawdata=driver.stop_recording_screen()
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess_%s(1).mp4" % (User_Type),"wb+") as vd:
                vd.write(base64.b64decode(video_rawdata))



        driver.start_recording_screen()        

        AddFundsFlow(driver,ReportDriver,"bank transfer","ETF",10000)
        WithdrawalFlow(driver,ReportDriver,"Full",User_ID,1000)
        WithdrawalFlow(driver,ReportDriver,"Partial",User_ID,1000)
        
        video_rawdata=driver.stop_recording_screen()
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess_%s(2).mp4" % (User_Type),"wb+") as vd:
                vd.write(base64.b64decode(video_rawdata))


        TestDone=True
        TestRail="enabled"
        if TestDone==True:
            ReportUserFinalResults(ReportDriver,TestDone,"offline","X","X")
            if TestRail:
                AnalyzeTestTrailResults("offline","N/A")

        

    except Exception as e:
        print(e)
        traceback.print_exc()

        video_rawdata=driver.stop_recording_screen()

        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\ErrorVideoforSmokeTest_%s.mp4" % (User_Type),"wb+") as vd:
                vd.write(base64.b64decode(video_rawdata))
        
        SendEmail(False,Credentials["Email"],User_Type,  "X","X",Credentials["Email"])
        slack.send_results(False,Credentials["Email"],User_Type,  "X","X",Credentials["Email"])
        print("Error in test check video!")
        TestDone=False        
    return TestDone