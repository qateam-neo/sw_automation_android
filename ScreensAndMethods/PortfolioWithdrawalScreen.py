
from ManualReport import ReportResults
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def Portfoliowithdrawal(driver,ReportDriver):
    Status=True
    TestCase="Portfolio Withdrawal screen"
    WithdrawalScreenShown=False
    while WithdrawalScreenShown==False:
        try:
            WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/reasonTextView")))
            Portfolio=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/reasonTextView")
            Portfolio[0].click()
            WithdrawalScreenShown=True
        except:
            driver.press_keycode(4)
            
            try:WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/title")))
            except: 
                driver.press_keycode(4)
                WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,"Neo.nbkc.smartwealth.demo:id/title")))
            Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/title")
            for ELEM in Titles:
                if ELEM.text=="Withdrawals":
                    ELEM.click()
                    WithdrawalScreenShown = False
                    break
    
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)