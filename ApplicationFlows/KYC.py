import base64
import json
import os
import sys
from time import sleep
from colorama import Fore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from AnalyzeFinalResults_SendEmail import AnalyzeFinalResults

from BlueScreens import AlmostThere_Blue, PersonalInfo_Blue
from CheckIfPageLoading import CheckIfPageLoading
from GesturesAndMotions import scrollDown
from HTMLFunctions import GenerateReport
from Intensive_Tests.helpers import Random_values
from KYCFillers import ChooseBirthDate, ChooseExpiryDate, ClickonCheckbox, SelectLocation
from ManualReport import ReportResults, ReportUserFinalResults
from TestRailReporting import TestRailReportSuccess


def Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow):
    video_rawdata=driver.stop_recording_screen()
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording\\SmokeTestSuccess%s_%s_%s(KYC).mp4" % (User_Type, RiskScore,OnboardingFlow),"wb+") as vd:
            vd.write(base64.b64decode(video_rawdata))
    
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)

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
    


def KYC_FillAll(driver,ReportDriver,JSON,Notes="N/A"):
    StopFlag=JSON["SingleUserDetails"]["StopFlag"].lower()
    RiskScore=JSON["SingleUserDetails"]["RiskScore"].lower()
    OnboardingFlow=JSON["SingleUserDetails"]["OnboardingFlow"].lower()
    User_Type=JSON["SingleUserDetails"]["User_Type"].lower()
    
    a_file = open(os.getcwd()+"/BaseClasses/KYC_3.0_JSON_File.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    # print(json_object)

    json_object["KYC_3.0"]["PersonalInfo_Fields"]["CivilID"] = str(Random_values().generate_numeric_value.with_length(12))

    a_file = open(os.getcwd()+"/BaseClasses/KYC_3.0_JSON_File.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
    
    with open(os.getcwd()+"/BaseClasses/KYC_3.0_JSON_File.json") as file:
# Load its content and make a new dictionary
        JSON=json.load(file)

    if "kyc" in StopFlag.lower() and "personal" in StopFlag.lower() :
    
        Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)
    KYC_PersonalInfo(driver,ReportDriver,JSON)
    
    if "kyc" in StopFlag.lower() and "address" in StopFlag.lower() :
    
        Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)
    KYC_AddressInfo(driver,ReportDriver,JSON)
    
    if "kyc" in StopFlag.lower() and "employment" in StopFlag.lower() :
        
        Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)
    KYC_Employment(driver,ReportDriver,JSON)
    
    if "kyc" in StopFlag.lower() and "income" in StopFlag.lower() or "wealth" in StopFlag.lower():
        
        Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)
    KYC_IncomeAndWealth(driver,ReportDriver,JSON, Notes)
    
    if "kyc" in StopFlag.lower() and "additional info" in StopFlag.lower():
        
        Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)
    KYC_AdditionalInfo(driver,ReportDriver,JSON)
    
    if "kyc" in StopFlag.lower() and "classification" in StopFlag.lower() :
        
        Exit(driver,ReportDriver,User_Type,RiskScore,OnboardingFlow)
    KYC_ConfirmClassification(driver,ReportDriver,JSON)

def KYC_PersonalInfo(driver,ReportDriver,PersonalInfo_Json):
    
    
    TestCase="Personal Info KYC 3.0"

    CheckIfPageLoading(driver)
    # print("Going to personal info blue",end="\r")
    PersonalInfo_Blue(driver,ReportDriver)
    # print("After personal info blue",end="\r")
    CheckIfPageLoading(driver)

    WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))
    Fields=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")

    ClickonCheckbox(driver,"Gender",(PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["Gender"]),"N/A")


    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))
    Fields=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")
    
    
    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))      
    Fields=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")   
    if Fields[1].text=="First Name" and Inputs[0].text!=PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["FirstName"]:

        Inputs[0].send_keys(PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["FirstName"])
        sleep(1.5)

    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))      
    Fields=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")   
    if Fields[2].text=="Middle Name" and Inputs[1].text!=PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["MiddleName"]:

        Inputs[1].send_keys(PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["MiddleName"])
        sleep(1.5)


    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))      
    Fields=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")   
    if Fields[3].text=="Family Name" and Inputs[2].text!=PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["LastName"]:
        Inputs[2].send_keys(PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["LastName"])
        sleep(1.5)


    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))      
    Fields=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")   
    if Fields[4].text=="Birth Date":
        x=Fields[4].text
        Fields[4].click()
        ChooseBirthDate(driver, x ,PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["Date_of_Birth"])   
        sleep(1.5)


    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))      
    Fields=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")  
     
    if Fields[5].text=="Nationality" and Inputs[4].text!=PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["Nationality"]:
        
        x=Fields[5].text
        Fields[5].click()
        SelectLocation(driver,x,PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["Nationality"])
        sleep(1.5)

    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))      
    Fields=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")   
    
    if Fields[6].text=="Country of Birth" and Inputs[5].text!=PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["Country_of_birth"]:
        x=Fields[6].text
        Fields[6].click()
        SelectLocation(driver,x,PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["Country_of_birth"])
        # scrollDown(driver,500, 1000, 500, 700)
        # sleep(1)
        sleep(1.5)
       
    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))
    Fields=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")
    
    if Fields[7].text=="Civil ID No." and Inputs[6].text!=PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["CivilID"]:
        Inputs[6].send_keys(PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["CivilID"])
        sleep(1.5)

    
    scrollDown(driver,500, 2200, 500, 700)
    sleep(1)
    Fields=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")   
    
    if Fields[len(Fields)-2].text=="Civil ID Serial No." and Inputs[len(Inputs)-2].text!=PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["CivilIDSerial"]:
        Inputs[len(Inputs)-2].send_keys(PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["CivilIDSerial"]) 
        sleep(1.5)


           
    if Fields[len(Fields)-1].text=="Civil ID Expiry Date":
        x=Fields[len(Fields)-1].text
        Fields[len(Fields)-1].click()
        ChooseExpiryDate(driver, x ,PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]["CivilIDExpiryDate"])
        sleep(1.5)

    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton").click()
    # else:
    #     print("Still missing field"+Fields[i].text)  
    
    JSON=PersonalInfo_Json["KYC_3.0"]["PersonalInfo_Fields"]
    intCivilIDNew=int(JSON["CivilID"])

    CivilIDNew=False
    atext=""
    x=intCivilIDNew
    while CivilIDNew==False and atext!="Enter civil ID No.":
        count=1
        while True:
            try:
                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_text_title")
                CivilIDNew=False
                break
            except:
                try:
                    AA=driver.find_elements(By.CLASS_NAME,"android.widget.TextView")
                    for A in AA:
                        if "Address" in A.text:
                            CivilIDNew=True 
                            print(Fore.GREEN+"\tCivil ID %s Worked!"%x+Fore.RESET)
                            print("\tCivil ID %s Worked!"%x,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
                            break
                    if CivilIDNew==True:
                        break 
                except: 
                    print("Waiting for Input (%s)"%count,end="\r")
                    sleep(0.5)
            
            count=count+1    
            
        
            
        if CivilIDNew==False:
            print (Fore.RED+"\tExisting Civil ID: %s, trying another..."%x+Fore.RESET)
            print ("\tExisting Civil ID: %s, trying another..."%x,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            
            if ReportDriver==None: print("No Report Driver found")
            else: ReportDriver.report().step(description="Existing CivilID number", message="Trying another number", passed=False,screenshot=False,inputs={"CivilID Old":intCivilIDNew})
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_button_positive").click()
            intCivilIDNew=intCivilIDNew+1
            x=intCivilIDNew
            
            a=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")
            a[len(a)-3].clear()
            sleep(2)
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/etValue")))
            a=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")
            a[len(a)-3].click()
            sleep(0.5)
            action = ActionChains(driver)
            action.send_keys(x).perform()
            driver.press_keycode(4)
            # a[len(a)-3].send_keys(x)..........................................................
            # atext=a[len(a)-3].text
            # driver.press_keycode(4)
            sleep(2)
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton").click()
            
    a_file = open(os.getcwd()+"/BaseClasses/KYC_3.0_JSON_File.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    # print(json_object)

    json_object["KYC_3.0"]["PersonalInfo_Fields"]["CivilID"] = str(intCivilIDNew)

    a_file = open(os.getcwd()+"/BaseClasses/KYC_3.0_JSON_File.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
            
    
    ReportResults(ReportDriver, driver, True,TestCase,"N/A",  "N/A")
    
def KYC_AddressInfo(driver,ReportDriver,AddressInfo_JSON):
    
    TestCase="Address Info KYC 3.0"
    
    CheckIfPageLoading(driver)
    WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.TextView")))
    AA=driver.find_elements(By.CLASS_NAME,"android.widget.TextView")
    Flag=False
    for A in AA:
        if A.text == "Address":
            try:
                WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))
                Flag=False
                break
            except:
                Flag=True
    if Flag==True:
        driver.press_keycode(4)
        scrollDown(driver,500, 2200, 500, 700)
        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton").click()


    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))
    Titles= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")
    
    if Titles[1].text=="City" and Inputs[1].text!=AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["City"]:
        
        x=Titles[1].text
        Titles[1].click()
        SelectLocation(driver,x,AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["City"])
    
    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))
    Titles= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")
      
    if Titles[2].text=="Area" and Inputs[2].text!=AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["Area"]:
        
        x=Titles[2].text
        Titles[2].click()
        SelectLocation(driver,x,AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["Area"])

    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))
    Titles= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")

                
    if Titles[3].text=="Block"and Inputs[3].text!=AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["Block"]:
        Inputs[3].send_keys(AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["Block"])
        sleep(1)
        
    if Titles[4].text=="Street"and Inputs[4].text!=AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["Street"]:

        Inputs[4].send_keys(AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["Street"])
        sleep(1)

    
    if Titles[5].text=="House"and Inputs[5].text!=AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["House"]:
        

        Inputs[5].send_keys(AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["House"])
        sleep(1)

    if Titles[6].text=="Mobile number"and Inputs[6].text!=AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["Mobile number"]:
 
        Inputs[6].send_keys(AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["Mobile number"])
        sleep(2)
    
    MobileNew=False

        
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton").click()
    # else:
    #     print("Still missing field"+Fields[i].text)  
    intMobileNew=AddressInfo_JSON["KYC_3.0"]["AddressInfo_Fields"]["Mobile number"]
    while MobileNew==False:
        try:
            WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/md_text_title")))
            MobileNew=False
            if ReportDriver==None: print("No Report Driver found")
            else:ReportDriver.report().step(description="Existing mobile number", message="Trying another number", passed=False,screenshot=False,inputs={"Mobile Old":intMobileNew})
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_button_positive").click()
            intMobileNew=int(intMobileNew)+1
            Inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etValue")

            Inputs[6].clear
            Inputs[6].send_keys(intMobileNew)
            sleep(2)
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton").click()
        except:
            try:
                MobileNew=True
                a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
                json_object = json.load(a_file)
                a_file.close()
                # print(json_object)

                json_object["KYC_3.0"]["AddressInfo_Fields"]["Mobile number"] = str(intMobileNew+2)

                a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
                json.dump(json_object, a_file)
                a_file.close()
            except:
                sleep(0.1)
    
        
    ReportResults(ReportDriver, driver, True,TestCase,"N/A",  "N/A")
    
def KYC_Employment(driver,ReportDriver,Employment_JSON):
    
    TestCase="Employment KYC 3.0"

    CheckIfPageLoading(driver)
    AlmostThere_Blue(driver,ReportDriver)
    CheckIfPageLoading(driver)

    WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/dropdown")))
    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
    
    Titles1= parentElement[0].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs1=parentElement[0].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
    
    Titles2= parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    Inputs2=parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
    
    ClickonCheckbox(driver,"Employment status",(Employment_JSON["KYC_3.0"]["Employment_Fields"]["EmploymentStatus"]),Inputs1)
    ClickonCheckbox(driver,"BoardMember",(Employment_JSON["KYC_3.0"]["Employment_Fields"]["BoardMember"]),Inputs2)
    
    SubmitButton=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton")
    SubmitButton.click()
    
    ReportResults(ReportDriver, driver, True,TestCase,"N/A",  "N/A")
    
    
def KYC_IncomeAndWealth(driver,ReportDriver,IncomeAndWealth_JSON,Notes="N/A"):
    
    TestCase="Income and wealth KYC 3.0"

    CheckIfPageLoading(driver)
    WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/dropdown")))
    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
    
    ReasonForInvesting= parentElement[0].find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    # print(ReasonForInvesting.text)

    if ReasonForInvesting.text=="Trading experience": #We are on customized flow.
        
        TradingExperience= parentElement[0].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        Inputs2=parentElement[0].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
        
        SourceOfIincome= parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        Inputs3=parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
        
        AnnualIncome= parentElement[2].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        Inputs4=parentElement[2].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
        
        # ClickonCheckbox(driver,"Reason For Investing",(IncomeAndWealth_JSON["KYC_3.0"]["IncomeAndWealth_Fields"]["ReasonForInvesting"]),Inputs1)
        ClickonCheckbox(driver,"TradingExperience",(IncomeAndWealth_JSON["KYC_3.0"]["IncomeAndWealth_Fields"]["TradingExperience"]),Inputs2)
        ClickonCheckbox(driver,"Source_Of_Income",(IncomeAndWealth_JSON["KYC_3.0"]["IncomeAndWealth_Fields"]["SourceOfIncome"]),Inputs3)
        ClickonCheckbox(driver,"AnnualIncome",(IncomeAndWealth_JSON["KYC_3.0"]["IncomeAndWealth_Fields"]["AnnualIncome"]),Inputs4)
        scrollDown(driver,500, 2500, 500, 500)
        scrollDown(driver,500, 2500, 500, 500)
        sleep(1)
        Inputs1=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
        for ELEM in Inputs1:
            if ELEM.text=="Not applicable":
                ELEM.click()
    
        # ReasonForInvesting= driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")


        
    else: #Predefined flow

        Inputs1=parentElement[0].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")

        TradingExperience= parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        Inputs2=parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")

        SourceOfIincome= parentElement[2].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        Inputs3=parentElement[2].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")

        AnnualIncome= parentElement[3].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        Inputs4=parentElement[3].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")

        ClickonCheckbox(driver,"Reason For Investing",(IncomeAndWealth_JSON["KYC_3.0"]["IncomeAndWealth_Fields"]["ReasonForInvesting"]),Inputs1)
        ClickonCheckbox(driver,"TradingExperience",(IncomeAndWealth_JSON["KYC_3.0"]["IncomeAndWealth_Fields"]["TradingExperience"]),Inputs2)
        ClickonCheckbox(driver,"Source_Of_Income",(IncomeAndWealth_JSON["KYC_3.0"]["IncomeAndWealth_Fields"]["SourceOfIncome"]),Inputs2)
        ClickonCheckbox(driver,"AnnualIncome",(IncomeAndWealth_JSON["KYC_3.0"]["IncomeAndWealth_Fields"]["AnnualIncome"]),Inputs4)

        scrollDown(driver,500, 2650, 500, 340)
        sleep(0.2)
        BB=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
        for B in BB:
            if B.text=="KD 15,000 to KD 100,000" or B.text=="Above KD 1,500,000":
                B.click()
                break
        scrollDown(driver,500, 2500, 500, 500)
        sleep(1)
        Inputs1=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
        for ELEM in Inputs1:
            if ELEM.text=="Not applicable":
                ELEM.click()


    
    parentElement=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/customText")
    BankName= parentElement.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    BankName.click()
    SelectLocation(driver,"Bank Name",IncomeAndWealth_JSON["KYC_3.0"]["IncomeAndWealth_Fields"]["BankName"])    
    # ClickonCheckbox(driver,"Total Value",(IncomeAndWealth_JSON["KYC_3.0"]["IncomeAndWealth_Fields"]["Total_Value"]),Inputs5)
    # ClickonCheckbox(driver,"ValueOfAssets",(IncomeAndWealth_JSON["KYC_3.0"]["IncomeAndWealth_Fields"]["ValueOfAssets"]),Inputs4)

    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/submitButton"))).click()
    sleep(1)

    # SubmitButton=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btn")
    # SubmitButton.click()
    
    ReportResults(ReportDriver, driver, True,TestCase,"N/A",  "N/A")
    
def KYC_AdditionalInfo(driver,ReportDriver,AdditionalInfo_JSON):
    TestCase = "Additional Information KYC 3.0"
    
    CheckIfPageLoading(driver)
    # Inputs1=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
    # Inputs1[3].click()
    WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/submitButton"))).click()
    ReportResults(ReportDriver, driver, True,TestCase,"N/A",  "N/A")


def KYC_ConfirmClassification(driver,ReportDriver,ConfirmClassification_JSON):
    # try:
    TestCase = "Confirm Classification KYC 3.0"
    
    CheckIfPageLoading(driver)
    try:
        Retail=WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/btnConfirm"))).click()
    except:
        print(Fore.RED+"Confirm Classification Screen is not shown."+Fore.RESET)
    
    ReportResults(ReportDriver, driver, True,TestCase,"N/A",  "N/A")

    # except:
    #     Retail=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnConfirm")
    #     OneOption=True

        
    # Retail=ConfirmClassification_JSON["KYC_3.0"]["ConfirmClassification"]["Retail"]
    # Qualified=ConfirmClassification_JSON["KYC_3.0"]["ConfirmClassification"]["Qualified"]
    
    # if OneOption=True:

    
    # if Retail==Qualified:
    #     print("Issue in JSON file in Field: ConfirmClassification // Qualified and Retail are either both True or both False.")
        
    # if Qualified:
    #     driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnConfirm").click()
    # elif Retail:
    #     Retail.click()
        