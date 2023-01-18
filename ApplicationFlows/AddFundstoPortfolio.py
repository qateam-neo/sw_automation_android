
from colorama import Fore
from AddFundsScreen import AddFundsScreen
from CheckFeatureFlags import FeatureFlag
from OTPScreen import DepositOTPOfflineUser
from EnterDepositAmount import EnterDepositAmountScreen
from IBANScreen import IBANScreen
from KNETScreen import KNETScreen
from ManualReport import ReportResults
from PaymentMethodScreen import PaymentMethodScreen
from TransferInstructionsScreen import TransferInstructionsScreen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def AddFundsFlow(driver,ReportDriver,PaymentMethod,User_Type,Amount=10000):
    Status=True
    TestCase="Additional Deposit Flow using "+PaymentMethod
    WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/navigation_transfer"))).click()
    AddFundsScreen(driver,ReportDriver)
    
    
    FeatureAvailable=FeatureFlag(driver,"Bank Transfer")
    if FeatureAvailable:
        PaymentMethodScreen(driver,ReportDriver,PaymentMethod)
        if PaymentMethod.lower() =="bank transfer" or PaymentMethod.lower()=="banktransfer":
            try:
                IBANScreen(driver,ReportDriver)
            except:
                print("IBAN already done!")
            EnterDepositAmountScreen(driver,ReportDriver)
            try: DepositOTPOfflineUser(driver,ReportDriver)
            except:print("No OTP needed or OTP FAILED!!")
            TransferInstructionsScreen(driver,ReportDriver)
        elif PaymentMethod.lower() =="knet":
            WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btnContinue"))).click()
            EnterDepositAmountScreen(driver,ReportDriver)
            KNETScreen(driver,ReportDriver)
    else:
        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/navigation_home").click()


    if ReportDriver==None:
        print("No Report Driver found")
        ReportResults(ReportDriver, driver, True,TestCase,"N/A",  "N/A")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)

