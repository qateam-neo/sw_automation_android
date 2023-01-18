from time import sleep
from unittest import TestCase
from colorama import Fore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ManualReport import ReportResults



def IBANScreen(driver,ReportDriver):
    Status=True
    TestCase="Enter IBAN Screen"
    IBAN="ibanibanibaniban"
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/layoutBank")))
        IBANField=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/etIBAN")
        
        IBANField.send_keys(IBAN)
        sleep(2)    
        
        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnContinueFunding").click()
    except:
        print (Fore.YELLOW+"IBAN Screen not Shown"+Fore.RESET)
    
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)