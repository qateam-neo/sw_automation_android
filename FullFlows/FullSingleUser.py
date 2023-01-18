import base64
import json
import sys
from time import sleep
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from ActivateUser import ActivateUser
from AddFundstoPortfolio import AddFundsFlow
from AnalyzeFinalResults_SendEmail import AnalyzeFinalResults
from ApproveUserByCivilID import ApproveUserByCivilID
from BookaCall import BookaCall
from ConfigureDevices import ConfigureDeviceEmulator
from EmailCount import EmailCountAPI_SingleUser_ReturnFullEmail
from GetTokenAPI import GetTokenAPI
from HTMLFunctions import GenerateReport
from ManualReport import ReportResultsUserSmokeTest, ReportUserFinalResults
from PendingDashboard import PendingDashboard
from PerformInitialDepositFlow import InitialDepositFlow
from SaveJSONFile import SaveJSONFile
from SendEmail import SendEmail
from SendSlack import slack_frontend
from SignContractAPI import SignContractAPI
from SignUpFlow import SignUpFlow
from TestRailReporting import TestRailReportFail, TestRailReportSuccess
from UploadIDs import UploadIDusingAPI_SmokeTest
from VerifyEmail import VerifyEmailusingAPI
from WithdrawalFlow import WithdrawalFlow
from KYC import KYC_FillAll

def Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow):
    video_rawdata=driver.stop_recording_screen()
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess%s_%s_%s(KYC).mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
            vd.write(base64.b64decode(video_rawdata))
    
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)
    SaveJSONFile("TechnicalVariables,progress",100)

    TestDone=True
    if TestDone==True:
        ReportUserFinalResults(ReportDriver,TestDone,User_Type,RiskScore,OnboardingFlow)
        if JSON["TestRailSmokeTests"]["Status"].lower() == "enabled":
            TestRail=True
        else : TestRail=False

        if TestRail:
            TestRailReportSuccess("N/A")
        
    GenerateReport()
    AnalyzeFinalResults(True)
    sys.exit()
    


def FullUserTest(ReportDriver,Credentials,AdminAuthorization=None):
    #User_Type: ETF or Islamic
    #RiskScore: User's risk score
    #Onboarding Type: Customized or Predefined
    slack=slack_frontend()
    SaveJSONFile("TechnicalVariables,progress",1)



    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)
        
    Credentials["Email"]=JSON["SingleUserDetails"]["Email"].lower()
    RiskScore=JSON["SingleUserDetails"]["RiskScore"].lower()
    OnboardingFlow=JSON["SingleUserDetails"]["OnboardingFlow"].lower()
    InitialDepositMethod=JSON["SingleUserDetails"]["InitialDepositMethod"]
    User_Type=JSON["SingleUserDetails"]["User_Type"].lower()
    StopFlag=JSON["SingleUserDetails"]["StopFlag"].lower()
    print(len(Credentials["Email"]))
    
    Credentials["Email"]=EmailCountAPI_SingleUser_ReturnFullEmail(None,Credentials["Email"])
    ReportResultsUserSmokeTest(ReportDriver,True,User_Type,RiskScore,OnboardingFlow)
    for i in range(4,10):
        SaveJSONFile("TechnicalVariables,progress",i)
        sleep(0.3)
   
    
    try:
        count=0
        while count<=7:
            try:
                driver=ConfigureDeviceEmulator(ReportDriver,Credentials)
                break
            except:
                sleep(2)
                count=count+1
                
        for i in range(10,20):
            SaveJSONFile("TechnicalVariables,progress",i)
        driver.start_recording_screen()
        Credentials=SignUpFlow(driver,ReportDriver,Credentials,JSON,User_Type,RiskScore,OnboardingFlow)
        if "verify email" in StopFlag.lower():
            
            Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)
        # Authorization=GetTokenAPI(Credentials["Email"])
        Authorization=GetTokenAPI(Credentials["Email"])
        VerifyEmailusingAPI(driver,ReportDriver,Credentials["Email"],Credentials["Password"],Authorization)
        if "upload id" in StopFlag.lower() or "upload ids" in StopFlag.lower():
            
            Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)

        User_ID=UploadIDusingAPI_SmokeTest(driver,ReportDriver,Credentials,Authorization)
        for i in range(20,30):
            SaveJSONFile("TechnicalVariables,progress",i)
        video_rawdata=driver.stop_recording_screen()
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess%s_%s_%s(SignUp_VerifyEmail_UploadID).mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
                vd.write(base64.b64decode(video_rawdata))
        
        while True:
            try:
                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/signedUpTv")
                break
            except:
                try:
                    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
                    break
                except:
                    #Still loading
                    F=None
        

        # Step 1: Upload IDs 
        # PendingDashboard(driver,ReportDriver)
        # UploadIDSmokeTests(driver,ReportDriver)


                
        # Step 2: Fill KYC + Sign Contract + Approve User from Admin using API collection 
        PendingDashboard(driver,ReportDriver)
        driver.start_recording_screen()        
        KYC_FillAll(driver,ReportDriver,JSON)
        video_rawdata=driver.stop_recording_screen()
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess%s_%s_%s(KYC).mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
                vd.write(base64.b64decode(video_rawdata))
        driver.start_recording_screen()        

        for i in range(30,40):
            SaveJSONFile("TechnicalVariables,progress",i)


        if "contract not signed" in StopFlag.lower():
            
            Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)

        # SignContract(driver,ReportDriver)
        BookaCall(driver,ReportDriver,False,True)            
        SignContractAPI(driver, ReportDriver,User_ID)
        for i in range(40,50):
            SaveJSONFile("TechnicalVariables,progress",i)

        if "contract signed" in StopFlag.lower() or "not approved" in StopFlag.lower() :            
            Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)
            
        ApproveUserByCivilID(driver,ReportDriver,Credentials)
        for i in range(50,60):
            SaveJSONFile("TechnicalVariables,progress",i)
            
        video_rawdata=driver.stop_recording_screen()
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess%s_%s_%s(Sign Contract and approve).mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
                vd.write(base64.b64decode(video_rawdata))
        driver.start_recording_screen()   
        
        if "initial deposit" in StopFlag.lower():
            
            Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)

        # Step 3: Initial Deposit flow + Activation 
        PendingDashboard(driver,ReportDriver)
        InitialDepositFlow(driver,ReportDriver,User_ID,InitialDepositMethod,User_Type)
        for i in range(60,70):
            SaveJSONFile("TechnicalVariables,progress",i)

        ActivateUser(ReportDriver,driver,User_ID)
        video_rawdata=driver.stop_recording_screen()
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess%s_%s_%s(Activate).mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
                vd.write(base64.b64decode(video_rawdata))
        driver.start_recording_screen()   


            
                

        if "active user" in StopFlag.lower() and not "deposit" in StopFlag.lower() and not "withdraw" in StopFlag.lower():
            Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)

        AddFundsFlow(driver,ReportDriver,"bank transfer",User_Type)
        if "active user" in StopFlag.lower() and "deposit" in StopFlag.lower() and not "withdraw" in StopFlag.lower():
            Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)
        for i in range(70,80):
            SaveJSONFile("TechnicalVariables,progress",i)

        WithdrawalFlow(driver,ReportDriver,"Partial",User_ID,1000)
        if "active user" in StopFlag.lower() and not "deposit" in StopFlag.lower() and "partial withdrawal" in StopFlag.lower():
            Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)
        for i in range(80,90):
            SaveJSONFile("TechnicalVariables,progress",i)

        WithdrawalFlow(driver,ReportDriver,"Full",User_ID,1000)
        if "active user" in StopFlag.lower() and not "deposit" in StopFlag.lower() and "partial withdrawal" in StopFlag.lower():
            Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)
        for i in range(90,98):
            SaveJSONFile("TechnicalVariables,progress",i)
        
        video_rawdata=driver.stop_recording_screen()
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess%s_%s_%s(Additional deposit and withdrawal).mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
                vd.write(base64.b64decode(video_rawdata))

        TestDone=True
        if TestDone==True:
            ReportUserFinalResults(ReportDriver,TestDone,User_Type,RiskScore,OnboardingFlow)
            if JSON["TestRailSmokeTests"]["Status"].lower() == "enabled":
                TestRail=True
            else : TestRail=False

            if TestRail:
                TestRailReportSuccess("N/A")

    except Exception as e:
        
        TestDone=False
        print(e)
        traceback.print_exc()
        Error=traceback.format_exc()
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
        # Load its content and make a new dictionary
            JSON=json.load(file)

        ReportUserFinalResults(ReportDriver,TestDone,User_Type,RiskScore,OnboardingFlow)
        if JSON["TestRailSmokeTests"]["Status"].lower() == "enabled":
            TestRail=True
        else : TestRail=False

        if TestRail:
            TestRailReportFail("N/A",str(e)+"\n"+str(Error))

        video_rawdata=driver.stop_recording_screen()

        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\ErrorVideoforSmokeTest%s_%s_%s.mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
                vd.write(base64.b64decode(video_rawdata))
        
        SendEmail(False,Credentials["Email"],User_Type, RiskScore,OnboardingFlow,Credentials["Email"])
        slack.send_results(False,Credentials["Email"],User_Type, RiskScore,OnboardingFlow,Credentials["Email"])
        print("ERROR!!! Code Has Failed!!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
        sleep(2)
        print("Error Message: ",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
        print("Error in test check video!")

    return TestDone
            
    