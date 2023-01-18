import base64
import json
from time import sleep
import traceback
from datetime import datetime
from ActivateUser import ActivateUser
from AddFundstoPortfolio import AddFundsFlow
from ApproveUserByCivilID import ApproveUserByCivilID
from BookaCall import BookaCall
from ConfirmMobileScreen import ConfirmMobileScreen_Test
from EmailCount import EmailCountAPI, EmailCountAPI_SingleUser_ReturnFullEmail
from FingerPrintScreen import FingerPrintScreen_Test
from GesturesAndMotions import RefreshScreenusingswipe
from GetTokenAPI import GetTokenAPI, PostTokenAPI
from KYC import KYC_FillAll
from ManualReport import ReportResultsUserSmokeTest, ReportUserFinalResults
from PendingDashboard import PendingDashboard
from PerformInitialDepositFlow import InitialDepositFlow
from SendEmail import SendEmail
from SendSlack import slack_frontend
from SignContractAPI import SignContractAPI
from SignInFlow import SignInFlow
from SignUpFlow import SignUpFlow
from TestRailReporting import AnalyzeTestTrailResults, AnalyzeTestTrailResults_Fail, AnalyzeTestTrailResults_Retest, GetCases
from UploadIDs import UploadIDusingAPI_SmokeTest
from VerifyEmail import VerifyEmailusingAPI
from WithdrawalFlow import WithdrawalFlow
from AnalyzeFinalResults_SendEmail import AnalyzeFinalResults
from colorama import Fore
from ClosePrograms import ClosePrograms
from ConfigureDevices import ConfigureDeviceEmulator, ConfigureDeviceEmulatorNoApp
from selenium.webdriver.support.ui import WebDriverWait # needs to be used when creating a function everytime
from selenium.webdriver.support import expected_conditions # needs to be used when creating a function everytime
from selenium.webdriver.common.by import By



def FullUserSmokeTests(ReportDriver,Credentials,FeatureName,User_Type,RiskScore,OnboardingFlow,InitialDeposit="Bank Transfer",AdditionalDeposit="Bank Transfer",AdminAuthorization=None):
    slack=slack_frontend()
    #User_Type: ETF or Islamic
    #RiskScore: User's risk score
    #Onboarding Type: Customized or Predefined
    TestRailCases=[False,False,False,False,True,True]
    FeatureName = FeatureName.lower()
    User_Type = User_Type.lower()
    OnboardingFlow = OnboardingFlow.lower()
    InitialDeposit = InitialDeposit.lower()
    AdditionalDeposit = AdditionalDeposit.lower()
    
    Email=EmailCountAPI_SingleUser_ReturnFullEmail(ReportDriver,"roy.braish+"+FeatureName+OnboardingFlow+User_Type+"@neo.ae")

    TestDone=False
    Credentials["Email"]=Email
    
    count=1
    while TestDone==False and count<=3:
        if count>1:
            Status=False # We mean here that it failed the first time and now retrying... 

        else:
            Status=True # We mean here that the test started for the first time now...

        sleep(2)
        ReportResultsUserSmokeTest(ReportDriver,Status,User_Type,RiskScore,OnboardingFlow)


        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
        # Load its content and make a new dictionary
            JSON=json.load(file)
            
        if JSON["TestRailSmokeTests"]["Status"].lower() == "enabled":
            TestRail=True
            run_id=JSON["TestRailSmokeTests"]["run_id"]
        else : TestRail=False



        try:
            while True:
                try:
                    driver=ConfigureDeviceEmulator(ReportDriver,Credentials)
                    break
                except:
                    sleep(2)
            # print(Credentials)
            driver.start_recording_screen()
            Credentials=SignUpFlow(driver,ReportDriver,Credentials,JSON,User_Type,RiskScore,OnboardingFlow)
            print(Credentials)
            print(Credentials["Email"])
            sleep(3)
            Authorization=GetTokenAPI(Credentials["Email"])
            VerifyEmailusingAPI(driver,ReportDriver,Credentials["Email"],Credentials["Password"],Authorization)
            User_ID=UploadIDusingAPI_SmokeTest(driver,ReportDriver,Credentials,Authorization)
            
            while True:
                try:
                    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/signedUpTv")
                    break
                except:
                    try:
                        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
                        break
                    except:
                        try:driver.find_element(By.ID, "neo.nbkc.smartwealth.demo:id/intercom_close_background").click()
                        except:


                            #Still loading
                            F=None
            

            # Step 1: Upload IDs 
            # PendingDashboard(driver,ReportDriver)
            # UploadIDSmokeTests(driver,ReportDriver)

            video_rawdata=driver.stop_recording_screen()
            with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess%s_%s_%s(SignUp_VerifyEmail_UploadID).mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
                    vd.write(base64.b64decode(video_rawdata))
                    
            driver.start_recording_screen()        
            # Step 2: Fill KYC + Sign Contract + Approve User from Admin using API collection 
            PendingDashboard(driver,ReportDriver)
            KYC_FillAll(driver,ReportDriver,JSON)
            
            video_rawdata=driver.stop_recording_screen()
            with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess%s_%s_%s(KYC).mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
                    vd.write(base64.b64decode(video_rawdata))

            driver.start_recording_screen()        
                                
            # SignContract(driver,ReportDriver)
            BookaCall(driver,ReportDriver,False,True)
            SignContractAPI(driver, ReportDriver,User_ID)
            ApproveUserByCivilID(driver,ReportDriver,Credentials)


            # Step 3: Initial Deposit flow + Activation 
            PendingDashboard(driver,ReportDriver)
            InitialDepositFlow(driver,ReportDriver,User_ID,InitialDeposit,User_Type)
            ActivateUser(ReportDriver,driver,User_ID)
            
            TestRailCases[0]=True
            
            video_rawdata=driver.stop_recording_screen()
            with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess%s_%s_%s(ActivateUser).mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
                    vd.write(base64.b64decode(video_rawdata))



            driver.start_recording_screen()        

            try:
                ConfirmMobileScreen_Test(driver,ReportDriver,Credentials["MobileNumber"])
                FingerPrintScreen_Test (driver,ReportDriver)
            except:  
                try:RefreshScreenusingswipe(driver)
                except:print("Can't Refresh Screen")
                
            AddFundsFlow(driver,ReportDriver,AdditionalDeposit,User_Type,10000)
            TestRailCases[1]=True
            WithdrawalFlow(driver,ReportDriver,"Full",User_ID,1000)
            TestRailCases[2]=True
            WithdrawalFlow(driver,ReportDriver,"Partial",User_ID,1000)
            TestRailCases[3]=True
            
            video_rawdata=driver.stop_recording_screen()
            with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess%s_%s_%s(DepositAndWithdrawalFlows).mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
                    vd.write(base64.b64decode(video_rawdata))
                    
            TestDone=True
            if TestDone==True:
                ReportUserFinalResults(ReportDriver,TestDone,User_Type,RiskScore,OnboardingFlow)
                if TestRail:
                    sleep(1)
                    AnalyzeTestTrailResults(User_Type,OnboardingFlow)    
            count=count+1

        except Exception as e:
            print(e)
            traceback.print_exc()
            

            video_rawdata=driver.stop_recording_screen()

            with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\ErrorVideoforSmokeTest%s_%s_%s.mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
                    vd.write(base64.b64decode(video_rawdata))
            
            # slack.send_results(False,Credentials["Email"],User_Type, RiskScore,OnboardingFlow,Credentials["Email"])
            print(Fore.RED+"Error in test check video!"+Fore.RESET)
            if count<3:
                AnalyzeTestTrailResults_Retest(User_Type,OnboardingFlow,str(e))
            TestDone=False
            count=count+1

            if TestDone == False:
                AnalyzeTestTrailResults_Fail(User_Type,OnboardingFlow,str(e))
        return TestDone
  
