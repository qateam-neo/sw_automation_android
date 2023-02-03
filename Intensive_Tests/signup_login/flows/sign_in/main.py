
from time import sleep
import requests
from Intensive_Tests.enums import limits
from Intensive_Tests.helpers import APIS, AndroidGestures, AppiumActions, DataBase, Random_values, Reporting
from Intensive_Tests.signup_login.config import IDS
from Intensive_Tests.signup_login.flows.sign_in.config import Credentials



class Sign_In():
    risk_score_target = 1
    driver = None

    def __init__(self,driver):
        self.driver = driver
        self.ReportDriver=None
        self.email = Credentials.email
        self.prefix=self._get_prefix()
        self.password = Credentials.password
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"customized")
        self.DataBase=DataBase()
        self.APIs=APIS(self.driver,self.email)
        self.testcase= "Sign In"
        
    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.get_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,text_element.text,expected) 
            return False 
        else:   return True


    def get_new_email(self):
        self.email=self.APIs.get_email_count()


    def _get_prefix(self):
        self.prefix= self.email.replace("@neo.ae","")
        while True:
            if self.prefix[len(self.prefix)-1].isdigit(): self.prefix=self.prefix[:-1]
            else: return self.prefix
            
    def _test_backup_valid_email(self):
        self.email=self.DataBase.get_latest_email("roy.braish")
        self.APIs.__init__(email=self.email)
        self.test_valid_email()
    
    def test_valid_email(self):
        self.AppiumGestures.send_keys_to_element(IDS.SignIn.email_entry,self.email)
        
        if self.AppiumGestures._check_if_visible(IDS.SignIn.email_error_icon,1):
            self.Report.report_testcase(False,self.testcase,"","Correct Email Format","Wrong Email Format")
        
    def analyze_screen(self,timeout=7):
        if self.AppiumGestures._check_if_visible(IDS.SignIn.error_messages.wrong_email_password,5): 
                self.AppiumGestures.click_element(IDS.SignIn.error_messages.ok_button)
                return False
        else:
            return True
    
    def test_valid_password(self):
        if self.AppiumGestures.get_element(IDS.SignIn.password_entry).text=="•••••••••••":print("We Can skip password")
        else:self.AppiumGestures.send_keys_to_element(IDS.SignIn.password_entry,self.password)

    def _test_happy_path(self,email="from_credentials_DEFAULT"):
        self.AppiumGestures._check_if_visible(IDS.SignIn.title)
        if email!= "from_credentials_DEFAULT":
            self.email=email
        self.test_valid_email()
        self.test_valid_password()
        
        self.AppiumGestures.click_element(IDS.SignIn.remember_me_checkbox)
        self.AppiumGestures.click_element(IDS.SignIn.login_button)
        
        if not self.analyze_screen(1): 
            self._test_backup_valid_email()
            self.AppiumGestures.click_element(IDS.SignIn.login_button)
        
        if self.AppiumGestures._check_if_visible(IDS.Notification_Intercome.close_button,7):
            self.AppiumGestures.click_element(IDS.Notification_Intercome.close_button)
        return self.email
            