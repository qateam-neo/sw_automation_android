from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ManualReport import ReportResults

def EIDFallBackScreen(driver,ReportDriver):
    
    TestCase="EID FallBack Screen"
    Status=True
    Title =WebDriverWait(driver, 16).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/titleTextView")))
    # Description=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/descriptionTextView")
    
    # TitleExpected="Please upload a copy of the front and back of your Civil ID"
    # DescriptionExpected="In case your Civil ID is expired or soon to be, please upload a copy of your Digital Civil ID as well."
    
    # if Title !=TitleExpected:
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase,Title.text,TitleExpected)
            
    # if Description != DescriptionExpected:
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase,Title.text,DescriptionExpected)
    
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status== True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
        
        
