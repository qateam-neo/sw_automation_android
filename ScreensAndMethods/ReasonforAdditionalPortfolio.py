from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ManualReport import ReportResults

def ReasonforAdditionalPortfolio(driver,ReportDriver):
    TestCase ="Reason for Additional Portfolio"
    Status = True
    
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/tvGoal")))
    PortfolioName=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvGoal")
    PortfolioName[1].click()
    
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"neo.nbkc.smartwealth.demo:id/btnContinue"))).click()
    
    
    
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
    
    
    

