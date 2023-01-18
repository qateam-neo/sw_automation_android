

from ConfirmMobileScreen import ConfirmMobileScreen_Test
from Continue_Registraction_Flow import ContinueReg_ThankYouScreen
from FingerPrintScreen import FingerPrintScreen_Test
from Intensive_Tests.Mobile_number.flows.verify_number.main import Verify_Mobile_Number
from PendingDashboard_to_ContinueRegistration import PendingDashboard_to_ContinueRegistration
from Show_me_the_app_flow import Showmetheappflow_ThankYouScreen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def CheckFlow_ContinueReg_Showme(driver,ReportDriver,email):
    
    ## Waiting for Show me the app or continue regirstration.
    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/signedUpTv")))
    try:
        ContinueReg_or_Showmetheapp = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/continueButton")))
        ContinueReg_or_ShowmetheappText=ContinueReg_or_Showmetheapp.text
    except:
        ContinueReg_or_Showmetheapp = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/showAppButton")))
        ContinueReg_or_ShowmetheappText=ContinueReg_or_Showmetheapp.text


    # print(ContinueReg_or_Showmetheapp)
    if (ContinueReg_or_ShowmetheappText=="Continue Registration"):
        ContinueReg_ThankYouScreen(driver,ReportDriver)
        FingerPrintScreen_Test(driver,ReportDriver)
        
    if (ContinueReg_or_ShowmetheappText=="Show me the app"):
        Showmetheappflow_ThankYouScreen(driver,ReportDriver)
        try:(Verify_Mobile_Number(driver,email).start_happy_path())
        except: print("Mobile number is already verified")
        FingerPrintScreen_Test (driver,ReportDriver)
        PendingDashboard_to_ContinueRegistration(driver,ReportDriver)

