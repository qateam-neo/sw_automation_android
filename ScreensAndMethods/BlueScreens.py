from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ManualReport import ReportResults, ReportResultsScreenNotShown


def PersonalInfo_Blue(driver,ReportDriver):
    
    TestCase="Personal Info Blue Screen"
    Status=True
    # Title=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tv_title"))).text
    # Info=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tv_info").
    try:
        StartButton=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/btn")))
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
        StartButton.click()
    except:
        ReportResultsScreenNotShown(ReportDriver,TestCase)
        
        
    # TitleExpected="Personal info"
    # InfoExpected="Please enter your personal details and address information in the following screens to start creating your investment profile."
    # ButtonExpected="Start"
    
    # if Title != TitleExpected:
    #     Status=False
    #     ReportResults(ReportDriver,driver,Status,TestCase,Title,TitleExpected)
        
    # if Info != InfoExpected:
    #     Status=False
    #     ReportResults(ReportDriver,driver,Status,TestCase,Info,InfoExpected)
    
    # if StartButton.text != ButtonExpected:
    #     Status =False
    #     ReportResults(ReportDriver,driver,Status,TestCase,StartButton.text,ButtonExpected)
        
    # if Status==True:


def AlmostThere_Blue(driver,ReportDriver):
    
    TestCase="Almost There Blue Screen"
    Status=True
    # Title=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tv_title"))).text
    # Info=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tv_info").text
    
    # TitleExpected="Almost there..."
    # InfoExpected="We need a few more details regarding your employment and financials so we can complete setting up your profile."
    # ButtonExpected="Continue"
    
    # if Title != TitleExpected:
    #     Status=False
    #     ReportResults(ReportDriver,driver,Status,TestCase,Title,TitleExpected)
        
    # if Info != InfoExpected:
    #     Status=False
    #     ReportResults(ReportDriver,driver,Status,TestCase,Info,InfoExpected)
        
    # if ContinueButton.text != ButtonExpected:
    #     Status =False
    #     ReportResults(ReportDriver,driver,Status,TestCase,ContinueButton.text,ButtonExpected)
        
    try:
        StartButton=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/btn")))
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
        StartButton.click()
    except:
        ReportResultsScreenNotShown(ReportDriver,TestCase)     

def Signyourcontract_Blue(driver,ReportDriver):
    
    TestCase="Sign your contract blue Screen"
    Status=True
    # Title=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tv_title"))).text
    # Info=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tv_info").text
    try:
        Button=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/btn")))
        Screen_Shown=True        
    except:
        print("Sign you Contract Blue screen is not shown")
        Screen_Shown=False
    
    if Screen_Shown:
        Button.click()
            
        if ReportDriver==None:
            print("No Report Driver found")
        elif Status:
            ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
        else:
            ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
    
    else:
        ReportResultsScreenNotShown(ReportDriver,TestCase)

    
