
from Intensive_Tests.deposits.config import IDS, KNET_Credentials, Localization_deposits, TransferRules
from Intensive_Tests.deposits.flows.wire_transfer.main import WireTransferFlow
from Intensive_Tests.enums import limits
from Intensive_Tests.helpers import APIS, AndroidGestures, AppiumActions, Random_values, Reporting
from .config import   Localization_KNET



class DirectDebitFlow():
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

