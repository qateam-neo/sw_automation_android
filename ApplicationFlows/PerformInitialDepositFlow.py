from CheckIfPageLoading import CheckIfPageLoading
from EnterDepositAmount import EnterDepositAmountScreen
from IBANScreen import IBANScreen
from KNETScreen import KNETScreen
from ManualReport import ReportResults
from PaymentMethodScreen import PaymentMethodScreen
from PendingDashboard import PendingDashboard
from TransferInstructionsScreen import TransferInstructionsScreen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from colorama import Fore

def InitialDepositFlow(driver,ReportDriver,User_ID,PaymentMethod,UserType):
    Passed=True
    CheckIfPageLoading(driver)

    try:IBANScreen(driver,ReportDriver)
    except:print("IBAN Not shown")
    PaymentMethodScreen(driver,ReportDriver,PaymentMethod)

    if "bank transfer" in PaymentMethod.lower() or "banktransfer" in PaymentMethod.lower() or "bt" in PaymentMethod.lower():
        try:
            IBANScreen(driver,ReportDriver)
        except:
            print("IBAN already done!")
        CheckIfPageLoading(driver)
        EnterDepositAmountScreen(driver,ReportDriver)
        CheckIfPageLoading(driver)
        TransferInstructionsScreen(driver,ReportDriver)
    elif PaymentMethod.lower() =="knet":
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btnContinue"))).click()
        CheckIfPageLoading(driver)
        try:
            EnterDepositAmountScreen(driver,ReportDriver)
            if (KNETScreen(driver,ReportDriver))==False:
                ReportResults(None,driver,False,"Initial Deposit Flow","KNET is not working","User should be able to deposit normally using KNET","Check UDF3 abd UDF4")
                raise ValueError("KNET is not available")
        except:
            Passed=False
            while True:
                try:
                    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvTime")
                    break
                except:
                    try:
                        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnBack").click()
                    except:
                        driver.press_keycode(4)
                        print("Searching for trigger screen to deposit using bank transfer")
            CheckIfPageLoading(driver)

            try:IBANScreen(driver,ReportDriver)
            except:print("IBAN Not shown")
            PendingDashboard(driver,ReportDriver)
            PaymentMethodScreen(driver,ReportDriver,"bank transfer")
            try:
                IBANScreen(driver,ReportDriver)
            except:
                print("IBAN already done!")
            CheckIfPageLoading(driver)
            EnterDepositAmountScreen(driver,ReportDriver)
            CheckIfPageLoading(driver)
            TransferInstructionsScreen(driver,ReportDriver)                    
            # ReportResults(None,driver,False,"Initial Deposit Flow","KNET and Bank transfer is not working","User should be able to deposit normally using both methods","Check UDF3 abd UDF4")        
            # Passed=False
    if Passed:ReportResults(None,driver,True,"Initial Deposit Flow")


               
        
    