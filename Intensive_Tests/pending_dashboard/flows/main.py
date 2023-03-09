
from selenium.webdriver.support.ui import WebDriverWait # needs to be used when creating a function everytime
from selenium.webdriver.support import expected_conditions # needs to be used when creating a function everytime
from selenium.webdriver.common.by import By
from Intensive_Tests.helpers import AppiumActions, Reporting

from Intensive_Tests.pending_dashboard.config import IDS
from Intensive_Tests.pending_dashboard.flows.kyc.main import pending_dashboard_kyc

class PendingDashboard :
    
    def __init__(self,driver):
        self.driver = driver
        self.ReportDriver=None
        self.Report=Reporting(self.driver,"Pending Dashboard")
        self.AppiumGestures=AppiumActions(self.driver)

    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.wait_for_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,text_element.text,expected) 
            return False 
        else:   return True
    
    def _check_which_flow(self):
        return len(self.AppiumGestures.wait_for_elements(IDS.time_id))

    def start(self,detailed=True):
        flow=self._check_which_flow()
        
        if flow==2: pending_dashboard_kyc(self.driver).start_happy_path(True)
