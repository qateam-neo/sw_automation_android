
from time import sleep
import requests
from Intensive_Tests.enums import limits
from Intensive_Tests.helpers import APIS, AndroidGestures, AppiumActions, DataBase, Random_values, Reporting
from Intensive_Tests.signup_login.config import IDS
from Intensive_Tests.signup_login.flows.sign_up.config import Credentials, Localization_SignUp



class Sign_Up():
    risk_score_target = 1
    driver = None

    def __init__(self,driver):
        self.driver = driver
        self.ReportDriver=None
        
        self.email = Credentials.email
        self.password = Credentials.password
        self.first_name=Credentials.first_name
        self.last_name=Credentials.last_name
        
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"customized")
        self.DataBase=DataBase()
        self.APIs=APIS(self.driver,self.email)

        self.testcase= "Sign Up"
        
    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.get_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,text_element.text,expected) 
            return False 
        else:   return True

    def _test_backup_valid_email(self):
        self.APIs.__init__(email=self.email)
        self._get_new_email()
        self.test_valid_email()


    def _get_new_email(self):
        self.email=self.APIs.get_email_count()
        self.APIs.__init__(email=self.email)



    def _get_prefix(self):
        self.prefix= self.email.replace("@neo.ae","")
        while True:
            if self.prefix[len(self.prefix)-1].isdigit(): self.prefix=self.prefix[:-1]
            else: return self.prefix

    def test_valid_first_name(self):
        self.AppiumGestures.send_keys_to_element(IDS.SignUp.first_name_entry,self.first_name)
   
    def test_valid_last_name(self):
        self.AppiumGestures.send_keys_to_element(IDS.SignUp.last_name_entry,self.last_name)

    def test_valid_email(self):
        self.AppiumGestures.send_keys_to_element(IDS.SignUp.email_entry,self.email)
        if self.AppiumGestures._check_if_visible(IDS.SignUp.email_error_icon,1):
            self.Report.report_testcase(False,self.testcase,"","Correct Email Format","Wrong Email Format","Enter a new email")

    def test_valid_password(self):
        if self.AppiumGestures.get_element(IDS.SignUp.pass_entry).text=="•••••••••••":print("We Can skip password")
        else:self.AppiumGestures.send_keys_to_element(IDS.SignUp.pass_entry,self.password)

   
    def _test_passed(self,timeout=7):
        if self.AppiumGestures._check_if_visible(IDS.SignUp.error_messages.email_exists.title,7): 
            
            return False
        else:
            return True
    
    def _analyze_error(self):
        if self._test_text(IDS.SignUp.error_messages.email_exists.title,Localization_SignUp.SignUp.error_messages.email_exists.title):
            self.AppiumGestures.click_element(IDS.SignUp.error_messages.email_exists.cancel_button)
            self.Report.report_testcase(False,self.testcase,self.risk_score_target,"Email exists","Expecting a new email") 
            self._test_backup_valid_email()            
            self.AppiumGestures.click_element(IDS.SignUp.continue_button)
        else:
            print("Unknown error occurred (ERROR NOT DEFINED IN CODE)")

    def _test_happy_path(self):
        self.AppiumGestures._check_if_visible(IDS.SignUp.title)
        
        self.test_valid_first_name()
        self.test_valid_last_name()
        self.test_valid_email()
        self.test_valid_password()
        
        self.AppiumGestures.click_element(IDS.SignUp.continue_button,4)
        
        while not self._test_passed(): 
            self._analyze_error()

        return self.email
            