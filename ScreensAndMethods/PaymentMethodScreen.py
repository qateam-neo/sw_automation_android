from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CheckFeatureFlags import FeatureFlag

from ManualReport import ReportResults



def PaymentMethodScreen(driver,ReportDriver,Paymentmethod):
    Status=True
    TestCase="Payment Method Screen"
    try:
        WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/card")))
        PaymentOptions=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/card")
        Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/labelTitle")
        FeatureAvailable=True
    except:FeatureAvailable=FeatureFlag(driver,"deposit")
    if FeatureAvailable:
        if len(PaymentOptions) == 1:
            TestCase= "Choose Deposit option (Bank Transfer payment Method only)"     
            if Titles[0].text == Paymentmethod:
                PaymentOptions[0].click()
                sleep(1)
            else:
                print("Error Payment  is not available")
                Status=False
        elif len(PaymentOptions) == 2:
            TestCase= "Choose Deposit option (2 payment Methods)"     
            if "knet" in Paymentmethod.lower():
                PaymentOptions[0].click()
                
            elif Paymentmethod.lower() == "bank transfer" or Paymentmethod.lower() == "banktransfer":
                PaymentOptions[1].click()
            else:
                print("Error Payment option is not ")    
                Status=False
        
        
        while True:
            try:
                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnContinue").click()
                break
            except:
                print("Not clicked can't find the element")
        if ReportDriver==None:
            print("No Report Driver found")
        elif Status:
            ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
        else:
            ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
    