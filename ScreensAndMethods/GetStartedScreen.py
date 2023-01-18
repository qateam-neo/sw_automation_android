
from time import sleep
from CheckIfPageLoading import CheckIfPageLoading
from Intensive_Tests.investment_proposal.config import IDS
from ManualReport import ReportResults
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

TestCase="Get Started Screen"


def GetStartedScreen_SignUp(driver,ReportDriver):
    TestCase ="'Get Started' Screen"
    GetStarted_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, IDS.GetStartedScreen.get_started_button)))
    GetStarted_button.click()
    ReportResults(ReportDriver, driver, True,TestCase,"N/A",  "N/A")
    



def GetStartedScreen_SignIn(driver,ReportDriver):
    TestCase ="'Get Started' Screen"
    SignIn_Button = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/loginButton")))
    SignIn_Button.click()
    ReportResults(ReportDriver, driver, True,TestCase,"N/A",  "N/A")

