import inspect
import json
import sys
sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests")

import pytest
from BackendVariables import ConstantVariables
import SystemPath

import requests


import curlify

# global Variables
Variables=ConstantVariables()

# @pytest.mark.order(0)
def test_Environment(request):    
    func_name = (inspect.stack()[0][3]).replace("test_","")
    Variables.temp_test_case=str(func_name)
    
    Env=str(request.config.getoption("--env"))
    Variables.SelectEnvironment(Env)   
    Variables.temp_API_URL="Environment Specification"
    
    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    # print(json_object)
    
    json_object["SW_UAT_URL"] = Variables.SW_UAT_URL
    json_object["Environment"] = Env.upper()
    

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
            





class Test_PreSignUp_APIs(object):


    def setup_method(self):
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json") as file:
        # Load its content and make a new dictionary
            JSON=json.load(file)
        Variables.SW_UAT_URL=JSON["SW_UAT_URL"]
        

    def test_General_ETF_Products(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        
        url=Variables.SW_UAT_URL+"general/etf/products"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        print(Variables.SW_UAT_URL)
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
    def test_General_Islamic_Products(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url=Variables.SW_UAT_URL+"general/islamic/products"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
            
            
    def test_General_Bank_Funds(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url=Variables.SW_UAT_URL+"general/variables"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_General_Variables(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url=Variables.SW_UAT_URL+"general/variables"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202



class Test_InvestmentProposal(object):

    def setup_method(self):
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json") as file:
        # Load its content and make a new dictionary
            JSON=json.load(file)
        Variables.SW_UAT_URL=JSON["SW_UAT_URL"]


    def test_ETF_Risk1(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=1&investment_type=etf"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_ETF_Risk2(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=2&investment_type=etf"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        

    def test_ETF_Risk3(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)
        
        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=3&investment_type=etf"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
        

    def test_ETF_Risk4(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=4&investment_type=etf"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
        
        
    def test_ETF_Risk5(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=5&investment_type=etf"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
                
    def test_ETF_Risk6(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=6&investment_type=etf"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
                
    def test_ETF_Risk7(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=7&investment_type=etf"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
                
    def test_ETF_Risk8(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=8&investment_type=etf"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
                
    def test_ETF_Risk9(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=9&investment_type=etf"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
                
    def test_ETF_Risk10(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=10&investment_type=etf"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
    def test_Islamic_Risk1(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=1&investment_type=islamic"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_Islamic_Risk2(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=2&investment_type=islamic"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        

    def test_Islamic_Risk3(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=3&investment_type=islamic"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
        

    def test_Islamic_Risk4(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=4&investment_type=islamic"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==400 or response.status_code==401 or response.status_code==404
        
        
        
    def test_Islamic_Risk5(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=5&investment_type=islamic"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==400 or response.status_code==401 or response.status_code==404
        
                
    def test_Islamic_Risk6(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=6&investment_type=islamic"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==400 or response.status_code==401 or response.status_code==404
        
                
    def test_Islamic_Risk7(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=7&investment_type=islamic"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==400 or response.status_code==401 or response.status_code==404
        
                
    def test_Islamic_Risk8(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=8&investment_type=islamic"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==400 or response.status_code==401 or response.status_code==404
        
                
    def test_Islamic_Risk9(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=9&investment_type=islamic"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==400 or response.status_code==401 or response.status_code==404
        
                
    def test_Islamic_Risk10(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/history/performance?risk_score=10&investment_type=islamic"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==400 or response.status_code==401 or response.status_code==404
        
    

class Test_Onboarding_Portfolio_Options(object):
    
    def setup_method(self):
        Variables.temp_test_case="Onboarding_Portfolio_Options (SKIPPED: Islamic 2.1 is not Depoloyed!)"
        Variables.temp_API_URL="general/all/products?type=onboarding&score={risk_score}"
        Variables.temp_status_code=200
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json") as file:
        # Load its content and make a new dictionary
            global JSON
            JSON=json.load(file)
        Variables.SW_UAT_URL=JSON["SW_UAT_URL"]
        if not JSON["is_islamic2.1_enabled"]: pytest.skip("************ Islamic 2.1 is not deployed  ************")


    
    def test_Risk_1(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=onboarding&score=1"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]=="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE DISABLED (STATUS= INACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 
        
    
    def test_Risk_2(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=onboarding&score=2"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]=="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE DISABLED (STATUS= INACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 
        
        
    def test_Risk_3(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=onboarding&score=3"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]=="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE DISABLED (STATUS= INACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 

    def test_Risk_4(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=onboarding&score=4"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]=="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE DISABLED (STATUS= INACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 


    def test_Risk_5(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=onboarding&score=5"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]=="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE DISABLED (STATUS= INACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 


    def test_Risk_6(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=onboarding&score=6"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]!="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 


    def test_Risk_7(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=onboarding&score=7"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]!="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 




    def test_Risk_8(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=onboarding&score=8"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]!="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 




    def test_Risk_9(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=onboarding&score=9"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]!="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 



    def test_Risk_10(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=onboarding&score=10"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]!="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 




class Test_Active_Additional_Portfolio_Options(object):
    
    def setup_method(self):
        Variables.temp_test_case="Test_Active_Additional_Portfolio_Options (SKIPPED: Islamic 2.1 is not Depoloyed!)"
        Variables.temp_API_URL="general/all/products?type=active&score={risk_score}"
        Variables.temp_status_code=200
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json") as file:
        # Load its content and make a new dictionary
            global JSON
            JSON=json.load(file)
        Variables.SW_UAT_URL=JSON["SW_UAT_URL"]
        if not JSON["is_islamic2.1_enabled"]: pytest.skip("************ Islamic 2.1 is not deployed  ************")

    
    def test_Risk_1(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=active&score=1"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]=="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE DISABLED (STATUS= INACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 
        
    
    def test_Risk_2(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=active&score=2"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]=="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE DISABLED (STATUS= INACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 
        
        
    def test_Risk_3(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=active&score=3"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]=="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE DISABLED (STATUS= INACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 

    def test_Risk_4(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=active&score=4"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]=="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE DISABLED (STATUS= INACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 


    def test_Risk_5(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=active&score=5"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]=="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE DISABLED (STATUS= INACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 


    def test_Risk_6(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=active&score=6"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]!="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 


    def test_Risk_7(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=active&score=7"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]!="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 




    def test_Risk_8(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=active&score=8"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]!="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 




    def test_Risk_9(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=active&score=9"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]!="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 



    def test_Risk_10(self):
                
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class ::"+str(func_name)

        url=Variables.SW_UAT_URL+"general/all/products?type=active&score=10"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        a=response.json()
        for Section in a["meta"]["investment_products"]:
            if Section["id"]=="global_multi_asset" and Section["state"]!="active":
                pytest.fail("*********************************** ETF SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]=="global_multi_asset_islamic" and Section["state"]!="active":
                pytest.fail("*********************************** ISLAMIC SHOULD BE ENABLED (STATUS= ACTIVE)  ***********************************") 
            elif Section["id"]!="global_multi_asset_islamic" and Section["id"]!="global_multi_asset" and Section["state"]=="active":
                pytest.fail("*********************************** ONLY ETF AND ISLAMIC SHOULD BE ENABLED  ***********************************") 


