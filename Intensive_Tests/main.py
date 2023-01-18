from Intensive_Tests.Mobile_number.flows.verify_number.main import Verify_Mobile_Number
from Intensive_Tests.Withdrawal.flows.main import Withdrawal
from Intensive_Tests.deposits.flows.main import Deposit
from Intensive_Tests.fingerprint.flows.biometric_fingerprint.main import Biometric_fingerprint
from Intensive_Tests.investment_proposal.enums import PredefinedEnums
from Intensive_Tests.investment_proposal.flows.main import Onboarding
import SystemPath

from ConfirmMobileScreen import ConfirmMobileScreen_Test
from FingerPrintScreen import FingerPrintScreen_Test
from GesturesAndMotions import RefreshScreenusingswipe
from Intensive_Tests.signup_login.config import IDS
from Intensive_Tests.signup_login.flows.sign_in.main import Sign_In


from BookaCall import BookaCall
from KYC import KYC_FillAll
from PendingDashboard import PendingDashboard


from Intensive_Tests.helpers import APIS, AndroidGestures,AppiumActions, ApplicationHelpers
from Intensive_Tests.signup_login.flows.sign_up.main import Sign_Up

from CheckFlowAndProceed import CheckFlow_ContinueReg_Showme
from Intensive_Tests.signup_login.flows.sign_up.config import Credentials

from time import sleep
from ConfigureDevices import Appiumdriver


import json
from time import sleep
from GetStartedScreen import GetStartedScreen_SignIn


# with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
# # Load its content and make a new dictionary
#     JSON=json.load(file)
email=Credentials.email

##################################################################
ReportDriver=None
def backupsignin():
    driver=Appiumdriver().create_driver_open_app()
    GetStartedScreen_SignIn(driver,ReportDriver)
    (Sign_In(driver)._test_happy_path())
    return driver



driver=Appiumdriver().create_driver_open_app()

AppiumGestures=AppiumActions(driver)
ApplicationGestures=ApplicationHelpers(driver)

Onboarding(driver,"islamic").start_predefined_happy_path(PredefinedEnums.GROWTH,detailed=False)
email=Sign_Up(driver)._test_happy_path()
Apis=APIS(driver,email)
DEPOSITS=Deposit(driver,email)



if not Apis.verify_email_and_upload_ids():  print("Issue with verifying email or IDS")
if ApplicationGestures.loading_stuck(): driver=backupsignin()

try:CheckFlow_ContinueReg_Showme(driver,ReportDriver,email)
except: sleep(0.1)


# PendingDashboard(driver,ReportDriver)
# KYC_FillAll(driver,ReportDriver,JSON)
# BookaCall(driver,ReportDriver,False,True)

Apis.sign_contract()
Apis.approve_by_civil_id()


DEPOSITS.KNET.initial_deposit()

Verify_Mobile_Number(driver,email).start_happy_path(True)
Biometric_fingerprint(driver,email).start_happy_path(True)
AppiumGestures.return_to_active_dashboard()
AppiumGestures.scrollDown_refresh()

DEPOSITS.WIRE.additional_deposit()

withdrawals=Withdrawal(driver,email)
withdrawals.start_partial_withdrawal_happy_path()
withdrawals.start_full_withdrawal_happy_path()