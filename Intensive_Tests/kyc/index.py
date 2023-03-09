

from Intensive_Tests.kyc.flows.personal_info.main import PersonalInfo


class KYC:
    def __init__(self,driver,email):

        self.driver = driver
        self.email = email
    
    def start(self):
        PersonalInfo(self.driver).start_happy_path()