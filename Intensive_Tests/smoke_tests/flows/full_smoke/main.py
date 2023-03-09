import os
import sys


sys.path.append(os.getcwd())
import SystemPath
from Intensive_Tests.signup_login.flows.sign_up.config import Credentials
from Intensive_Tests.smoke_tests.flows.full_smoke.config import SmokeTestData

import json
from BookaCall import BookaCall
from KYC import KYC_FillAll
from PendingDashboard import PendingDashboard


from Intensive_Tests.Mobile_number.flows.verify_number.main import Verify_Mobile_Number
from Intensive_Tests.Withdrawal.flows.main import Withdrawal
from Intensive_Tests.deposits.flows.main import Deposit
from Intensive_Tests.fingerprint.flows.biometric_fingerprint.main import Biometric_fingerprint
from Intensive_Tests.investment_proposal.enums import PredefinedEnums
from Intensive_Tests.investment_proposal.flows.main import Onboarding

from Intensive_Tests.signup_login.flows.sign_in.main import Sign_In




from Intensive_Tests.helpers import APIS, AppiumActions, ApplicationHelpers, AndroidGestures, Random_values, Reporting
from Intensive_Tests.signup_login.flows.sign_up.main import Sign_Up

from CheckFlowAndProceed import CheckFlow_ContinueReg_Showme

from time import sleep
from ConfigureDevices import Appiumdriver


from time import sleep
from GetStartedScreen import GetStartedScreen_SignIn


from Intensive_Tests.enums import limits


class FullSmokeTests():
    risk_score_target = 1
    driver = None
    ReportDriver=None
    def __init__(self):
        self.email=Credentials.email
        with open("/Users/mohamadharb/Documents/Roy Personal/sw_automation_android/BaseClasses/KYC_3.0_JSON_File.json") as file:
        # Load its content and make a new dictionary
            self.JSON=json.load(file)
        pass

    
    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.get_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,"N/A",expected,text_element.text) 
            return False 
        else:   return True

    def define_classes(self):
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"Initial deposit")
        self.APIs=APIS(self.driver,self.email)
        self.ApplicationGestures=ApplicationHelpers(self.driver)
        self.DEPOSITS=Deposit(self.driver,self.email)

        
        temp=self.APIs._get_user_profile("iban_number,total_nav,investment_type")
        iban_available=temp[0]
        if iban_available==False:   self.iban_number=Random_values.generate_alphanumeric_value.in_range(limits.IBAN_MIN,limits.IBAN_MAX)
        else:   self.iban_number=iban_available
        
        self.balance=temp[1]
    
        if temp[2] =="islamic":  self.is_islamic=True
        else: self.is_islamic=False
        
    def backupsignin(self):
        self.driver=Appiumdriver().create_driver_open_app()
        GetStartedScreen_SignIn(self.driver,None)
        (Sign_In(self.driver)._test_happy_path(email=self.email))
        return self.driver

    def full_user_flow(self,user_type="default",flow="default",initial_deposit="bank transfer",additional_deposit="bank transfer"):

        self.user_type = user_type if user_type != "default" else "etf"
        self.flow = flow if flow != "default" else "predefined"

        
    
        self.driver=Appiumdriver().create_driver_open_app()
        

        if "predefined" in self.flow.lower():Onboarding(self.driver,self.user_type).start_predefined_happy_path(PredefinedEnums(3).Get_random_value(),detailed=False)
        elif "customized" in self.flow.lower():Onboarding(self.driver,self.user_type).start_customized_happy_path()
        self.email=Sign_Up(self.driver)._test_happy_path()
        # driver=backupsignin()
        
        self.define_classes()
        

        if not self.APIs.verify_email_and_upload_ids():  print("Issue with verifying email or IDS")
        if self.ApplicationGestures.loading_stuck(): self.driver=self.backupsignin()


        try:CheckFlow_ContinueReg_Showme(self.driver,self.ReportDriver,self.email)
        except: sleep(0.1)


        PendingDashboard(self.driver,self.ReportDriver)
        KYC_FillAll(self.driver,self.ReportDriver,self.JSON)
        BookaCall(self.driver,self.ReportDriver,False,True)

        self.APIs.sign_contract()
        self.APIs.approve_by_civil_id()


        self.DEPOSITS.WIRE.initial_deposit()
        self.APIs._get_user_profile()
        self.APIs._activate_user()
        Verify_Mobile_Number(self.driver,self.email).start_happy_path(True)
        Biometric_fingerprint(self.driver,self.email).start_happy_path(True)
        self.AppiumGestures.return_to_active_dashboard()
        self.AppiumGestures.scrollDown_refresh()

        self.DEPOSITS.WIRE.additional_deposit()

        withdrawals=Withdrawal(self.driver,self.email)
        withdrawals.start_partial_withdrawal_happy_path()
        withdrawals.start_full_withdrawal_happy_path()
        
    def start(self):
        for self.flow in SmokeTestData.flows:
            for self.user_type in SmokeTestData.user_type_options:
                try:
                    self.full_user_flow(self.user_type,self.flow)
                    self.Report.report_testcase(True,"\n%s %s full user test\n\n"%(self.flow,self.user_type))
                except Exception as error:
                    print("ERROR-ERROR-ERROR-ERROR-ERROR-ERROR")
                    print(error)
                    print("ERROR-ERROR-ERROR-ERROR-ERROR-ERROR")
                    
                    self.Report.report_testcase(False,"%s %s full user test"%(self.flow,self.user_type),"N/A","N/A",str(error))