from Intensive_Tests import helpers
from Intensive_Tests.config import Application_screens
from Intensive_Tests.helpers import AndroidGestures, AppiumActions, ApplicationHelpers, Reporting
from Intensive_Tests.pending_dashboard.config import IDS
from Intensive_Tests.pending_dashboard.flows.kyc.config import Localization_pending_dashboard_kyc


class pending_dashboard_kyc():
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.testcase="Pending Dashboard KYC"

        
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"Pending Dashboard KYC")
        self.helpers=ApplicationHelpers(driver)
    
        
    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.wait_for_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,text_element.text,expected) 
            return False 
        else:   return True
    
    def _ids_uploaded(self):
        progress=self.AppiumGestures.get_elements(IDS.time_id)
        if len(progress) == 3:
            self.Report.report_testcase(False,self.testcase,"N/A","IDs should be uploaded","IDs are not uploaded")
        elif len(progress) == 2:
            return True
        elif len(progress) == 1:
            self.Report.report_testcase(False,self.testcase,"N/A","KYC shouldn't be filled","KYC is already filled and contract is signed")

            
    def proceed_flow(self):
        self.AppiumGestures.click_element(IDS.kyc_button)


        
    def start_happy_path(self,detailed=True):
        self._ids_uploaded()
        self.helpers.test_screen_localization(Application_screens.Personal_info)
        self.proceed_flow()
        
        