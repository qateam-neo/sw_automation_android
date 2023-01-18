from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from EnterDepositAmount import EnterDepositAmountScreen
from InvestmentProposal import InvestmentProposal
from KNETScreen import KNETScreen
from PaymentMethodScreen import PaymentMethodScreen
from PersonalisePortfolio import PersonalisePortfolio

from ReasonforAdditionalPortfolio import ReasonforAdditionalPortfolio
from TransferInstructionsScreen import TransferInstructionsScreen




def CreatePortfolioAndFund(driver,ReportDriver,JSON,PaymentMethod):
    TestCase ="Create Portfolio And Fund Screen"
    Status = True
    
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/addPortfolioButton"))).click()
    ReasonforAdditionalPortfolio(driver, ReportDriver)
    PersonalisePortfolio(driver,ReportDriver)
    InvestmentProposal(driver,ReportDriver)
    PaymentMethodScreen(driver,ReportDriver,PaymentMethod)
    if PaymentMethod.lower() =="bank transfer" or PaymentMethod.lower()=="banktransfer":
        print("\tBank Transfer method")
        EnterDepositAmountScreen(driver,ReportDriver)
        TransferInstructionsScreen(driver,ReportDriver)
    elif PaymentMethod.lower() =="knet":
        print("\tKNET method")
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btnContinue"))).click()
        EnterDepositAmountScreen(driver,ReportDriver)
        KNETScreen(driver,ReportDriver)
