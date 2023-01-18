


import inspect
import json

import requests
from GetProfileAPIReturnID import GetProfileAPIReturnID

from GetTokenAPI import GetTokenAPI
import curlify

class RiskEngine_API():
    
    
    
    def __init__(self,AdminAuthorization="N/A",User_ID="N/A",Email="N/A") :
        if User_ID == "N/A" and Email=="N/A" :
            with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
                JSON=json.load(file)
            self.User_ID =JSON["TechnicalVariables"]["User_ID"]
        elif User_ID == "N/A" and Email !="N/A":
            Auth=GetTokenAPI(Email)
            self.User_ID=GetProfileAPIReturnID(Auth,None,Email,"Password123")
        elif User_ID != "N/A" and Email =="N/A":
            self.User_ID=User_ID
        if AdminAuthorization != "N/A":
            self.AdminAuthorization = str(AdminAuthorization)
        self.SW_UAT_URL="https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/"
        # print(self.AdminAuthorization)
        # print(self.User_ID)
        
    def setheader(self):
        self.headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Authorization': self.AdminAuthorization,
                    'Connection': 'keep-alive',
                    'ContentType': 'application/json',
                    'Origin': 'https://admin.nbkcapital-smartwealth.com',
                    'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                    'X-Locale': 'en_US',
                    'X-Platform': 'web',
                    'X-Version': '2.0',
                    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"'
                    }
        
        
    def test_user_paci(self):

        url = self.SW_UAT_URL+"admin/project-connect/risk-engine/%s/paci"%str(self.User_ID)
        response = requests.request("GET", url, headers=self.headers)

        r=response.text
        return r


    def test_user_world_check(self):


        url = self.SW_UAT_URL+"admin/project-connect/risk-engine/%s/world-check"%str(self.User_ID)
        response = requests.request("GET", url, headers=self.headers)

        r=response.text
        return r


    def test_user_kyc(self):


        url = self.SW_UAT_URL+"admin/profile/%s/kyc"%str(self.User_ID)
        response = requests.request("GET", url, headers=self.headers)

        r=response.text
        return r


    def test_user_pep(self):


        url = self.SW_UAT_URL+"admin/project-connect/risk-engine/%s/pep"%str(self.User_ID)
        response = requests.request("GET", url, headers=self.headers)

        r=response.text
        return r

    def test_user_countries(self):


        url = self.SW_UAT_URL+"admin/project-connect/risk-engine/%s/countries"%str(self.User_ID)
        response = requests.request("GET", url, headers=self.headers)

        r=response.text
        return r


    def test_user_employment(self):


        url = self.SW_UAT_URL+"admin/project-connect/risk-engine/%s/employment"%str(self.User_ID)
        response = requests.request("GET", url, headers=self.headers)

        r=response.text
        return r


    def test_user_kyc_2(self):


        url = self.SW_UAT_URL+"admin/profile/%s/kyc"%str(self.User_ID)
        response = requests.request("GET", url, headers=self.headers)

        r=response.text
        return r



