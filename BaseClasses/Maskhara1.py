# from Intensive_Tests.deposits.flows.main import Deposit
import os,sys
sys.path.append(os.getcwd())
import SystemPath
from Intensive_Tests.kyc.flows.personal_info.main import PersonalInfo

from Intensive_Tests.pending_dashboard.flows.main import PendingDashboard
# import json
from ConfigureDevices import Appiumdriver
from Intensive_Tests.helpers import AppiumActions

from Intensive_Tests.signup_login.flows.sign_in.config import Credentials
# from Intensive_Tests.signup_login.flows.sign_in.main import Sign_In
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from Intensive_Tests.kyc.flows.personal_info.config import KYC_Fields
from Intensive_Tests.kyc.config import IDS

from selenium.webdriver.support.ui import WebDriverWait # needs to be used when creating a function everytime
from selenium.webdriver.support import expected_conditions # needs to be used when creating a function everytime
# with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
# # Load its content and make a new dictionary
#     JSON=json.load(file)
email=Credentials.email
ReportDriver=None



##################################################################
# ReportDriver=None
driver=Appiumdriver().create_driver_no_app()

AppiumGestures=AppiumActions(driver)
# WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.ID,IDS.input_parent_id)))        
# parent=AppiumGestures.find_element_parent_by_text(KYC_Fields.Civil_id_expiry)
 
# AppiumGestures.fill_list_picker(parent,KYC_Fields.Nationality)

# a=driver.find_element(By.ID,'android:id/month_view')
# c=a.find_element(By.CLASS_NAME,"android.view.View")
# print(c.get_attribute("content-desc"))
# driver.find_element(By.ID,IDS.input_parent_id)
# Find the parent ViewGroup element
# parent = element.find_element_by_xpath('..')

# PendingDashboard(driver).start(False)
PersonalInfo(driver).start_happy_path()
# AppiumGestures.fill_date_picker(parent,KYC_Fields.Civil_id_expiry)

# ApplicationGestures=ApplicationHelpers(driver)

# Apis=APIS(driver,email)
