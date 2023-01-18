
import random
from Intensive_Tests.Withdrawal.config import IDS, Localization_withdrawal, TransferRules
from Intensive_Tests.Withdrawal.flows.Partial_withdrawal.config import Localization_Partial
from Intensive_Tests.enums import limits
from Intensive_Tests.helpers import APIS, AndroidGestures, AppiumActions, Random_values, Reporting



class PartialWithdrawal():
    risk_score_target = 1
    driver = None

    def __init__(self, driver,email,amount=None):
        self.driver = driver
        self.email=email
        self.ReportDriver=None
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"Initial deposit")
        self.APIs=APIS(self.driver,self.email)
        self.balance=self.APIs._get_user_profile("total_nav")
        if amount is None:self.amount= self.amount= Random_values.generate_numeric_value.between_2_numbers(1,TransferRules.Withdrawal.single_portolio.getMaximumWithdrawalamount(self.balance))
        else: self.amount= amount
        

    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.get_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,"N/A",expected,text_element.text) 
            return False 
        else:   return True

    def _enter_withdrawal_reason(self):
        self.AppiumGestures.click_element(IDS.withdrawal_amount.withdrawal_reason_dropdown)
        self.AppiumGestures._check_if_visible("android:id/text1")
        self.AppiumGestures.click_element(("android:id/text1",random.randint(0,8)))
        self.AppiumGestures.click_element("neo.nbkc.smartwealth.demo:id/btnOk")
    
    def enter_amount_screen(self):
        self.testcase="Enter amount screen"
        
        self.AppiumGestures._check_if_visible(IDS.withdrawal_amount.title,11)
        
        self._test_text(IDS.withdrawal_amount.title,Localization_Partial.withdrawal_amount.title)
        self._test_text(IDS.withdrawal_amount.purpose_label,Localization_Partial.withdrawal_amount.purpose_label)
        self._test_text(IDS.withdrawal_amount.withdrawal_account_label,Localization_Partial.withdrawal_amount.withdrawal_account_label)
        self._test_text(IDS.withdrawal_amount.info_label,Localization_Partial.withdrawal_amount.info_label)

        self.AppiumGestures.send_keys_to_element(IDS.withdrawal_amount.withdrawal_amount_entry,self.amount,7)
        self._enter_withdrawal_reason()
        self.AppiumGestures.click_element(IDS.withdrawal_amount.submit_button)
    
    def otp_screen(self):
        self.testcase="OTP screen"
        
        self.AppiumGestures._check_if_visible(IDS.otp_screen.label,10)

        self._test_text(IDS.otp_screen.title,Localization_withdrawal.otp_screen.title)
        self._test_text(IDS.otp_screen.description,Localization_withdrawal.otp_screen.description+" "+self.email)
        self._test_text(IDS.otp_screen.label,Localization_withdrawal.otp_screen.label)
        self._test_text(IDS.otp_screen.continue_button,Localization_withdrawal.otp_screen.continue_button)
        otp_code=self.APIs.withdrawal_otp()
        self.AppiumGestures.send_otp_text((IDS.otp_screen.entries_id,0),otp_code)
        try:self.AppiumGestures.click_element(IDS.otp_screen.continue_button)
        except: print("Automatically moved to next screen")
        

    def thank_you_screen(self):
        #todo: FIXME:  FIXME:  FIXME:  FIXME:  FIXME:  FIXME:  FIXME:  FIXME:  FIXME: 
        self.testcase="Thank you screen"
        self.AppiumGestures._check_if_visible(IDS.thank_you.description,8)

        self._test_text(IDS.thank_you.title,Localization_withdrawal.thank_you.title)
        self._test_text(IDS.thank_you.subtitle,Localization_withdrawal.thank_you.subtitle)
        self._test_text(IDS.thank_you.description,Localization_withdrawal.thank_you.description)
        
        self.AppiumGestures.click_element(IDS.thank_you.close_button)  
        self.AppiumGestures.return_to_active_dashboard()
        
    def start(self):
        self.enter_amount_screen()
        self.otp_screen()
        self.thank_you_screen()
        #TODO: SHould add the more intensive tests here
        
    def test_happy_path(self):
        self.enter_amount_screen()
        self.otp_screen()
        self.thank_you_screen()
