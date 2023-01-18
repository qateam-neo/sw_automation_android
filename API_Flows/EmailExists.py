import json
import requests
from GetProfileAPIReturnID import GetProfileAPIReturnID, PJConnect_GetProfileAPIReturnID
from Constants_Technical_Variables import Constants #HTTPS this is HTTP

from GetTokenAPI import GetTokenAPI


def CheckIfEmailExists_ReturnUser_ID(Email):
    try:
        if GetTokenAPI(Email)==False:
            raise ValueError("Get Token API is not available")
    except:
        
        url = "https://auth.staging-nbksmartwealth.com/oauth/token"
        payload = json.dumps({"username": Email,
                            "password": "Password123",
                            "audience": "https://staging-nbksmartwealth.eu.auth0.com/api/v2/",
                            "grant_type": "http://auth0.com/oauth/grant-type/password-realm",
                            "scope": "openid email",
                            "realm": "Username-Password-Authentication",
                            "client_id": "QpVWZklsV9I7hDBfhDVW6PMGRtG9pNs6"
                            })
        header_Cookie={'X-Platform': 'android' , 'X-locale': 'en_US' , 'X-version': '1.0' , 'Content-Type': 'application/json' , 'Cookie': 'did=s%3Av0%3A6493fda0-91f8-11ec-bd24-23d965feca4f.YKRF%2BNhTSyAOJufKB2VSnGEc%2B5cnjmJO1Kvd6NagNTo; did_compat=s%3Av0%3A6493fda0-91f8-11ec-bd24-23d965feca4f.YKRF%2BNhTSyAOJufKB2VSnGEc%2B5cnjmJO1Kvd6NagNTo'}

        response = requests.request("POST", url, headers=header_Cookie, data=payload)
        a=response.json()
            
        # print(r.text)
        if response.status_code == 200 or response.status_code == 201  or response.status_code =="200" or response.status_code == "201" :
            AuthTemp="Bearer "+a["access_token"]
            User_ID=GetProfileAPIReturnID(Authorization=AuthTemp)        
            return User_ID
        else:
            return False

def PJConnect_CheckIfEmailExists_ReturnUser_ID(CMNO):


    url = "https://sw-api.nbkcapital-smartwealth.com/api/v2/development/project-connect/token"

    payload = json.dumps({
    "civil_id": CMNO,
    "is_encoded": True
    })
    headers = {
    'X-Platform': 'android',
    'X-Version': '1.0',
    'User-Agent': 'Mozilla/4.0 [en] (WinNT; I)',
    'X-Locale': 'en_US',
    'Accept': 'application/json, text/plain, */*',
    'authority': 'sw-api.nbkcapital-smartwealth.com',
    'Content-Type': 'application/json',
    'x-token-source': 'connect',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'http://neo-frontend',
    'referer': 'http://neo-frontend/',
    'authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'
    } 
    response = requests.request("POST", url, headers=headers, data=payload)
    a=response.json()
    print(response.text)
    # print(r.text)
    if response.status_code == 200 or response.status_code == 201  or response.status_code =="200" or response.status_code == "201" :
        AuthTemp="Bearer "+a["token"]
        User_ID=PJConnect_GetProfileAPIReturnID(Authorization=AuthTemp)    
        print(User_ID)   
        return User_ID
    else:
        return False

