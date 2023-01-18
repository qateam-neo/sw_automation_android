from Intensive_Tests.Withdrawal.config import IDS, Localization_withdrawal, TransferRules
from Intensive_Tests.Withdrawal.flows.Full_withdrawal.main import FullWithdrawal
from Intensive_Tests.Withdrawal.flows.Partial_withdrawal.main import PartialWithdrawal
from Intensive_Tests.helpers import APIS, AndroidGestures, AppiumActions, Random_values, Reporting
import SystemPath

class Withdrawal:
    
    def __init__(self,driver,email):
        self.driver = driver
        self.email=email
        self.ReportDriver=None
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"Withdrawal")
        self.APIs=APIS(self.driver,self.email)
        if self.APIs._get_user_profile("investment_type") =="islamic":  self.is_islamic=True
        else: self.is_islamic=False

        
    
    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.get_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,"N/A",expected,text_element.text) 
            return False 
        else:   return True

    def _fix_withdrawal_screen(self):
        count=0
        while True:
            if self.AppiumGestures._check_if_visible(IDS.Choose_portfolio.select_account):
                break
            else:
                self.AndroidGestures.BACK()
                self.Settings_screen(True)
            if count == 3:
                self.AppiumGestures.click_element(IDS.Settings_screen.home_button)
                self.AppiumGestures.scrollDown_refresh()
                self.Settings_screen(True)
            count=count + 1
                
                

    def Settings_screen(self,skip_details=False):
        self.testcase="settings screen"
        self.AppiumGestures.click_element(IDS.Settings_screen.settings_button,4)
        self.AppiumGestures._check_if_visible(IDS.Settings_screen.title,8)

        if not skip_details:
            self._test_text(IDS.Settings_screen.withdrawal_title,Localization_withdrawal.Settings_screen.withdrawal_title)
            self._test_text(IDS.Settings_screen.withdrawal_description,Localization_withdrawal.Settings_screen.withdrawal_description)
        self.AppiumGestures.click_element(IDS.Settings_screen.withdrawal_button)
        self._fix_withdrawal_screen()
        
    def Choose_portfolio(self,skip_details=False):
        self.testcase="Choose portfolio screen"
        self.AppiumGestures._check_if_visible(IDS.Choose_portfolio.select_account,7)

        if not skip_details:
            self._test_text(IDS.Choose_portfolio.portfolio1_title,Localization_withdrawal.Choose_portfolio.portfolio1_title)
            if self.is_islamic:expected=Localization_withdrawal.Choose_portfolio.portfolio1_type
            else: expected=Localization_withdrawal.Choose_portfolio.islamic_portfolio_type
            self._test_text(IDS.Choose_portfolio.portfolio1_type,expected)
        self.AppiumGestures.click_element(IDS.Choose_portfolio.portfolio1_option)
    
    def Withdrawal_type(self,withdrawal_option,skip_details=False):
        """
        :withdrawal_option should be "full or "partial"
        """
        
        self.testcase="Withdrawal type screen"
        self.AppiumGestures._check_if_visible(IDS.withdrawal_type.withdrawal_type_label,7)
        if not skip_details:
            self._test_text(IDS.withdrawal_type.title,Localization_withdrawal.withdrawal_type.title)
            self._test_text(IDS.withdrawal_type.withdrawal_type_label,Localization_withdrawal.withdrawal_type.withdrawal_type_label)
            self._test_text(IDS.withdrawal_type.Full_withdrawal_title,Localization_withdrawal.withdrawal_type.Full_withdrawal_title)
            self._test_text(IDS.withdrawal_type.Full_withdrawal_description,Localization_withdrawal.withdrawal_type.Full_withdrawal_description)
            self._test_text(IDS.withdrawal_type.Partial_withdrawal_title,Localization_withdrawal.withdrawal_type.Partial_withdrawal_title)
            self._test_text(IDS.withdrawal_type.Partial_withdrawal_description,Localization_withdrawal.withdrawal_type.Partial_withdrawal_description)
        
        if  "partial" in  withdrawal_option.lower():
            self.AppiumGestures.click_element(IDS.withdrawal_type.Partial_withdrawal_button)
        elif "full" in withdrawal_option.lower():
            self.AppiumGestures.click_element(IDS.withdrawal_type.Full_withdrawal_button)
             
        
        self.AppiumGestures.click_element(IDS.withdrawal_type.continue_button)
    
            
    def start_partial_withdrawal_happy_path(self,withdrawal_amount=None):
        self.Report.change_flow("Partial Withdrawal")
        if withdrawal_amount is not None and withdrawal_amount.isdigit(): self.amount=int(withdrawal_amount)
        self.Settings_screen()
        self.Choose_portfolio()
        self.Withdrawal_type("partial")
        PartialWithdrawal(self.driver,self.email).test_happy_path()
            
                    
            
    def start_full_withdrawal_happy_path(self,withdrawal_amount=None):
        self.Report.change_flow("Full Withdrawal")
        self.Settings_screen()
        self.Choose_portfolio()
        self.Withdrawal_type("full")
        FullWithdrawal(self.driver,self.email).test_happy_path()
            
