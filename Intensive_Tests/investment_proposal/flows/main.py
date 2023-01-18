from time import sleep
from Intensive_Tests.helpers import APIS, AndroidGestures, AppiumActions, Reporting
from Intensive_Tests.investment_proposal.config import IDS, Localization_Onboarding,Investment_Proposal_Info
from Intensive_Tests.investment_proposal.enums import PredefinedEnums
from Intensive_Tests.investment_proposal.flows.predefined.main import PredefinedFlow


class Onboarding :
    
    def __init__(self,driver,user_type):
        self.driver = driver
        self.user_type = user_type.lower()
        self.ReportDriver=None
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"Onboarding")

    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.wait_for_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,text_element.text,expected) 
            return False 
        else:   return True
    
    def compare_lists(self,list1,list2,report=True):
        if list1!=list2:
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,list1,list2) 
            return False 
        else:   return True
                
    def _islamic_popup(self,detailed=True):
        self.testcase="Islamic popup"
        
        self.AppiumGestures._check_if_visible(IDS.islamic_popup.description)
        if detailed: 
            self._test_text(IDS.islamic_popup.description,Localization_Onboarding.islamic_popup.description)
            self._test_text(IDS.islamic_popup.continue_button,Localization_Onboarding.islamic_popup.continue_button)
            self._test_text(IDS.islamic_popup.select_another_plan_button,Localization_Onboarding.islamic_popup.select_another_plan_button)
        self.AppiumGestures.click_element(IDS.islamic_popup.continue_button)

    def _analyze_investment_type_eligibility(self,report=True):
        if self._test_text(IDS.investment_type_screen.etf_tag,Localization_Onboarding.investment_type_screen.not_eligible_tag,False):
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,"ETF should be enabled","ETF Shows tag not eligble")
        if self.risk_score_target<6 and not self._test_text(IDS.investment_type_screen.islamic_tag,Localization_Onboarding.investment_type_screen.not_eligible_tag,False):
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,"Islamic should be disabled","islamic is enabled")
        if self.risk_score_target>=6 and self._test_text(IDS.investment_type_screen.islamic_tag,Localization_Onboarding.investment_type_screen.not_eligible_tag,False):
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,"Islamic should be enabled","islamic is disabled")

    def _choose_user_type(self):
        if "etf" in self.user_type:
            self.AppiumGestures.click_element(IDS.investment_type_screen.etf_option)
            self.AppiumGestures.click_element(IDS.investment_type_screen.Continue)
        elif "islamic" in self.user_type:
            self.AppiumGestures.click_element(IDS.investment_type_screen.islamic_option)
            self.AppiumGestures.click_element(IDS.investment_type_screen.Continue)
            self._islamic_popup()
        
        
    def _choose_onboarding_flow(self):
        if "predefined" in self.onboarding_flow:
            self.AppiumGestures.click_element(IDS.how_would_you_like_to_get_started_screen.predefined_button)
        elif "customized" in self.onboarding_flow:
            self.AppiumGestures.click_element(IDS.how_would_you_like_to_get_started_screen.customized_button)
        self.AppiumGestures.click_element(IDS.how_would_you_like_to_get_started_screen.continue_button)
        
    def _handle_loading(self):  
        while True:
            if not self.AppiumGestures._check_if_visible(IDS.Loading.Dots,3): break
            else:  sleep(0.3)
            
            
    def _handle_investment_proposal_loading(self):
        self._handle_loading()
        while True:
            if not self.AppiumGestures._check_if_visible(IDS.investment_proposal_screen.percentages_texts): break
            else:   sleep(0.3)
        
    def _get_historical_titles_list(self):
        self.actual_titles_list=[]
        self.percentages = self.AppiumGestures.wait_for_elements(IDS.investment_proposal_screen.percentages_texts)
        for elem in self.percentages:
            self.actual_titles_list.append(elem.text)
        return self.actual_titles_list

    def _get_historical_percentages_list(self):
        self.actual_percentages_list=[]
        self.percentages = self.AppiumGestures.wait_for_elements(IDS.investment_proposal_screen.percentages)
        for elem in self.percentages:
            self.actual_percentages_list.append(elem.text)
        return self.actual_percentages_list
       

    def _test_InvProp_text(self):
        if "etf" in self.user_type and "predefined" in self.onboarding_flow: 
            INVESTMENT_PROPOSAL_LOCALIZATION=Investment_Proposal_Info.Predefined.ETF
            HISTORICAL_PERFORMANCE_PERCENTAGES=Investment_Proposal_Info.Historical_Performance.ETF.percentages[self.risk_score_target]
            HISTORICAL_PERFORMANCE_TITLES=Investment_Proposal_Info.Historical_Performance.ETF.titles

        elif "etf" in self.user_type and "customized" in self.onboarding_flow: 
            INVESTMENT_PROPOSAL_LOCALIZATION=Investment_Proposal_Info.Customized.ETF
            HISTORICAL_PERFORMANCE_PERCENTAGES=Investment_Proposal_Info.Historical_Performance.ETF.percentages[self.risk_score_target]
            HISTORICAL_PERFORMANCE_TITLES=Investment_Proposal_Info.Historical_Performance.ETF.titles

        elif "islamic" in self.user_type and "predefined" in self.onboarding_flow: 
            INVESTMENT_PROPOSAL_LOCALIZATION=Investment_Proposal_Info.Predefined.ISLAMIC
            HISTORICAL_PERFORMANCE_PERCENTAGES=Investment_Proposal_Info.Historical_Performance.ISLAMIC.percentages[self.risk_score_target]
            HISTORICAL_PERFORMANCE_TITLES=Investment_Proposal_Info.Historical_Performance.ISLAMIC.titles

        elif "islamic" in self.user_type and "customized" in self.onboarding_flow: 
            INVESTMENT_PROPOSAL_LOCALIZATION=Investment_Proposal_Info.Customized.ISLAMIC
            HISTORICAL_PERFORMANCE_PERCENTAGES=Investment_Proposal_Info.Historical_Performance.ISLAMIC.percentages[self.risk_score_target]
            HISTORICAL_PERFORMANCE_TITLES=Investment_Proposal_Info.Historical_Performance.ISLAMIC.titles
            
        if not self.AppiumGestures._check_if_visible(IDS.investment_proposal_screen.description):
            self.AppiumGestures.click_element(IDS.investment_proposal_screen.expand_description_button)
            self.AppiumGestures._check_if_visible(IDS.investment_proposal_screen.description,6)

        self._test_text(IDS.investment_proposal_screen.title,INVESTMENT_PROPOSAL_LOCALIZATION.get_title(self.risk_score_target))
        self._test_text(IDS.investment_proposal_screen.description,INVESTMENT_PROPOSAL_LOCALIZATION.get_description(self.risk_score_target))
        self._test_text(IDS.investment_proposal_screen.risk_score_text,INVESTMENT_PROPOSAL_LOCALIZATION.get_risk_score_text(self.risk_score_target))
        self.compare_lists(self._get_historical_titles_list(),HISTORICAL_PERFORMANCE_TITLES)
        self.compare_lists(self._get_historical_percentages_list(),HISTORICAL_PERFORMANCE_PERCENTAGES)

        
        
    """
    START WRITING THE MAIN TESTS HERE: (SCREENS)
    
    """
    
    def test_get_started_screen(self,detailed=True):
        self.testcase="Get started screen"
        
        self.AppiumGestures._check_if_visible(IDS.GetStartedScreen.login_button)
        if detailed:
            self._test_text(IDS.GetStartedScreen.title,Localization_Onboarding.GetStartedScreen.title)
            self._test_text(IDS.GetStartedScreen.description,Localization_Onboarding.GetStartedScreen.description)
            self._test_text(IDS.GetStartedScreen.get_started_button,Localization_Onboarding.GetStartedScreen.get_started_button)
            self._test_text(IDS.GetStartedScreen.login_button,Localization_Onboarding.GetStartedScreen.login_button)
            self._test_text(IDS.GetStartedScreen.change_language_button,Localization_Onboarding.GetStartedScreen.change_language_button)
        self.AppiumGestures.click_element(IDS.GetStartedScreen.get_started_button)
        
        
    def test_how_would_you_like_to_get_started_screen(self,detailed=True):
        self.testcase="How would you like to get started screen"

        self.AppiumGestures._check_if_visible(IDS.how_would_you_like_to_get_started_screen.title)
        if detailed:
            self._test_text(IDS.how_would_you_like_to_get_started_screen.title,Localization_Onboarding.how_would_you_like_to_get_started_screen.title)
            self._test_text(IDS.how_would_you_like_to_get_started_screen.description,Localization_Onboarding.how_would_you_like_to_get_started_screen.description)
            self._test_text(IDS.how_would_you_like_to_get_started_screen.customized_title,Localization_Onboarding.how_would_you_like_to_get_started_screen.customized_title)
            self._test_text(IDS.how_would_you_like_to_get_started_screen.customized_description,Localization_Onboarding.how_would_you_like_to_get_started_screen.customized_description)
            self._test_text(IDS.how_would_you_like_to_get_started_screen.predefined_title,Localization_Onboarding.how_would_you_like_to_get_started_screen.predefined_title)
            self._test_text(IDS.how_would_you_like_to_get_started_screen.predefined_description,Localization_Onboarding.how_would_you_like_to_get_started_screen.predefined_description)
            
        self._choose_onboarding_flow()
        
        
    def test_investment_type_screen(self,detailed=True,user_type=None,risk_score_target=None):
        self.testcase="Investment type screen"      
          
        if user_type is not None: self.user_type=user_type
        if risk_score_target is not None: self.risk_score_target=risk_score_target

        self.AppiumGestures._check_if_visible(IDS.investment_type_screen.etf_tag)
        
        if detailed:
            self._test_text(IDS.investment_type_screen.title,Localization_Onboarding.investment_type_screen.title)
            self._test_text(IDS.investment_type_screen.description,Localization_Onboarding.investment_type_screen.description)
            self._test_text(IDS.investment_type_screen.etf_title,Localization_Onboarding.investment_type_screen.etf_title)
            self._test_text(IDS.investment_type_screen.etf_description,Localization_Onboarding.investment_type_screen.etf_description)
            self._test_text(IDS.investment_type_screen.islamic_title,Localization_Onboarding.investment_type_screen.islamic_title)
            self._test_text(IDS.investment_type_screen.islamic_description,Localization_Onboarding.investment_type_screen.islamic_description)

        self._analyze_investment_type_eligibility()
        self._choose_user_type()
        
        
    def test_investment_proposal_screen(self,detailed=True):
        self.AppiumGestures._check_if_visible(IDS.investment_proposal_screen.start_investing_button,8)
        if detailed:self._test_InvProp_text()
        self.AppiumGestures.click_element(IDS.investment_proposal_screen.start_investing_button)



    def start_predefined_happy_path(self,predefined_option,detailed=True):
        """
        ::predefined_option: PredefinedEnums.Conservative,PredefinedEnums.Balanced,PredefinedEnums.Growth
        """
        self.onboarding_flow="predefined"
        self.risk_score_target=predefined_option
        self.test_get_started_screen(False)
        self.test_how_would_you_like_to_get_started_screen(False)
        PredefinedFlow(self.driver,self.risk_score_target,self.user_type).start_happy_path(False)
        self.test_investment_type_screen(detailed=False)
        self.test_investment_proposal_screen(detailed=False)
        
            
