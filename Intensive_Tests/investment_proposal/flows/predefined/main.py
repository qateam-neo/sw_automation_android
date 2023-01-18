from Intensive_Tests.helpers import AndroidGestures, AppiumActions, Reporting
from Intensive_Tests.investment_proposal.config import IDS
from Intensive_Tests.investment_proposal.flows.predefined.config import Localization_Predefined
from ...enums import PredefinedEnums


class PredefinedFlow():
    driver = None
    predefined_option = PredefinedEnums.BALANCED

    def __init__(self, driver, predefined_option,user_type):
        self.driver = driver
        self.risk_score_target = predefined_option
        self.user_type=user_type
        self.ReportDriver=None
        
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"predefined")
        
        
    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.wait_for_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,text_element.text,expected) 
            return False 
        else:   return True

    def _choose_predefined_option(self):
        if self.risk_score_target ==3: self.AppiumGestures.click_element(IDS.predefined_options_screen.conservative_button)
        elif self.risk_score_target ==5: self.AppiumGestures.click_element(IDS.predefined_options_screen.balanced_button)
        elif self.risk_score_target ==7: self.AppiumGestures.click_element(IDS.predefined_options_screen.growth_button)
        else: self.AppiumGestures.click_element(IDS.predefined_options_screen.balanced_button)
        self.AppiumGestures.click_element(IDS.predefined_options_screen.continue_button)

    def predefined_scores_screen(self,detailed=True):
        
        self.testcase="Predefined risk scores screen"
        
        self.AppiumGestures._check_if_visible(IDS.predefined_options_screen.not_sure_button)
        if detailed:
            self._test_text(IDS.predefined_options_screen.title,Localization_Predefined.predefined_options_screen.title)
            self._test_text(IDS.predefined_options_screen.conservative_title,Localization_Predefined.predefined_options_screen.conservative_title)
            self._test_text(IDS.predefined_options_screen.conservative_description,Localization_Predefined.predefined_options_screen.conservative_description)
            self._test_text(IDS.predefined_options_screen.balanced_title,Localization_Predefined.predefined_options_screen.balanced_title)
            self._test_text(IDS.predefined_options_screen.balanced_description,Localization_Predefined.predefined_options_screen.balanced_description)
            self._test_text(IDS.predefined_options_screen.growth_title,Localization_Predefined.predefined_options_screen.growth_title)
            self._test_text(IDS.predefined_options_screen.growth_description,Localization_Predefined.predefined_options_screen.growth_description)
            self._test_text(IDS.predefined_options_screen.not_sure_button,Localization_Predefined.predefined_options_screen.not_sure_button)
            self._test_text(IDS.predefined_options_screen.continue_button,Localization_Predefined.predefined_options_screen.continue_button)
            
        self._choose_predefined_option()
        
    def start_happy_path(self,detailed=True):
        self.predefined_scores_screen(detailed)
        
        