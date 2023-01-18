
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from BookaCall import BookaCall_Withdrawal
from CheckFeatureFlags import FeatureFlag
from CheckIfPageLoading import CheckIfPageLoading

from EnterWithdrawalAmount_Reason import EnterWithdrawalAmount_Reason
from ManualReport import ReportResults
from MenuScreen import MenuScreen
from OTPScreen import WithdrawalOTPScreen_API
from PortfolioWithdrawalScreen import Portfoliowithdrawal
from WithdrawalThankYou import WithdrawalThankYou
from WithdrawaltypeScreen import WithdrawalTypeScreen


def WithdrawalFlow(driver,ReportDriver,WithdrawalType,User_ID,Amount=1000):
    WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/navigation_more"))).click()
    Status=True
    TestCase="Withdrawal Flow (%s)"%WithdrawalType
    # #Refresh Application
    # driver.press_keycode(3)
    # sleep(0.5)
    # driver.press_keycode(187)
    # sleep(0.5)
    # taponcoordinates(driver,550,850)
   
    MenuScreen(driver, ReportDriver,"Withdrawals")
    CheckIfPageLoading(driver)
    Portfoliowithdrawal(driver,ReportDriver)
    CheckIfPageLoading(driver)
    WithdrawalTypeScreen(driver,ReportDriver,WithdrawalType)
    try:WebDriverWait(driver,8).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/btnContinue"))).click()
    except:sleep(0.1)
    if "full" in WithdrawalType.lower():
        BookaCall_Withdrawal(driver,ReportDriver,False,True)
    EnterWithdrawalAmount_Reason(driver,ReportDriver,WithdrawalType,Amount)
    WithdrawalOTPScreen_API(driver,ReportDriver,User_ID)
    # WithdrawalOTPScreen(driver,ReportDriver)
    WithdrawalThankYou(driver,ReportDriver)
    driver.press_keycode(4)
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/navigation_home"))).click()
    
    if ReportDriver==None:
        print("No Report Driver found")
        ReportResults(ReportDriver, driver, True,TestCase,"N/A",  "N/A")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)