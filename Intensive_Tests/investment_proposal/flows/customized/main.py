import json
from time import sleep
import traceback


from GesturesAndMotions import scrollDown, taponcoordinates
from Intensive_Tests.helpers import AndroidGestures, AppiumActions, Reporting
from Intensive_Tests.investment_proposal.config import IDS
from ManualReport import ReportResults
from .config import questionnaires,questionnaire_questions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CustomizedFlow():
    risk_score_target = 1
    driver = None

    def __init__(self, driver, risk_score_target,user_type):
        self.driver = driver
        self.risk_score_target = risk_score_target
        self.user_type=user_type
        self.ReportDriver=None
        self.old_risk_score_target=risk_score_target
        self.AndroidGestures=AndroidGestures(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
        self.Report=Reporting(self.driver,"customized")

    def _test_text(self,id,expected,report=True):
        text_element = self.AppiumGestures.wait_for_element(id)
        if text_element.text != expected:
            if report:self.Report.report_testcase(False,self.testcase,self.risk_score_target,text_element.text,expected) 
            return False 
        else:   return True

    def _navigate_to_first_question(self):
        while True:
            try:
                if (self._test_text(IDS.questionnaire.question,questionnaire_questions[1],report=False)):break
                else:self.AndroidGestures.BACK()
            except:
                self.AndroidGestures.BACK()
                print("Error in navigating to first question")
            sleep(0.5)



    def _navigate_to_investment_type(self):
        while True:
            try:
                if self.AppiumGestures._check_if_visible(IDS.investment_type_screen.etf_option):break
                else:self.AndroidGestures.BACK()
            except:
                print("Error in navigating to Investment type screen")


    def _select_option(self, value_index):
        option_element=self.AppiumGestures.wait_for_elements(IDS.questionnaire.select_option)
        option_element[value_index].click()


    def _fill_age_input(self, value):
        SamePage=True
        while SamePage==True:
            if SamePage==True:
                Title=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")))
                try:AgeField= self.driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/textInput")
                except:sleep(0.1)
                if Title.text ==  "What is your current age?":
                    AgeField.click()
                    sleep(2)
                    AgeField.send_keys(str(value))
                    sleep(1)
                    Keyboardshown=self.driver.is_keyboard_shown()
                    if Keyboardshown==True:                
                        taponcoordinates(self.driver,1262,2737)
                    else:
                        AgeField.click()
                
            A=self.driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")
            if A.text=="What is your monthly income (in USD)?":
                sleep(0.2)
                SamePage=False
                # print(Fore.GREEN+"\t"+Title.text +" is Successfull!!!"+Fore.RESET)
                # print("\t"+Title.text +" is Successfull!!!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
                break
            elif A.text=="What is your current age?":
                SamePage=True

            
            
    def _test_investment_proposal_text_risk_score(self,mode="N/A"):
    
        self.testcase="Investment Proposal"
        try:    self.AppiumGestures.wait_for_element(IDS.investment_proposal_screen.description)
        except: self.AppiumGestures.wait_for_element(IDS.investment_proposal_screen.expand_description_button).click()
        sleep(1)
        
        if self.user_type.lower() == "etf":
            A=self._test_text(IDS.investment_proposal_screen.title,investment_proposal_etf[self.old_risk_score_target][0]["title"])
            B=self._test_text(IDS.investment_proposal_screen.description,investment_proposal_etf[self.old_risk_score_target][0]["description"])
            C=self._test_text(IDS.investment_proposal_screen.risk_score_text,investment_proposal_etf[self.risk_score_target][0]["risk_score_text"])
            if A and B and C:   self.Report.report_testcase(True,self.testcase,self.risk_score_target)


    def _handle_investment_proposal_loading(self):
        self._handle_loading()
        while True:
            if not self.AppiumGestures._check_if_visible(IDS.investment_proposal_screen.percentages_texts): break
            else:   sleep(0.3)



    def _handle_loading(self):  
         
        while True:
            if not self.AppiumGestures._check_if_visible(IDS.Loading.Dots,3): break
            else:   sleep(0.3)

        
    
    
    def _test_risk_increment(self):
        
        self.AppiumGestures.wait_for_element(IDS.investment_proposal_screen.risk_score_increase).click()
        sleep(2.3)
        
        if self.risk_score_target <10 :self.risk_score_target=self.risk_score_target+1
        self._test_investment_proposal_text_risk_score("increment")
        self._historical_performance_percentages()
        

    def _test_recommended_risk(self):
        self._test_investment_proposal_text_risk_score()
        self._historical_performance_percentages()

        
    def _test_risk_decrement(self):
        
        self.AppiumGestures.wait_for_element(IDS.investment_proposal_screen.risk_score_decrease).click()
        sleep(2.3)
        
        if self.risk_score_target >1: self.risk_score_target=self.risk_score_target-1
        self._test_investment_proposal_text_risk_score("decrement")
        self._historical_performance_percentages()



    def _check_islamic_availability(self):
        
        Islamic_tag=self.AppiumGestures.wait_for_element(IDS.investment_type_screen.islamic_tag)
        if Islamic_tag.text != "Not eligible":
            return True
        else:
            return False
                



    def _historical_performance_percentages(self):
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/percentageTextView")))
        self.testcase="Historical Performance"
        count=0
        status=True
        self.actual_percentages_list=[]
        sleep(1.5)
        self.percentages = self.driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/percentageTextView")
        for elem in self.percentages:
            self.actual_percentages_list.append(elem.text)

        if historical_performance_etf[self.risk_score_target]!= self.actual_percentages_list:
            self.Report.report_testcase(False,self.testcase,self.risk_score_target,self.actual_percentages_list,historical_performance_etf[self.risk_score_target])
        else:
            self.Report.report_testcase(True,self.testcase,self.risk_score_target)
        
        
    def _investment_type(self):
        
        status=True
        WebDriverWait(self.driver, 12).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/layoutInfo")))
        Buttons=self.driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/layoutInfo")
        
        if int(self.old_risk_score_target) <6:
            if self._check_islamic_availability():
                ReportResults(self.ReportDriver,self.driver,False,"\tIslamic Customized on risk score "+str(self.risk_score_target),"Islamic is enabled on risk score "+str(self.risk_score_target),"Islamic should be disabled on risk score "+str(self.risk_score_target))

            #Choosing Bank Transfer by default.
            WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/layoutInfo")))
            Buttons=self.driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/layoutInfo")
            Buttons[0].click()
        else:
            TagNames=self.driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTag")
            if TagNames[1].text == "Not eligible":
                ReportResults(self.ReportDriver,self.driver,False,"\tIslamic Customized on risk score "+str(self.risk_score_target),"Islamic is disabled on risk score "+str(self.risk_score_target),"Islamic should be enabled on risk score "+str(self.risk_score_target))
                status=False
                
            if self.user_type == "etf":
                Buttons[0].click()
            elif self.user_type == "islamic":
                Buttons[1].click()  
                try:self._pop_up_handling()
                except:
                    ReportResults(self.ReportDriver,self.driver,False,"\tIslamic Customized on risk score "+str(self.risk_score_target),"Islamic popup on risk score "+str(self.risk_score_target),"Islamic ppop up should be shown on risk score "+str(self.risk_score_target))
                    status=False
            
                    
        try:self.driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnContinue").click()
        except:
            scrollDown(self.driver,500, 2200, 500, 700)
            self.driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnContinue").click()                    
        if status:ReportResults(self.ReportDriver,self.driver,True,"\tInestment Type Screen on risk score "+str(self.risk_score_target))
            
    def _pop_up_handling(self):
        Continue=WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/btnContinue")))
        SelectAnotherPlan=self.driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvSelectPlan")
        Continue.click()
        
        
    def start(self):
        for question in questionnaires[self.risk_score_target]:
            if(question['type'] == 'select'):
                self._select_option(question['value'])
            if (question['type'] == 'input'):
                self._fill_age_input(question['value'])
        self._investment_type()

    def start_happy_path(self,detailed=False):
        for question in questionnaires[self.risk_score_target]:
            if(question['type'] == 'select'):
                self._select_option(question['value'])
            if (question['type'] == 'input'):
                self._fill_age_input(question['value'])
        # self._investment_type()
        # self._test_recommended_risk()
        # self.AppiumGestures.click_element(IDS.investment_proposal_screen.start_investing_button)

    def start_intensive_tests(self):
        for risk_score in range(1,11):
            self.risk_score_target=risk_score
            self.old_risk_score_target=risk_score

            print("\n\nRecommended Risk:  "+str(self.old_risk_score_target))
            print("\n\nRecommended Risk:  "+str(self.old_risk_score_target),file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

            self.start()
            
            self._test_recommended_risk()
            self._test_risk_increment()
            self._test_risk_decrement()
            
            self._navigate_to_first_question()


            
            
                    
