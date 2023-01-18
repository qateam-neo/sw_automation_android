from datetime import datetime
import json


import random
# from test_pytest_specific_scenarios import Variables

from Platform_OS import getplatform_OS
global MobileNumber,CivilID
Mobile="59"+str(random.randint(100000,999999))
CID=random.randint(100000000000,999999999999)

#TODO: FIXME: 
#TODO: FIXME:   Set After functin to save variables, status code, print response: Response, CURL: ... 
#TODO: FIXME: 
#TODO: FIXME: 


class ConstantVariables():
    def __init__(self) :
        
        self.laptop_platform=getplatform_OS()
        if self.laptop_platform =="windows":
            self.CivilID={'file': open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\TEST.pdf', 'rb')}

        elif self.laptop_platform=="mac":
            self.CivilID=""
    
    def SelectEnvironment(self,environment):
        self.Environment=environment
        if "internal" in self.Environment.lower():
            self.SW_UAT_URL="https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/"        
        elif "uat" in self.Environment.lower():    
            self.SW_UAT_URL="https://api.nbkcapital-smartwealth.com/api/v2/"
        else:
            self.SW_UAT_URL="https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/"  
            
        self.Auth0_domain="https://auth.staging-nbksmartwealth.com/"
      
    
    def SetEmail(self,Email):
        self.Email = Email
    x_platorm= "android"
    
    UserType="etf"
    User_id=""
    Bank="al_ahli"
    MobileNumber=str(Mobile)
    MobileNumberOTP=""
    CivilIDNumber=str(CID)
    civil_id_serial="1234567899"
    iban=""
    
    withdrawal_otp=""
    withdrawal_id=""
    
    additional_islamic_portfolio_id=""    
    additional_islamic_withdrawal_otp=""
    additional_etf_portfolio_id=""
    additional_etf_withdrawal_otp=""

    original_risk_score=str(7)
    modified_risk_score=str(3)

    temp_test_case=""
    temp_API_URL="www.google.com"
    # Email="roy.braish+testisbackend@neo.ae"
    Email="tala.gebran+test19@neo.ae"

    Authorization=""
    AdminAuthorization=''
    Auth0_UserID=""
    
    
    header1={"Authorization": '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'}
    header_NoAuthorization={'Content-Type': 'application/json' , 'x-locale': 'en_US' , 'x-version': '1.0' , 'x-platform': x_platorm}
    header_Authorization={'Content-Type': 'application/json' , 'x-locale': 'en_US' , 'x-version': '1.0' , 'x-platform': x_platorm ,"Authorization":""}
    header_Cookie={'X-Platform': 'android' , 'X-locale': 'en_US' , 'X-version': '1.0' , 'Content-Type': 'application/json' , 'Cookie': 'did=s%3Av0%3A6493fda0-91f8-11ec-bd24-23d965feca4f.YKRF%2BNhTSyAOJufKB2VSnGEc%2B5cnjmJO1Kvd6NagNTo; did_compat=s%3Av0%3A6493fda0-91f8-11ec-bd24-23d965feca4f.YKRF%2BNhTSyAOJufKB2VSnGEc%2B5cnjmJO1Kvd6NagNTo'}
    
    temp_status_code="default"
    
    
