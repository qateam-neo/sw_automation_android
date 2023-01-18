
from colorama import Fore
from ManualReport import ReportResults
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def PendingDashboard(driver,ReportDriver):
    
    InputsDone = [False,False,False]
    Status=True
    # Title1=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvBannerTitle")))
    # Description1=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvBannerDesc")
    
    # Title1Expected1="Get full access.."
    # Description1Expected="We need a few more info to finish setting up your account. Continue now to start investing on auto-pilot."
    
    # if Title1 !=Title1Expected1:
    #         Status=False
    #         ReportResults(ReportDriver, driver, Status,TestCase,Title1.text,Title1Expected1)
            
    # if Description1 != Description1Expected:
    #         Status=False
    #         ReportResults(ReportDriver, driver, Status,TestCase,Description1.text,Description1Expected)
            
                
    WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))

    Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
    ApproxTime=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTime")
    Descriptions=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvDescription")
    
    if len(ApproxTime) == 3:
        TestCase="Pending Dashboard on Upload ID Step"
        # TitlesExpected=["Verify your ID","Complete your information","Fund your account"]
        # TimeExpected=["Approximately 2mins","Approximately 5 mins","Approximately 2mins"]
        # DescriptionExpected=["Your Civil ID will be scanned and automatically verified","Enter your personal information and sign your client agreements","Deposit funds into your account to start your smart investment journey."]
        
        # for i in range(0, len(Titles)):

        #     if ( (Titles[i].text) != TitlesExpected[i] ):
        #         Status=False
        #         ReportResults(ReportDriver, driver, Status,TestCase,Titles[i].text,TitlesExpected[i])
                
        #     if ( (Descriptions[i].text) != DescriptionExpected[i] ):
        #         Status=False
        #         ReportResults(ReportDriver, driver, Status,TestCase, Descriptions[i].text , DescriptionExpected[i])
        
        # for i in range(0, len(ApproxTime)):
        #     if ( (ApproxTime[i].text) != TimeExpected[i] ):
        #         Status=False
        #         ReportResults(ReportDriver, driver, Status,TestCase, ApproxTime[i].text , TimeExpected[i])
        InputsDone = [False,False,False]
        Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        Titles[0].click() # Go to permission screen or upload ID
    
    elif len(ApproxTime) == 2: 
        TestCase="Pending Dashboard on KYC Step"
        # print("ID already uploaded") 
        ReportResults(ReportDriver, driver, Status, TestCase,"ID is already uploaded","N/A")
        InputsDone = [True,False,False]
        Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        Titles[1].click() # Go to KYC
    
    elif len(ApproxTime) == 1:
        TestCase="Pending Dashboard on Initial Deposit"
        # print("User is pending Initial deposit") 
        InputsDone = [True,True,False]
        try:
            Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
            Titles[2].click() # Go to initial deposit
            # print("Going to Initial Deposit Flow: ") 
        except:
            print(Fore.RED+"\tCan't Click Element!!!"+Fore.RESET)
        # if UserApproved == False:
            
        # else:
        #     UserApproved.click() # Go to Initial Deposit

        
    return InputsDone