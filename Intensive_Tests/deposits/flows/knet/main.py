
from Intensive_Tests.deposits.config import IDS, KNET_Credentials, Localization_deposits, TransferRules
from Intensive_Tests.deposits.flows.wire_transfer.main import WireTransferFlow
from Intensive_Tests.enums import limits
from Intensive_Tests.helpers import APIS, AndroidGestures, AppiumActions, Random_values, Reporting
from .config import   Localization_KNET



class KNETFlow():
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
        self.amount= Random_values.generate_numeric_value.between_2_numbers(TransferRules.KNETBoundaries.initial_deposit.MIN,TransferRules.KNETBoundaries.initial_deposit.MAX)
        temp=self.APIs._get_user_profile("total_nav,investment_type")
        
        self.balance=temp[0]
        if temp[1] =="islamic":  self.is_islamic=True
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

        try:
            self.islamic_popup()
        except:
            print("islamic popup")
        
        
    
    def islamic_popup(self,detailed=True):
        
        self.testcase="Islamic popup"
        self.AppiumGestures._check_if_visible(IDS.KNETPopup.close_button,8)
        if detailed:
            self._test_text(IDS.KNETPopup.title,Localization_KNET.KNETPopup.title)
            self._test_text(IDS.KNETPopup.description,Localization_KNET.KNETPopup.description)
            self._test_text(IDS.KNETPopup.continue_button,Localization_KNET.KNETPopup.continue_button)
        self.AppiumGestures.click_element(IDS.KNETPopup.continue_button)
        
    
    def enter_amount(self):
        self.testcase="Enter Amount"        
        self.AppiumGestures._check_if_visible(IDS.Enter_Amount.description,6)
        self._test_text(IDS.Enter_Amount.title,Localization_KNET.Enter_Amount.title)
        self._test_text(IDS.Enter_Amount.description,Localization_KNET.Enter_Amount.description)
        
        self.AppiumGestures.send_keys_to_element(IDS.Enter_Amount.amount_entry,self.amount)
        if self.AppiumGestures._check_if_visible(IDS.Enter_Amount.error_message,1):
            self.Report.report_testcase(False,self.testcase,"","Initial deposit amount limit: %s to %s"%(str(TransferRules.KNETBoundaries.initial_deposit.MIN),str(TransferRules.BKTransferBoundaries.initial_deposit.MAX)),"amount is: "+str(self.amount))
        self.AppiumGestures.click_element(IDS.Enter_Amount.continue_button)

        
    
    def _validate_initial_deposit_success(self):
        self.testcase="Pending Dashboard Initial Deposit Done!"
        if self.AppiumGestures._check_if_visible(IDS.PendingDashboard.initial_deposit_title,15):
            if self.AppiumGestures._check_if_visible(IDS.PendingDashboard.initial_deposit_time,1):
                self.Report.report_testcase(False,self.testcase,"","All 3 steps should be cleared","Initial Deposit step is pending")
    
    def _activate_user_using_API(self):
        self.APIs._activate_user()

        
    def knet_screen(self):
        count=0
        while self.AppiumGestures.wait_for_element_class(("android.widget.TextView","Add Funds"),10)==False or self.AppiumGestures.wait_for_element_class(IDS.KNET_class_locators.bank_button)==False:
            if count==4:
                raise ValueError("KNET screen took more than 40 seconds to load")
        self.AppiumGestures.wait_for_element_class(IDS.KNET_class_locators.bank_button).click()
        self.AppiumGestures.search_element_by_id_text(IDS.KNET_class_locators.knet_testcard_button).click()
        
        self.AppiumGestures.wait_for_element_class(IDS.KNET_class_locators.month_dropdown).click()
        self.AppiumGestures.search_element_by_id_text(IDS.KNET_class_locators.month_button).click()
        
        self.AppiumGestures.wait_for_element_class(IDS.KNET_class_locators.year_dropdown).click()
        self.AppiumGestures.search_element_by_id_text(IDS.KNET_class_locators.year_button).click()
        
        InputFields=self.AppiumGestures.wait_for_elements_class(IDS.KNET_class_locators.cardnumber_pin_entry)
        InputFields[0].send_keys(KNET_Credentials.card_number)
        InputFields[1].send_keys(KNET_Credentials.pin)
        
        self.AppiumGestures.wait_for_element_class(IDS.KNET_class_locators.submit_button).click()
        while True:
            if self.AppiumGestures.wait_for_element_class(IDS.KNET_class_locators.second_screen.confirm)!=False:
                self.AppiumGestures.wait_for_element_class(IDS.KNET_class_locators.second_screen.confirm).click()
                break
            elif self.AppiumGestures.wait_for_element(IDS.KNET_class_locators.error_screen_IDS.title)!=False:
                self.AppiumGestures.click_element(IDS.KNET_class_locators.error_screen_IDS.back_button)
                self.Report.report_testcase(False,"KNET screen","N/A","KNET should be enabled","KNET is not enabled","Enable UDF# and UDF4")
                self.AppiumGestures.return_to_payment_method()
                return False
            elif self.AppiumGestures.wait_for_element_class(IDS.KNET_class_locators.submit_button)!=False:
                self.AppiumGestures.wait_for_element_class(IDS.KNET_class_locators.submit_button).click()
        return True




    def start(self):
        self.pending_dashboard()
        self.select_payment_method(IDS.SelectPaymentMethod.knet_option_button)
        self.iban()
        
    def test_initial_deposit_happy_path(self):
        self.Report.change_flow("Initial deposit")

        self.pending_dashboard()
        self.select_payment_method(IDS.SelectPaymentMethod.knet_option_button)
        self.enter_amount()
        if not self.knet_screen():
            WireTransferFlow(self.driver,self.email).test_initial_deposit_happy_path()
        else:
            self.AppiumGestures.return_to_pending_dashboard()
            self.APIs._activate_user(self.amount)
        
        try:self.AppiumGestures.click_element(IDS.PendingDashboard.do_it_later_button,6)
        except: print("Can't find go to dashboard")
        
        self.AppiumGestures.scrollDown_refresh()
        self.AppiumGestures.return_to_active_dashboard()
        

    def test_additional_deposit_happy_path(self):
        self.Report.change_flow("Additional deposit")

        self.active_dashboard()
        self.active_select_portfolio()
        self.select_payment_method(IDS.SelectPaymentMethod.knet_option_button)

        self.enter_amount()
        if not self.knet_screen():
            WireTransferFlow(self.driver,self.email).test_additional_deposit_happy_path()
        
        self.AppiumGestures.return_to_active_dashboard()
        
