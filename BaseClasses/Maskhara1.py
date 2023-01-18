# from Intensive_Tests.deposits.flows.main import Deposit
from Intensive_Tests.helpers import APIS
import SystemPath
# import json
from ConfigureDevices import Appiumdriver
from Intensive_Tests.deposits.flows.wire_transfer.main import WireTransferFlow
from Intensive_Tests.helpers import APIS, AppiumActions, ApplicationHelpers

from Intensive_Tests.signup_login.flows.sign_in.config import Credentials
# from Intensive_Tests.signup_login.flows.sign_in.main import Sign_In
from selenium.webdriver.common.by import By


# with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
# # Load its content and make a new dictionary
#     JSON=json.load(file)
email=Credentials.email

##################################################################
# ReportDriver=None
driver=Appiumdriver().create_driver_no_app()

AppiumGestures=AppiumActions(driver)
# ApplicationGestures=ApplicationHelpers(driver)

# Apis=APIS(driver,email)


AppiumGestures.click_element