
from Intensive_Tests.deposits.config import IDS, Localization_deposits, TransferRules
from Intensive_Tests.deposits.flows.knet.main import KNETFlow
from Intensive_Tests.deposits.flows.wire_transfer.main import WireTransferFlow
from Intensive_Tests.enums import limits
from Intensive_Tests.helpers import APIS, AndroidGestures, AppiumActions, Random_values, Reporting



class Deposit:
    def __init__(self,driver,email):
        self.WIRE=self.wire(driver,email)
        self.KNET=self.knet(driver,email)

        self.driver = driver
        self.email = email
        
    
    
    class wire:
        def __init__(self,driver,email):
            self.driver=driver
            self.email=email
            self.Deposit_bank_transfer=WireTransferFlow(self.driver, self.email)

        
        def initial_deposit(self):
            self.Deposit_bank_transfer.test_initial_deposit_happy_path()

        def additional_deposit(self):
            self.Deposit_bank_transfer.test_additional_deposit_happy_path()
    
    class knet:
        def __init__(self,driver,email) :
            self.driver=driver
            self.email=email
            self.Deposit_knet=KNETFlow(self.driver, self.email)
            
        def initial_deposit(self):
            self.Deposit_knet.test_initial_deposit_happy_path()
        
        def additional_deposit(self):
            self.Deposit_knet.test_additional_deposit_happy_path()
    
        
    
    
    # class KNET:
    #     def __init__(self,driver,email):

