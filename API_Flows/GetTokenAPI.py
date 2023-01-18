import json
import requests

from Constants_Technical_Variables import Constants


def GetTokenAPI(Email):
    
    
    API_Name="Get Bearer Token"
    for i in range(0,2):
        r = requests.get(
            Constants.SW_UAT_URL+"development/get-token?email="+Email,

            
            headers={	
                    "Authorization": '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'
                    }
        )
        
        #Script
        
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text
        Authorization="Bearer " + a["access_token"]
        break
    if r.status_code==200 or r.status_code==201:
        return Authorization
    else:
        return False


def PostTokenAPI(Email):
    
    
    API_Name="Post Bearer Token"
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

    StatusCode=str(response.status_code)
    Authorization="Bearer "+a["access_token"]    
    return Authorization