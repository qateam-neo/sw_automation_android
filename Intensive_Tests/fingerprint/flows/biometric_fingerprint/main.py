
from Intensive_Tests.fingerprint.config import IDS, Localization_fingerprint
from Intensive_Tests.enums import limits
from Intensive_Tests.helpers import APIS, AndroidGestures, AppiumActions, Random_values, Reporting



class Biometric_fingerprint():
    risk_score_target = 1
    driver = None

    def __init__(self, driver, email):
        self.driver = driver
        self.email = email
        self.risk_score_target="N/A"
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"Fingerprint")
        self.APIs=APIS(self.driver,self.email)
        self.testcase="Fingerprint"
        
    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.get_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,text_element.text,expected) 
            return False 
        else:   return True

    def test_biometric_fingerprint_screen(self,detailed=True):
        self.AppiumGestures._check_if_visible(IDS.fingerprint_screen.enable_button)
        if detailed:
            self._test_text(IDS.fingerprint_screen.title,Localization_fingerprint.title)
            self._test_text(IDS.fingerprint_screen.description,Localization_fingerprint.description)
            self._test_text(IDS.fingerprint_screen.enable_button,Localization_fingerprint.enable_button)
        self.AndroidGestures.BACK()
        
    def start_happy_path(self,detailed=True):
        if self.AppiumGestures._check_if_visible(IDS.fingerprint_screen.enable_button,10):
            self.test_biometric_fingerprint_screen(False)
        else:
            self.Report.report_testcase_not_shown(self.testcase)
                            