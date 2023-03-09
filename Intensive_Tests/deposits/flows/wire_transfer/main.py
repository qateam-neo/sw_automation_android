
from Intensive_Tests.deposits.config import IDS, Localization_deposits, TransferRules
from Intensive_Tests.enums import limits
from Intensive_Tests.helpers import APIS, AndroidGestures, AppiumActions, Random_values, Reporting
from Intensive_Tests.pending_dashboard.flows.main import PendingDashboard
from .config import  Localization_BT



class WireTransferFlow():
    risk_score_target = 1
    driver = None

    def __init__(self, driver,email):
        self.driver = driver
        
        self.email=email
        self.ReportDriver=None
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"Initial deposit")
        self.APIs=APIS(self.driver,self.email)
        self.amount= Random_values.generate_numeric_value.between_2_numbers(TransferRules.BKTransferBoundaries.initial_deposit.MIN,TransferRules.BKTransferBoundaries.initial_deposit.MAX)
        temp=self.APIs._get_user_profile("iban_number,total_nav,investment_type")
        iban_available=temp[0]
        if iban_available==False:   self.iban_number=Random_values.generate_alphanumeric_value.in_range(limits.IBAN_MIN,limits.IBAN_MAX)
        else:   self.iban_number=iban_available
        
        self.balance=temp[1]
    
        if temp[2] =="islamic":  self.is_islamic=True
        else: self.is_islamic=False
   
    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.get_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,"N/A",expected,text_element.text) 
            return False 
        else:   return True

    def active_dashboard(self):
        self.testcase="Active Dashboard"
        self.AppiumGestures.return_to_active_dashboard()

        self.AppiumGestures._check_if_visible(IDS.ActiveDashboard.deposit_button)
        self.AppiumGestures.click_element(IDS.ActiveDashboard.deposit_button)
        
    def active_select_portfolio(self):
        self.testcase="Select Portfolio to Deposit"
        self.AppiumGestures._check_if_visible(IDS.active_select_portfolio.portfolio1_option,6)
        
        self._test_text(IDS.active_select_portfolio.portfolio_title,Localization_deposits.active_select_portfolio.portfolio_title)
        
        if self.is_islamic: expected=Localization_deposits.active_select_portfolio.islamic_portfolio_type
        else:               expected=Localization_deposits.active_select_portfolio.portfolio_type
        self._test_text(IDS.active_select_portfolio.portfolio_type,expected)
        
        self._test_text(IDS.active_select_portfolio.portfolio_amount,'${:,}'.format(int(self.balance)) )

        self.AppiumGestures.click_element(IDS.active_select_portfolio.portfolio1_option)

    
    def pending_dashboard(self):
        
        self.testcase="Pending Dashboard"
        self.AppiumGestures.return_to_pending_dashboard()
        self.AppiumGestures.wait_for_element(IDS.PendingDashboard.initial_deposit_time,10)
        
        self._test_text(IDS.PendingDashboard.title,Localization_deposits.PendingDashboard.title)
        self._test_text(IDS.PendingDashboard.description,Localization_deposits.PendingDashboard.description)
        
        self._test_text(IDS.PendingDashboard.eid_title,Localization_deposits.PendingDashboard.eid_title)
        self._test_text(IDS.PendingDashboard.eid_description,Localization_deposits.PendingDashboard.eid_description)
        
        self._test_text(IDS.PendingDashboard.kyc_title,Localization_deposits.PendingDashboard.kyc_title)
        self._test_text(IDS.PendingDashboard.kyc_description,Localization_deposits.PendingDashboard.kyc_description)
        
        self._test_text(IDS.PendingDashboard.initial_deposit_title,Localization_deposits.PendingDashboard.initial_deposit_title)
        self._test_text(IDS.PendingDashboard.initial_deposit_time,Localization_deposits.PendingDashboard.initial_deposit_time)
        self._test_text(IDS.PendingDashboard.initial_deposit_description,Localization_deposits.PendingDashboard.initial_deposit_description)
        
        self.AppiumGestures.click_element(IDS.PendingDashboard.initial_deposit_image_button)
        

    def select_payment_method(self,deposit_option_id):
        
        self.testcase="Select Payment Method"
        self.AppiumGestures.wait_for_element(IDS.SelectPaymentMethod.bt_title,10)

        self._test_text(IDS.SelectPaymentMethod.title,Localization_deposits.SelectPaymentMethod.title)
        self._test_text(IDS.SelectPaymentMethod.description,Localization_deposits.SelectPaymentMethod.description)
        
        self._test_text(IDS.SelectPaymentMethod.bt_title,Localization_deposits.SelectPaymentMethod.bt_title)
        # self._test_text(IDS.SelectPaymentMethod.bt_time,Localization_deposits.SelectPaymentMethod.bt_time)
        self._test_text(IDS.SelectPaymentMethod.bt_description,Localization_deposits.SelectPaymentMethod.bt_description)
        
        self._test_text(IDS.SelectPaymentMethod.knet_title,Localization_deposits.SelectPaymentMethod.knet_title)
        # self._test_text(IDS.SelectPaymentMethod.knet_time,Localization_deposits.SelectPaymentMethod.knet_time)
        self._test_text(IDS.SelectPaymentMethod.knet_description,Localization_deposits.SelectPaymentMethod.knet_description)
        
        # self._test_text(IDS.SelectPaymentMethod.dd_title,Localization_deposits.SelectPaymentMethod.dd_title)
        # self._test_text(IDS.SelectPaymentMethod.dd_time,Localization_deposits.SelectPaymentMethod.dd_time)
        # self._test_text(IDS.SelectPaymentMethod.dd_description,Localization_deposits.SelectPaymentMethod.dd_description)

        self.AppiumGestures.click_element(deposit_option_id)
        
        self.AppiumGestures.click_element(IDS.SelectPaymentMethod.continue_button)
    
    def iban(self):
        
        self.testcase="IBAN"        
        self.AppiumGestures.wait_for_element(IDS.IBAN.iban_limit_message,6)

        
        self._test_text(IDS.IBAN.title,Localization_BT.IBAN.title)
        self._test_text(IDS.IBAN.description,Localization_BT.IBAN.description)
        self._test_text(IDS.IBAN.iban_limit_message,Localization_BT.IBAN.iban_limit_message)
        
        self.AppiumGestures.send_keys_to_element(IDS.IBAN.iban_entry,self.iban_number)
        self.AppiumGestures.click_element(IDS.IBAN.continue_button)
        
    def enter_amount(self):
        self.testcase="Enter Amount"        
        self.AppiumGestures._check_if_visible(IDS.Enter_Amount.description,6)
        self._test_text(IDS.Enter_Amount.title,Localization_BT.Enter_Amount.title)
        self._test_text(IDS.Enter_Amount.description,Localization_BT.Enter_Amount.description)
        self._test_text(IDS.Enter_Amount.iban,self.iban_number)
        
        self.AppiumGestures.send_keys_to_element(IDS.Enter_Amount.amount_entry,self.amount)
        if self.AppiumGestures._check_if_visible(IDS.Enter_Amount.error_message,1):
            self.Report.report_testcase(False,self.testcase,"","Initial deposit amount limit: %s to %s"%(str(TransferRules.BKTransferBoundaries.initial_deposit.MIN),str(TransferRules.BKTransferBoundaries.initial_deposit.MAX)),"amount is: "+str(self.amount))
        self.AppiumGestures.click_element(IDS.Enter_Amount.continue_button)

    def transfer_instructions(self):
        self.testcase="Transfer Instructions"        

        self.AppiumGestures._check_if_visible(IDS.TransferInstructions.title,6)
        self._test_text(IDS.TransferInstructions.title,Localization_BT.TransferInstructions.title)
        self._test_text(IDS.TransferInstructions.description,Localization_BT.TransferInstructions.description)
        
        # self._test_text(IDS.TransferInstructions.continue_button,Localization_BT.TransferInstructions.continue_button)
        
        try: 
            self.AppiumGestures.click_element(IDS.TransferInstructions.continue_button)
        except:
            try:
                self.AppiumGestures.scrollDown_refresh()
                self.AppiumGestures.click_element(IDS.TransferInstructions.continue_button)
            except:
                self.AndroidGestures.BACK()
    
    def _validate_initial_deposit_success(self):
        self.testcase="Pending Dashboard Initial Deposit Done!"
        if self.AppiumGestures._check_if_visible(IDS.PendingDashboard.initial_deposit_title,15):
            if self.AppiumGestures._check_if_visible(IDS.PendingDashboard.initial_deposit_time,1):
                self.Report.report_testcase(False,self.testcase,"","All 3 steps should be cleared","Initial Deposit step is pending")
    
    def _activate_user_using_API(self):
        self.APIs._activate_user()

    def start(self):
        PendingDashboard(self.driver).start(False)
        self.select_payment_method(IDS.SelectPaymentMethod.bt_option_button)
        self.iban()
        
    def test_initial_deposit_happy_path(self):
        self.Report.change_flow("Initial deposit")

        PendingDashboard(self.driver).start(False)
        self.select_payment_method(IDS.SelectPaymentMethod.bt_option_button)
        if self.AppiumGestures._check_if_visible(IDS.IBAN.iban_entry,10):self.iban()
        self.enter_amount()
        try:self.transfer_instructions()
        except: self.AppiumGestures.return_to_pending_dashboard()
        self.APIs._activate_user(self.amount)
        
        try:self.AppiumGestures.click_element(IDS.PendingDashboard.do_it_later_button,6)
        except: print("Can't find go to dashboard")
        
        self.AppiumGestures.scrollDown_refresh()
        self.AppiumGestures.return_to_active_dashboard()
        

    def test_additional_deposit_happy_path(self):
        self.Report.change_flow("Additional deposit")

        self.active_dashboard()
        self.active_select_portfolio()
        self.select_payment_method(IDS.SelectPaymentMethod.bt_option_button)
        if self.AppiumGestures._check_if_visible(IDS.IBAN.iban_entry,8):self.iban()
        self.enter_amount()
        self.transfer_instructions()
        self.AppiumGestures.return_to_active_dashboard()