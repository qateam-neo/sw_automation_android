
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CheckIfPageLoading import CheckIfPageLoading

from ManualReport import ReportResults

def WithdrawalThankYou(driver,ReportDriver):
    CheckIfPageLoading(driver)
    # try:
    #     A=WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/title"))).text
    #     if "api" in A or "depricated" in A:
    #         driver.press_keycode(4)
    # except:
    #     print("API Depricated is not shown")
    #     APIDep=False
    
    TestCase="Withdrawal Thank You"
    Status=True
    
    Button=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/closeButton")))
    Button.click()
    
    
    if ReportDriver==None:
            print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)