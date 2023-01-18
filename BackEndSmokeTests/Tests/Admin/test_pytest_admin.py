

import SystemPath

import inspect
import json
import sys
import pytest
import requests
import curlify
sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests")
from BackendVariables import ConstantVariables


Variables=ConstantVariables()

@pytest.mark.order(0)
def test_setup_method():
    url = "https://auth.staging-nbksmartwealth.com/oauth/token"
    payload = json.dumps({"username": "roy.braish+admin@neo.ae",
                        "password": "Password123",
                        "audience": "https://staging-nbksmartwealth.eu.auth0.com/api/v2/",
                        "grant_type": "http://auth0.com/oauth/grant-type/password-realm",
                        "scope": "openid email",
                        "realm": "Username-Password-Authentication",
                        "client_id": "QpVWZklsV9I7hDBfhDVW6PMGRtG9pNs6"
                        })
    response = requests.request("POST", url, headers=Variables.header_Cookie, data=payload)
    a=response.json()
    Variables.AdminAuthorization="Bearer "+a["access_token"]
        

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json", "r")
    json_object = json.load(a_file)
    # print(json_object)
    
    Variables.Email=json_object["Email"] 
    Variables.UserType = json_object["user_type"] 
    Variables.User_id=json_object["user_id"] 
    Variables.MobileNumber=json_object["mobile_number"] 
    Variables.CivilIDNumber=json_object["civil_id"] 
    Variables.iban=json_object["iban"] 
    Variables.original_risk_score=json_object["original_risk_score"]
    Variables.modified_risk_score=json_object["modified_risk_score"]


    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json", "r")
    JSON = json.load(a_file)
    a_file.close()
    # print(json_object)
    
    JSON["admin_authorization"] = Variables.AdminAuthorization


    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json", "w")
    json.dump(JSON, a_file)
    a_file.close()



class Test_Admin_user_profile():


    def setup_method(self):
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json") as file:
        # Load its content and make a new dictionary
            JSON=json.load(file)
        Variables.AdminAuthorization=JSON["admin_authorization"]
        Variables.SW_UAT_URL="https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/"
        self.headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Authorization': Variables.AdminAuthorization,
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

    def test_user_info(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/info"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_user_summary(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/summary"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202




    def test_user_status(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/status"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202



    def test_user_kyc_cid_status(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/project-connect/%s/kyc-cid-status"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_user_notes(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/notes"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_user_bank(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/bank"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_user_steps(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/steps"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_user_portfolios_investment_type_etf(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/portfolios?investment_type=etf"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_user_portfolios_investment_type_mmf(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/portfolios?investment_type=mmf"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_user_funds(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/funds"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_user_deposits(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/deposits"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202



    def test_user_withdrawals(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/withdrawals"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_user_banks(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/banks"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_user_rm(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/rm/user/"+str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_user_address(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/address"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_user_rm_list(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/rm?user_filter_type=all"
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202



class Test_Risk_Engine():


    def setup_method(self):
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json") as file:
        # Load its content and make a new dictionary
            JSON=json.load(file)
        Variables.AdminAuthorization=JSON["admin_authorization"]
        Variables.SW_UAT_URL="https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/"
        self.headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Authorization': Variables.AdminAuthorization,
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

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/project-connect/risk-engine/%s/paci"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_user_world_check(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/project-connect/risk-engine/%s/world-check"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_user_kyc(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/kyc"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_user_pep(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/project-connect/risk-engine/%s/pep"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_user_countries(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/project-connect/risk-engine/%s/countries"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_user_employment(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/project-connect/risk-engine/%s/employment"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_user_kyc_2(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url = Variables.SW_UAT_URL+"admin/profile/%s/kyc"%str(Variables.User_id)
        response = requests.request("GET", url, headers=self.headers)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202



