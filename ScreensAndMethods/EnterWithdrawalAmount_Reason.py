
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CheckIfPageLoading import CheckIfPageLoading

from ManualReport import ReportResults

def EnterWithdrawalAmount_Reason(driver,ReportDriver,WithdrawalType,Amount=1000):
    
    CheckIfPageLoading(driver)
    Status=True
    TestCase="Enter Withdrawal Amount and Reason"
    if WithdrawalType=="Partial" or WithdrawalType=="Partial Withdrawal" or WithdrawalType == "partial" :
    
        AmountField=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/etInput")))
        AmountField.click()
        AmountField.send_keys(Amount)
    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/pickerWithdrawalReason")))
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/pickerWithdrawalReason").click()
    
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "android:id/text1")))
    Options= driver.find_elements(By.ID,"android:id/text1")
    Options[2].click()
    
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnOk").click()
    
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/btnSubmit")))
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnSubmit").click()
    
    
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)