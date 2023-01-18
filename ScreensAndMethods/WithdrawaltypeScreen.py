
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ManualReport import ReportResults


def WithdrawalTypeScreen(driver,ReportDriver,WithdrawalType):
    Status=True
    TestCase="Withdrawal Type Screen"
    WebDriverWait(driver,25).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/labelTitle")))
    Options=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/labelTitle")
    if WithdrawalType=="Full" or WithdrawalType=="Full Withdrawal" or WithdrawalType == "full" :
        Options[0].click()
    
    elif WithdrawalType=="Partial" or WithdrawalType=="Partial Withdrawal" or WithdrawalType == "partial" :
        Options[1].click()
        
    else:
        Options[1].click() #By default
        print("Wrong Withdrawal Type")
    
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnContinue").click()
      
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)