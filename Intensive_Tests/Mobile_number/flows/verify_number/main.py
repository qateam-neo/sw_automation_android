
from Intensive_Tests.Mobile_number.config import IDS
from Intensive_Tests.Mobile_number.flows.verify_number.config import Localization_Mobile_number
from Intensive_Tests.enums import limits
from Intensive_Tests.helpers import APIS, AndroidGestures, AppiumActions, Random_values, Reporting



class Verify_Mobile_Number():
    risk_score_target = 1
    driver = None

    def __init__(self, driver, email):
        self.driver = driver
        self.email = email
        self.risk_score_target="N/A"
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"Verifying Mobile Number")
        self.APIs=APIS(self.driver,self.email)
        self.testcase="Verify Mobile Number"
        
    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.get_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,text_element.text,expected) 
            return False 
        else:   return True


    def test_verify_mobile_number_screen(self):
        self.testcase="Verify Mobile Number"
        
        self._test_text(IDS.Verify_Mobile_number_screen.title,Localization_Mobile_number.Verify_Mobile_number.title) 
        self._test_text(IDS.Verify_Mobile_number_screen.description,Localization_Mobile_number.Verify_Mobile_number.description) 
        self._test_text(IDS.Verify_Mobile_number_screen.support_message,Localization_Mobile_number.Verify_Mobile_number.support_message) 
        self._test_text(IDS.Verify_Mobile_number_screen.continue_button,Localization_Mobile_number.Verify_Mobile_number.continue_button) 
        self._test_text(IDS.Verify_Mobile_number_screen.number,self.APIs._get_mobile_number(self.email,"text"))
        self.AppiumGestures.click_element(IDS.Verify_Mobile_number_screen.continue_button)
    
    def test_otp(self):
        self.testcase="Verify Mobile Number OTP"

        if self.AppiumGestures._check_if_visible(IDS.otp.otp_entry,7):
            self.mobile_otp=str(APIS._get_mobile_number_otp())
            otp_entries=self.AppiumGestures.get_elements(IDS.otp.otp_entry)
            for i in range(0,len(otp_entries)):
                otp_entries[i].send_keys(self.mobile_otp[i])                
                self.AppiumGestures.click_element(IDS.otp.continue_button)
        else:
            self.Report.report_testcase(False,self.testcase,self.risk_score_target,"OTP","Error on otp screen not opening")
    
    def test_thank_you_screen(self):
        self.testcase="Verify Mobile Number Thank You"

        self._test_text(IDS.thank_you.title,Localization_Mobile_number.thank_you.title)    
        self._test_text(IDS.thank_you.description,Localization_Mobile_number.thank_you.description)    
        self._test_text(IDS.thank_you.method_text,Localization_Mobile_number.thank_you.method_text)    
        self._test_text(IDS.thank_you.email_option,Localization_Mobile_number.thank_you.email_option)    
        self._test_text(IDS.thank_you.sms_option,Localization_Mobile_number.thank_you.sms_option)    
        self.AppiumGestures.click_element(IDS.thank_you.email_option)
        
    def start_happy_path(self,skip_verify=False):
        if self.AppiumGestures._check_if_visible(IDS.Verify_Mobile_number_screen.number,10):
            if not skip_verify:
                self.test_verify_mobile_number_screen()
                self.test_otp()
                self.test_thank_you_screen()
            else:
                self.AndroidGestures.BACK()
        else:
            self.Report.report_testcase_not_shown(self.testcase)
                