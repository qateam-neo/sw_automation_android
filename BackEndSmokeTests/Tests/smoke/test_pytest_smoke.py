from datetime import datetime
import inspect
import json
import os
import sys
from time import sleep
import curlify
# from SystemPathBackend import System_Path_Backend
sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests")
import SystemPath

# import pytest
from BackendVariables import ConstantVariables
# from GetProfileAPIReturnID import GetProfileAPIReturnID
import requests


Variables=ConstantVariables()



class Test_ConfigureTests(object):
    
    def test_Environment(self,request):
        

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        Env=str(request.config.getoption("--env"))
        Variables.SelectEnvironment(Env)   
    
        



    
    def test_GetEmailCount(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        Email=Variables.Email
        Prefix=[]
        for i in range(len(Email)-1,0,-1):
            if Email[i]=="@":
                for j in range(i-1,-1,-1):
                    if Email[j].isdigit():
                        # print("Skip Numbers")
                        sleep(0.1)
                    else:
                        Prefix.append(Email[j])
                i=(-3)

        Prefix.reverse()
        FullPrefix="".join(Prefix)

        if "+" in FullPrefix:
            url= Variables.SW_UAT_URL+"development/email-count?prefix="+FullPrefix
        headers = { 'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'   }
        response = requests.request("GET", url, headers=headers)
        
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url

        if response.status_code == 200 or response.status_code == "200" or response.status_code == "201" or response.status_code == 201:
            count = response.json()["count"]
            # print(count)
            Variables.SetEmail(FullPrefix+str(int(count)+1)+"@neo.ae")
            # Variables.SetEmail("tala.gebran+test19@neo.ae")
            pass
        else:assert False






class Test_GeneralAPIs(object):
    def test_BankFunds_Categories(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url=Variables.SW_UAT_URL+"general/bank-funds/categories"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
            
    def test_General_Variables(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
       
        url=Variables.SW_UAT_URL+"general/variables"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_Risk_Scores(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url=Variables.SW_UAT_URL+"risk/scores"
        response = requests.request("GET", url, headers=Variables.header_NoAuthorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    
######################################
    
#   Create user and Sign up
    
######################################


class Test_SignUp(object):
    
    def test_Auth0_SignUpAPI(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url=Variables.Auth0_domain+"dbconnections/signup"
        payload = json.dumps({"password": "Password123","connection": "Username-Password-Authentication","user_metadata": {"lang": "en"},"email": Variables.Email,"client_id": "QpVWZklsV9I7hDBfhDVW6PMGRtG9pNs6"})
        headers = {
        'auth0-client': 'eyJuYW1lIjoiQXV0aDAuQW5kcm9pZCIsInZlcnNpb24iOiIxLjE0LjEifQ==',
        'content-type': 'application/json; charset=utf-8',
        'host': 'auth.staging-nbksmartwealth.com',
        'connection': 'Keep-Alive',
        'Cookie': 'did=s%3Av0%3A6493fda0-91f8-11ec-bd24-23d965feca4f.YKRF%2BNhTSyAOJufKB2VSnGEc%2B5cnjmJO1Kvd6NagNTo; did_compat=s%3Av0%3A6493fda0-91f8-11ec-bd24-23d965feca4f.YKRF%2BNhTSyAOJufKB2VSnGEc%2B5cnjmJO1Kvd6NagNTo'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
        
    def test_PostBearerToken(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)    

        url = "https://auth.staging-nbksmartwealth.com/oauth/token"
        payload = json.dumps({"username": Variables.Email,
                            "password": "Password123",
                            "audience": "https://staging-nbksmartwealth.eu.auth0.com/api/v2/",
                            "grant_type": "http://auth0.com/oauth/grant-type/password-realm",
                            "scope": "openid email",
                            "realm": "Username-Password-Authentication",
                            "client_id": "QpVWZklsV9I7hDBfhDVW6PMGRtG9pNs6"
                            })
        response = requests.request("POST", url, headers=Variables.header_Cookie, data=payload)
        a=response.json()
        Variables.Authorization="Bearer "+a["access_token"]
        Variables.header_Authorization["Authorization"]=Variables.Authorization
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
    def test_PostAdminBearerToken(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)    

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
        
        
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        

    def test_Auth0_UserInfo(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = "https://auth.staging-nbksmartwealth.com/userinfo"
        headers = {
        'authorization': Variables.Authorization,
        'accept-language': 'en',
        'auth0-client': 'eyJuYW1lIjoiQXV0aDAuQW5kcm9pZCIsInZlcnNpb24iOiIxLjE0LjEifQ==',
        'host': 'auth.staging-nbksmartwealth.com',
        'connection': 'Keep-Alive',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/2.7.5',
        'x-postman-captr': '9804378',
        'Cookie': '__cf_bm=3PnvVowK2WQgTJbb52rPMyVXWPVqnSXXV4tYvomhBys-1667153148-0-ATXYQpY5D/IKVh+cJKGmMbIOO5e0cwkrte+C+k6cuFhVX0uffz7iSpdAdGZTNs/Icc7Q7sUU3gWWguBvF63ZtGU=; did=s%3Av0%3A6493fda0-91f8-11ec-bd24-23d965feca4f.YKRF%2BNhTSyAOJufKB2VSnGEc%2B5cnjmJO1Kvd6NagNTo; did_compat=s%3Av0%3A6493fda0-91f8-11ec-bd24-23d965feca4f.YKRF%2BNhTSyAOJufKB2VSnGEc%2B5cnjmJO1Kvd6NagNTo'
        }

        response = requests.request("GET", url, headers=headers)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_Post_Profile(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url=Variables.SW_UAT_URL+"profile"
        payload = json.dumps({  "email": Variables.Email,
                                "investment_type": Variables.UserType,
                                "language": "en",
                                "modified_risk_score": int(Variables.modified_risk_score),
                                "original_risk_score": int(Variables.original_risk_score)    })
        
        response = requests.request("POST", url, headers=Variables.header_Authorization,data=payload)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        



    def test_Get_Profile(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url=Variables.SW_UAT_URL+"profile"    
        response = requests.request("GET", url, headers=Variables.header_Authorization)
        a=response.json()
        Variables.Auth0_UserID=a["meta"]["auth0_id"]
        Variables.User_id=a["meta"]["id"]
        try:    Variables.iban=a["meta"]["iban_number"]
        except: pass
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json") as file:
        # Load its content and make a new dictionary
            JSON=json.load(file)
        JSON["Email"]=Variables.Email
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        


    def test_set_Language(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"profile"
        payload = json.dumps({"language": "en"})
        response = requests.request("PUT", url, headers=Variables.header_Authorization, data=payload)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


# ######################################
    
# #   Verify Email Address
# #   Upload IDs
    
# ######################################



class Test_VerifyEmail_UploadIDs(object):

    def test_verify_email(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url = "https://staging-nbksmartwealth.eu.auth0.com/api/v2/users/"+Variables.Auth0_UserID

        payload = json.dumps({
        "email": Variables.Email,
        "email_verified": True,
        "verify_email": True
        })
        headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1xcHNlck9mQzJyT0l6ZjhxMWdUTyJ9.eyJpc3MiOiJodHRwczovL3N0YWdpbmctbmJrc21hcnR3ZWFsdGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImdhbEtZWlJKbzZ1eUFsZ2ZYZEFZazdvVWRUMmk1cllGQGNsaWVudHMiLCJhdWQiOiJodHRwczovL3N0YWdpbmctbmJrc21hcnR3ZWFsdGguZXUuYXV0aDAuY29tL2FwaS92Mi8iLCJpYXQiOjE2Njc1NTA3NzMsImV4cCI6MTY3MDE0Mjc3MywiYXpwIjoiZ2FsS1laUkpvNnV5QWxnZlhkQVlrN29VZFQyaTVyWUYiLCJzY29wZSI6InJlYWQ6Y2xpZW50X2dyYW50cyBjcmVhdGU6Y2xpZW50X2dyYW50cyBkZWxldGU6Y2xpZW50X2dyYW50cyB1cGRhdGU6Y2xpZW50X2dyYW50cyByZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgY3JlYXRlOnVzZXJzIHJlYWQ6dXNlcnNfYXBwX21ldGFkYXRhIHVwZGF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgZGVsZXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBjcmVhdGU6dXNlcnNfYXBwX21ldGFkYXRhIGNyZWF0ZTp1c2VyX3RpY2tldHMgcmVhZDpjbGllbnRzIHVwZGF0ZTpjbGllbnRzIGRlbGV0ZTpjbGllbnRzIGNyZWF0ZTpjbGllbnRzIHJlYWQ6Y2xpZW50X2tleXMgdXBkYXRlOmNsaWVudF9rZXlzIGRlbGV0ZTpjbGllbnRfa2V5cyBjcmVhdGU6Y2xpZW50X2tleXMgcmVhZDpjb25uZWN0aW9ucyB1cGRhdGU6Y29ubmVjdGlvbnMgZGVsZXRlOmNvbm5lY3Rpb25zIGNyZWF0ZTpjb25uZWN0aW9ucyByZWFkOnJlc291cmNlX3NlcnZlcnMgdXBkYXRlOnJlc291cmNlX3NlcnZlcnMgZGVsZXRlOnJlc291cmNlX3NlcnZlcnMgY3JlYXRlOnJlc291cmNlX3NlcnZlcnMgcmVhZDpkZXZpY2VfY3JlZGVudGlhbHMgdXBkYXRlOmRldmljZV9jcmVkZW50aWFscyBkZWxldGU6ZGV2aWNlX2NyZWRlbnRpYWxzIGNyZWF0ZTpkZXZpY2VfY3JlZGVudGlhbHMgcmVhZDpydWxlcyB1cGRhdGU6cnVsZXMgZGVsZXRlOnJ1bGVzIGNyZWF0ZTpydWxlcyByZWFkOnJ1bGVzX2NvbmZpZ3MgdXBkYXRlOnJ1bGVzX2NvbmZpZ3MgZGVsZXRlOnJ1bGVzX2NvbmZpZ3MgcmVhZDplbWFpbF9wcm92aWRlciB1cGRhdGU6ZW1haWxfcHJvdmlkZXIgZGVsZXRlOmVtYWlsX3Byb3ZpZGVyIGNyZWF0ZTplbWFpbF9wcm92aWRlciBibGFja2xpc3Q6dG9rZW5zIHJlYWQ6c3RhdHMgcmVhZDp0ZW5hbnRfc2V0dGluZ3MgdXBkYXRlOnRlbmFudF9zZXR0aW5ncyByZWFkOmxvZ3MgcmVhZDpzaGllbGRzIGNyZWF0ZTpzaGllbGRzIGRlbGV0ZTpzaGllbGRzIHVwZGF0ZTp0cmlnZ2VycyByZWFkOnRyaWdnZXJzIHJlYWQ6Z3JhbnRzIGRlbGV0ZTpncmFudHMgcmVhZDpndWFyZGlhbl9mYWN0b3JzIHVwZGF0ZTpndWFyZGlhbl9mYWN0b3JzIHJlYWQ6Z3VhcmRpYW5fZW5yb2xsbWVudHMgZGVsZXRlOmd1YXJkaWFuX2Vucm9sbG1lbnRzIGNyZWF0ZTpndWFyZGlhbl9lbnJvbGxtZW50X3RpY2tldHMgcmVhZDp1c2VyX2lkcF90b2tlbnMgY3JlYXRlOnBhc3N3b3Jkc19jaGVja2luZ19qb2IgZGVsZXRlOnBhc3N3b3Jkc19jaGVja2luZ19qb2IgcmVhZDpjdXN0b21fZG9tYWlucyBkZWxldGU6Y3VzdG9tX2RvbWFpbnMgY3JlYXRlOmN1c3RvbV9kb21haW5zIHJlYWQ6ZW1haWxfdGVtcGxhdGVzIGNyZWF0ZTplbWFpbF90ZW1wbGF0ZXMgdXBkYXRlOmVtYWlsX3RlbXBsYXRlcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.FdLPwNxhJ-MGGs-_6oJF0O7QLjtFhs0C8FyYNGMNlR49eVE34AIdQxDanO_ju10-Rrzwan0QNkqPl0w3vmjHxP3JmSk1MzA0Xdt5s_Co2tONW7y4cFiPURnXTscYWMnmqxZQ-43hTBvbyrD2x0ta2kCJDUMmf3bIIh7gvKAYuXEe-SkZkL-DHayf7KWAQnRoXg3c7wkF1OCvVqBhGpUw34-HKun6pOMJdmweYeh9VTWBiWP1TgdOOZeRBoT8E3wWXXa3VRqfwGrgB9QUBxV6gLEKDr3qDqQgiKMpkptEgNTo9aRI3w2uI0Ru-8m1h8TIHLIhg0MPtc6r7Yhhltgjwg',
        'Content-Type': 'application/json'
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_steps_new(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url = "https://api.nbkcapital-smartwealth.com/api/v1/profile/kyc/steps_new"

        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        

    def test_post_primary_id_front(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        

        response = requests.post(
        "https://api.nbkcapital-smartwealth.com/api/v2/profile/primary-id",
        
        files={'file': open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\TEST.pdf', 'rb')},

        headers={
            "Authorization":Variables.Authorization,
            "x-locale":"en_US",
            "x-version":"1.8.68",
            "x-platform":"android"
                    
        }
            )
            
        #Script
        
        a=response.json()
                                    
        print("RESPONSE: "+response.text)
        Variables.temp_status_code=response.status_code
        Variables.temp_API_URL="https://api.nbkcapital-smartwealth.com/api/v2/profile/primary-id"
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
    

    def test_post_primary_id_back(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        response = requests.post(
        "https://api.nbkcapital-smartwealth.com/api/v2/profile/primary-id-other-side",
        
        files={'file': open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\TEST.pdf', 'rb')},

        headers={
            "Authorization":Variables.Authorization,
            "x-locale":"en_US",
            "x-version":"1.8.68",
            "x-platform":"android"
                    
        }
            )
            
        #Script
        
        a=response.json()


        print("RESPONSE: "+response.text)
        Variables.temp_status_code=response.status_code
        Variables.temp_API_URL="https://api.nbkcapital-smartwealth.com/api/v2/profile/primary-id-other-side"
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        

    def test_get_video_id(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+"profile/video-id/signed-url?file_name=%s.mp4"%Variables.User_id
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("RESPONSE: "+response.text)
        
        
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        

    def test_post_video_id(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"profile/video-id"
        payload='file_name=%s.mp4'%Variables.User_id
        response = requests.request("GET", url, headers=Variables.header_Authorization,data=payload)
    
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        # assert response.status_code==200 or response.status_code==201 or response.status_code==202
        pass



# ######################################
    
# #   KYC 
    
# ######################################



class Test_KYC(object):
    
    def test_get_kyc(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+"profile/kyc"
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_kyc_personal_info(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+"profile/kyc"
        Personal_info= json.dumps({ "sex": "m",
                                "first_name": "Create user",
                                "middle_name": "Backend Automation",
                                "family_name": "Script",
                                "birth_country": "AU",
                                "nationality": "KW",
                                "birth_date": "1996-06-09T00:00:00.000Z",
                                "civil_id_number": str(Variables.CivilIDNumber),
                                "civil_id_serial": str(Variables.civil_id_serial),
                                "civil_id_expiry_date": "2026-08-12T19:39:40.000Z",
                                "passport_number": "Backend",
                                "passport_country": "LB",
                                "passport_expiry_date": "2028-08-23T15:57:51.290Z",
                                "is_customer_same_as_beneficiary": True,
                                "beneficiary_power_of_attorney_enabled": False
                            })
        response = requests.request("PUT", url, headers=Variables.header_Authorization,data=Personal_info)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
    def test_get_kyc_1(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+"profile/kyc"
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
    def test_kyc_address_info(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+"profile/kyc"
        Address_info=json.dumps({   "address_country": "KW",
                                "address_city": "Farwaniya",
                                "address_area": "Reggai",
                                "address_street": "Test",
                                "address_block": "55",
                                "address_house": "Test",
                                "is_customer_same_as_beneficiary": True,
                                "beneficiary_power_of_attorney_enabled": False,
                                "contact_mobile_number": str(Variables.MobileNumber)
                                })

        response = requests.request("PUT", url, headers=Variables.header_Authorization,data=Address_info)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
       
    def test_kyc_Employment_info(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+"profile/kyc"
        Employment_info=json.dumps({    "employment_status" : "employed",
                                    "employer_type" : "private_sector",
                                    "private_sector_industry" : "travel_transportation",
                                    "employment_sector" : "travel_agency",
                                    "employment_company" : "Yik",
                                    "employment_department" : "Hjb",
                                    "employment_place" : "Ijv",
                                    "auth_sign_process_financial_transactions" : False,

                                    "is_customer_same_as_beneficiary" : True,
                                    "beneficiary_power_of_attorney_enabled" : False,

                                    "board_membership_existing" : False
                                    })
        response = requests.request("PUT", url, headers=Variables.header_Authorization,data=Employment_info)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        

    def test_kyc_IncomeAndWealth_info(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+"profile/kyc"
        IncomeAndWealth_info=json.dumps({   "investment_reason" : "income_generation",
                                        "trading_experience" : "good",
                                        "income_source" : ["investments"],


                                        "income_annual" : "20,000-50,000",
                                        "liquid_investments_kd" : "less_than_15000",


                                        "assets_value" : "above_100000_kd",
                                        "transactions_value_past_two_years" : "below_250000_kd",
                                        "financial_sector_years_experience" : "less_than_one_year",

                                        "beneficiary_power_of_attorney_enabled" : False,
                                        "is_customer_same_as_beneficiary" : True,
                                        "bank_name" : str(Variables.Bank)})

        response = requests.request("PUT", url, headers=Variables.header_Authorization,data=IncomeAndWealth_info)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        

    def test_kyc_Additional_info(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+"profile/kyc"
        Additional_info=json.dumps({    "political_position_existing" : True,
                                        "political_position_is_me" : False,
                                        "political_position_role" : "parliment_member",
                                        "political_position_relationship" : "child",
                                        "political_position_name" : "Testfamilymemberpolitical name",


                                        "us_citizen" : True,
                                        "tax_payer_identification" : "Testtaxus",
                                        "us_address_1" : "Testus1",
                                        "us_address_2" : "Testus2",


                                        "pays_taxes_in_other_country" : True,
                                        "tax_country_1" : "US",
                                        "tax_country_2" : "IS",
                                        "tax_country_3" : "AW",

                                        "tax_payer_id_1" : "TestTaxUS",
                                        "tax_payer_id_2" : "Test tax additional 1",
                                        "tax_payer_id_3" : "Test tax additional 2",


                                        "is_customer_same_as_beneficiary" : True,
                                        "beneficiary_power_of_attorney_enabled" : False })
        
        response = requests.request("PUT", url, headers=Variables.header_Authorization,data=Additional_info)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_get_kyc_2(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+"profile/kyc"
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        

    def test_ConfirmClassification(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"profile"
        payload = json.dumps({"is_classification_confirmed":True})
        response = requests.request("PUT", url, headers=Variables.header_Authorization, data=payload)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
        
        
    
# ######################################
    
# #   Create and Sign Contract
# #   Approve the user
    
# ######################################



class Test_SignContract_Approve(object):    
    def test_CreateContract(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+"profile/contract"
        response = requests.request("POST", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        

    def test_SignContract(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"development/"+Variables.User_id+"/set-contract-signed"
        headers={
                "Authorization":"#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#",
                "Content-Type":"application/json",
                "x-locale":"en_US",
                "x-version":"1.0",
                "x-platform":Variables.x_platorm          
            }

        response = requests.request("PUT", url, headers=headers)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Set_Admin_risk_classification(self):
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"admin/profile/"+str(Variables.User_id)
        payload = json.dumps({
                        "contact_mobile_number": Variables.MobileNumber,
                        "civil_id_expiry_date": str(datetime.today().strftime('%Y-%m-%d')),
                        "civil_id_serial": Variables.civil_id_serial,
                        "risk_level": "Medium"
                    })
        headers={
                "Authorization":Variables.AdminAuthorization,
                "Content-Type":"application/json",
                "x-locale":"en_US",
                "x-version":"1.0",
                "x-platform":Variables.x_platorm          
            }

        response = requests.request("PUT", url, headers=headers, data=payload)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_Set_Admin_internal_note(self):
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"admin/profile/%s/notes"%str(Variables.User_id)
        payload = json.dumps({"note": "Backend Deployment Smoke Tests\nPlease report in case you found issue and thank you."})
        headers={    'Accept': '*/*',
                                'Accept-Language': 'en-US,en;q=0.9',
                                'Authorization': Variables.AdminAuthorization,
                                'Connection': 'keep-alive',
                                'Content-Type': 'application/json',
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
                                        
        
        response = requests.request("POST", url, headers=headers, data=payload)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202



    def test_set_CivilID_KYCExpiry(self):

        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"development/%s/set-kyc-cid-expiry"%Variables.User_id
        payload = json.dumps({  "kyc_expiry_date":datetime.today().replace(year=datetime.today().year+4).strftime('%Y-%m-%d'),
                                "cid_expiry_date":datetime.today().replace(year=datetime.today().year+4).strftime('%Y-%m-%d')
                                })
        response = requests.request("POST", url, headers=Variables.header_Authorization, data=payload)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202





    def test_ApproveUser_CivilID(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"external/project-connect/dev/profile/approve"
        payload = json.dumps({"civil_id_number": str(Variables.CivilIDNumber)})
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
        

######################################
    
#   Initial Deposit 
#   Activate the user

######################################
    
    
    
class Test_Initial_Deposit_Activate(object):


    def test_exposure(self):
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"portfolio/%s/exposure"%str(Variables.User_id)
        
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_holdings(self):
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"portfolio/%s/holding"%str(Variables.User_id)
        
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    
    
    def test_InitialDeposit_BankTransfer(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"transactions/deposit/"+str(Variables.User_id)
        
        Deposit_Info=json.dumps({           "bank_name": str(Variables.Bank),
                                            "beneficiary_name": "",
                                            "frequency_type": 0,
                                            "initial_investment": 5000,
                                            "start_date": str(datetime.today().strftime('%Y-%m-%d')),
                                            "recurring_investment": 0,
                                            "transfer_method": "Bank Transfer" 
                                            })
        response = requests.request("POST", url, headers=Variables.header_Authorization, data=Deposit_Info)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
    def test_ActivateUser(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"development/activate/"+Variables.User_id

        headers = {'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#',
                    'Content-Type': 'application/json',     'x-locale': 'en_US',    'x-version': '1.0',     'x-platform': 'web'}
        ActivatePortfolio_Info=json.dumps({  "initial_investment": 12000, "create_fund": True })
        response = requests.request("POST", url, headers=headers, data=ActivatePortfolio_Info)
        a=response.json()

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


######################################

#   Test Portfolio
#   Test Banners
#   Test SW Articles
    
######################################



class Test_GeneralActiveAPIs(object):

    
    
    
    def test_Get_Profile_2(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url=Variables.SW_UAT_URL+"profile"    
        response = requests.request("GET", url, headers=Variables.header_Authorization)
        a=response.json()
        
        Variables.iban=a["meta"]["iban_number"]
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
        
    def test_Portfolios_Info(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+ "portfolio" 
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
            

    def test_Banners(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+ "profile/banners"
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
    def test_SW_Articles(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url="https://blog.nbkcapitalsmartwealth.com/wp-json/wp/v2/posts?categories=25,17&page=1&per_page=4&order_by=date"
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
    
    


######################################
    
#   Additional Deposit 
#   Full Withdrawal
    
######################################
    
    
   
class Test_AdditionalDeposit_Withdrawal(object):

    def Additional_Funds(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url = "https://api.nbkcapital-smartwealth.com/api/v2/development/add/"+Variables.User_id+"/fund"
        payload = json.dumps({"amount": str(5555)})
        headers = {    'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#',    'Content-Type': 'application/json'     }
        response = requests.request("POST", url, headers=headers, data=payload)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
            
    def test_AdditionalDeposit_BankTransfer(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"transactions/deposit/"+str(Variables.User_id)
            
        Deposit_Info=json.dumps({       "bank_name": str(Variables.Bank),
                                        "beneficiary_name": "",
                                        "frequency_type": 0,
                                        "initial_investment": 5000,
                                        "start_date": str(datetime.today().strftime('%Y-%m-%d')),
                                        "recurring_investment": 0,
                                        "transfer_method": "Bank Transfer"
                                        })
        response = requests.request("POST", url, headers=Variables.header_Authorization, data=Deposit_Info)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
    def test_Profile_Transactions(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+ "profile/transactions"
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Full_Withdrawal(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url=Variables.SW_UAT_URL+"transactions/withdraw/"+Variables.User_id
        Full_Withdrawal=json.dumps  (    {"iban_number":Variables.iban,
                                "is_full_withdraw":True,
                                "purpose":"7",
                                "source_bank":"nbk_kuwait",
                                "transfer_method":"Bank Transfer"})

        response = requests.request("POST", url, headers=Variables.header_Authorization, data=Full_Withdrawal)
        a=response.json()
        Variables.withdrawal_id=a["meta"]["transaction_id"]
        Variables.withdrawal_otp=a["meta"]["otp_code"]
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Withdrawal_otp_Verification(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url= Variables.SW_UAT_URL+"transactions/%s/withdraw/verify"%Variables.withdrawal_id
        payload=json.dumps({"input_code":str(Variables.withdrawal_otp)})
        response = requests.request("POST", url, headers=Variables.header_Authorization, data=payload)
        a=response.json()
        
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert (response.status_code==200 or response.status_code==201 or response.status_code==202) and a["meta"]["result"]=="VALID"

    def test_get_Withdrawal_Pending_Instructions(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+ "transactions/funding-instructions/bank-transfer/"+Variables.User_id
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        



######################################
    
#   Test Bank Information 
#   Test Mobile Number Exists
#   Test Mobile Number OTP
#   Set Prefered method as Email Address
    
######################################
  
    
   
class Test_ConfirmMobile(object):


    def test_exposure(self):
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"portfolio/%s/exposure"%str(Variables.User_id)
        
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_holdings(self):
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"portfolio/%s/holding"%str(Variables.User_id)
        
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202



    def test_Bank_Information(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url = Variables.SW_UAT_URL+"profile/bank-information"
        response = requests.request("GET", url, headers=Variables.header_Authorization)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Confirm_Mobile_Number(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"profile/otp/sms/available?phone_number="+str(Variables.MobileNumber)
        response = requests.request("GET", url, headers=Variables.header_Authorization)
        a=response.json()

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Mobile_Number_OTP(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"profile/otp/sms"
        payload=json.dumps({"phone_number":str(Variables.MobileNumber)})
        response = requests.request("POST", url, headers=Variables.header_Authorization, data=payload)
        a=response.json()

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        Variables.MobileNumberOTP=a["meta"]["otp_code"]
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Verify_Mobile_OTP(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"profile/otp/sms/verify"

        payload=json.dumps({"otp_code":str(Variables.MobileNumberOTP),"phone_number":str(Variables.MobileNumber)})
        response = requests.request("POST", url, headers=Variables.header_Authorization, data=payload)
        a=response.json()

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Set_Prefered_Method_Email(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"profile"

        payload=json.dumps({"otp_preferred_method":"email"})
        response = requests.request("PUT", url, headers=Variables.header_Authorization, data=payload)
        a=response.json()

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202




######################################
    
#   Create a new Islamic portfolio 
#   Fund Portfolio
#   Activate Portfolio
#   Additional Deposit to Islamic Portfolio
#   Full Withdrawal on Islamic Portfolio
    
######################################



class Test_Additional_Islamic_Portfolio(object):
    
    def test_Create_Additional_Portfolio_Islamic(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
            
        url=Variables.SW_UAT_URL+"portfolio"
        Additional_Islamic_Portfolio_Info=json.dumps({
                "initial_investment": 558.0,
                "frequency_type": 0,
                "horizon": 15,
                "iban_number": Variables.iban,
                "investment_product": "GENERAL",
                "investment_type": "islamic",
                "modified_risk_score": int(Variables.modified_risk_score),
                "original_risk_score": int(Variables.original_risk_score),
                "mode": "conventional",
                "portfolio_name": "Islamic ",
                "reason": "education",
                "recurring_investment": 0.0,
                "target_amount": 2366.0,
                "type": "general"
                })

        response = requests.request("POST", url, headers=Variables.header_Authorization, data=Additional_Islamic_Portfolio_Info)
        a=response.json()
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        Variables.additional_islamic_portfolio_id=a["meta"]["portfolio_id"]
        
        

        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_Initial_Deposit_Additional_Islamic_Portfolio_BankTransfer(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url=Variables.SW_UAT_URL+"transactions/deposit/"+str(Variables.additional_islamic_portfolio_id)
        
        Additional_Portfolio_Deposit_BankTransfer = json.dumps({
                                                "bank_name": Variables.Bank,
                                                "beneficiary_name": "",
                                                "frequency_type": 0,
                                                "iban_number": Variables.iban,
                                                "initial_investment": 5000.0,
                                                "recurring_investment": 0.0,
                                                "start_date": "2022-11-11",
                                                "transfer_method": "Bank Transfer"
                                                })

        response = requests.request("POST", url, headers=Variables.header_Authorization, data=Additional_Portfolio_Deposit_BankTransfer)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Activate_Islamic_Portfolio(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url = Variables.SW_UAT_URL+"development/activate/"+Variables.additional_islamic_portfolio_id

        headers = {'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#',
                    'Content-Type': 'application/json',     'x-locale': 'en_US',    'x-version': '1.0',     'x-platform': 'web'}
        ActivatePortfolio_Info=json.dumps({  "initial_investment": 12000, "create_fund": True })

        response = requests.request("POST", url, headers=headers, data=ActivatePortfolio_Info)
        a=response.json()

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Additional_Deposit_Islamic_Portfolio_BankTransfer(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"transactions/deposit/"+str(Variables.additional_islamic_portfolio_id)
        Deposit_Info=json.dumps({       "bank_name": str(Variables.Bank),
                                        "beneficiary_name": "",
                                        "frequency_type": 0,
                                        "initial_investment": 5000,
                                        "start_date": str(datetime.today().strftime('%Y-%m-%d')),
                                        "recurring_investment": 0,
                                        "transfer_method": "Bank Transfer"
                                        })

        response = requests.request("POST", url, headers=Variables.header_Authorization, data=Deposit_Info)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Full_Withdrawal_Islamic_Portfolio(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url=Variables.SW_UAT_URL+"transactions/withdraw/"+str(Variables.additional_islamic_portfolio_id)
            
    
        Full_Withdrawal=json.dumps  (    {"iban_number":Variables.iban,
                                      "is_full_withdraw":True,
                                      "purpose":"7",
                                      "source_bank":"nbk_kuwait",
                                      "transfer_method":"Bank Transfer"})
        
        response = requests.request("POST", url, headers=Variables.header_Authorization, data=Full_Withdrawal)
        a=response.json()
        
        Variables.withdrawal_id=a["meta"]["transaction_id"]
        Variables.additional_islamic_withdrawal_otp=a["meta"]["otp_code"]
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Full_Withdrawal_otp_Verification_Islamic_Portfolio(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url= Variables.SW_UAT_URL+"transactions/%s/withdraw/verify"%Variables.withdrawal_id
        payload=json.dumps({"input_code":str(Variables.additional_islamic_withdrawal_otp)})
        response = requests.request("POST", url, headers=Variables.header_Authorization, data=payload)
        a=response.json()
        
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert (response.status_code==200 or response.status_code==201 or response.status_code==202) and a["meta"]["result"]=="VALID"

    def test_Full_get_Withdrawal_Pending_Instructions_Islamic_Portfolio(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+ "transactions/funding-instructions/bank-transfer/"+Variables.User_id
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_exposure(self):
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"portfolio/%s/exposure"%str(Variables.additional_islamic_portfolio_id)
        
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_holdings(self):
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"portfolio/%s/holding"%str(Variables.additional_islamic_portfolio_id)
        
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    
    
    
    
# ######################################
    
# #   Create a new ETF portfolio 
# #   Fund Portfolio
# #   Activate Portfolio
# #   Additional Deposit to ETF Portfolio
# #   Partial Withdrawal on ETF Portfolio
    
# ######################################
    
    
    
  
class Test_Additional_ETF_Portfolio(object):
        
    def test_Create_Additional_Portfolio_ETF(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
            
        url=Variables.SW_UAT_URL+"portfolio"
        Additional_ETF_Portfolio_Info=json.dumps({
                                            "initial_investment": 966.0,
                                            "frequency_type": 0,
                                            "horizon": 15,
                                            "iban_number": Variables.iban,
                                            "investment_product": "GENERAL",
                                            "investment_type": "etf",
                                            "modified_risk_score": int(Variables.original_risk_score),
                                            "original_risk_score": int(Variables.original_risk_score),
                                            "mode": "conventional",
                                            "portfolio_name": "etf",
                                            "reason": "education",
                                            "recurring_investment": 0.0,
                                            "target_amount": 11664.0,
                                            "type": "goal"
                                            })

        response = requests.request("POST", url, headers=Variables.header_Authorization, data=Additional_ETF_Portfolio_Info)
        a=response.json()

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        Variables.additional_etf_portfolio_id=a["meta"]["portfolio_id"]

        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_Initial_Deposit_Additional_ETF_Portfolio_BankTransfer(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url=Variables.SW_UAT_URL+"transactions/deposit/"+str(Variables.additional_etf_portfolio_id)
        Additional_Portfolio_Deposit_BankTransfer = json.dumps({
                                            "bank_name": Variables.Bank,
                                            "beneficiary_name": "",
                                            "frequency_type": 0,
                                            "iban_number": Variables.iban,
                                            "initial_investment": 5000.0,
                                            "recurring_investment": 0.0,
                                            "start_date": "2022-11-11",
                                            "transfer_method": "Bank Transfer"
                                            })

        response = requests.request("POST", url, headers=Variables.header_Authorization, data=Additional_Portfolio_Deposit_BankTransfer)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Activate_ETF_Portfolio(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url = Variables.SW_UAT_URL+"development/activate/"+Variables.additional_etf_portfolio_id

        headers = {'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#',
                    'Content-Type': 'application/json',     'x-locale': 'en_US',    'x-version': '1.0',     'x-platform': 'web'}
        ActivatePortfolio_Info=json.dumps({  "initial_investment": 12000, "create_fund": True })

        response = requests.request("POST", url, headers=headers, data=ActivatePortfolio_Info)

        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Additional_Deposit_ETF_Portfolio_BankTransfer(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"transactions/deposit/"+str(Variables.additional_etf_portfolio_id)
        Deposit_Info=json.dumps({       "bank_name": str(Variables.Bank),
                                        "beneficiary_name": "",
                                        "frequency_type": 0,
                                        "initial_investment": 5000,
                                        "start_date": str(datetime.today().strftime('%Y-%m-%d')),
                                        "recurring_investment": 0,
                                        "transfer_method": "Bank Transfer"
                                        })

        response = requests.request("POST", url, headers=Variables.header_Authorization, data=Deposit_Info)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

    def test_Partial_Withdrawal_ETF_Portfolio(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url=Variables.SW_UAT_URL+"transactions/withdraw/"+str(Variables.additional_etf_portfolio_id)
        Partial_Withdrawal=json.dumps({     "amount_usd":200.0,
                                        "iban_number":Variables.iban,
                                        "is_full_withdraw":False,
                                        "purpose":"6",
                                        "source_bank":"nbk_kuwait",
                                        "transfer_method":"Bank Transfer"})
        
        response = requests.request("POST", url, headers=Variables.header_Authorization, data=Partial_Withdrawal)
        a=response.json()
        print(a)
        Variables.withdrawal_id=a["meta"]["transaction_id"]
        Variables.additional_etf_withdrawal_otp=a["meta"]["otp_code"]
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_Partial_Withdrawal_otp_Verification_ETF_Portfolio(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        url= Variables.SW_UAT_URL+"transactions/%s/withdraw/verify"%str(Variables.withdrawal_id)
        payload=json.dumps({"input_code":Variables.additional_etf_withdrawal_otp})
        response = requests.request("POST", url, headers=Variables.header_Authorization, data=payload)
        a=response.json()
        
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert (response.status_code==200 or response.status_code==201 or response.status_code==202) and a["meta"]["result"]=="VALID"

    def test_Partial_get_Withdrawal_Pending_Instructions_ETF_Portfolio(self):
        
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)
        
        url = Variables.SW_UAT_URL+ "transactions/funding-instructions/bank-transfer/"+Variables.User_id
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202

        
        
    def test_exposure(self):
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"portfolio/%s/exposure"%str(Variables.additional_etf_portfolio_id)
        
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202


    def test_holdings(self):
        class_name=(__class__.__name__).replace("Test_","")
        func_name = (inspect.stack()[0][3]).replace("test_","")
        Variables.temp_test_case=str(class_name)+" Class :: "+str(func_name)

        url = Variables.SW_UAT_URL+"portfolio/%s/holding"%str(Variables.additional_etf_portfolio_id)
        
        response = requests.request("GET", url, headers=Variables.header_Authorization)
    
        print("CURL: " +curlify.to_curl(response.request))
        print("RESPONSE: "+response.text)
        
        
        Variables.temp_status_code=response.status_code        
        Variables.temp_API_URL=url
        assert response.status_code==200 or response.status_code==201 or response.status_code==202
        
        
        
def save_json():
        
    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    # print(json_object)
    
    json_object["Email"] = Variables.Email
    json_object["user_type"] = Variables.UserType
    json_object["user_id"] = Variables.User_id
    json_object["mobile_number"] = Variables.MobileNumber
    json_object["civil_id"]= Variables.CivilIDNumber
    json_object["iban"] = Variables.iban
    json_object["original_risk_score"] = Variables.original_risk_score
    json_object["modified_risk_score"] = Variables.modified_risk_score

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
