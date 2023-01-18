import json
import requests

from Constants_Technical_Variables import Constants #HTTPS this is HTTP


def PostTokenAPI(Email):
    
    
    API_Name="Post Bearer Token"
    for i in range(0,2):

        url = "https://auth.staging-nbksmartwealth.com/oauth/token"

        payload = json.dumps({
        "username": Email,
        "password": "Password123",
        "audience": "https://staging-nbksmartwealth.eu.auth0.com/api/v2/",
        "grant_type": "http://auth0.com/oauth/grant-type/password-realm",
        "scope": "openid email",
        "realm": "Username-Password-Authentication",
        "client_id": "QpVWZklsV9I7hDBfhDVW6PMGRtG9pNs6"
        })
        headers = {
        'X-locale': 'ar_AE',
        'X-version': '1.0',
        'Content-Type': 'application/json',
        'Cookie': '__cf_bm=ZOo98B.ImOsxrvZOvkMfieuemv7_VsFGBbSLyzQa6Fw-1666023586-0-AV7ABDeRCEt1HDEZx6mtwS4mxj01mhiMRaWFkxF593EPp0cSFUYWBczlEeien+fTDyVEVUIDOqgPSaluDUGtyFs=; did=s%3Av0%3A6493fda0-91f8-11ec-bd24-23d965feca4f.YKRF%2BNhTSyAOJufKB2VSnGEc%2B5cnjmJO1Kvd6NagNTo; did_compat=s%3Av0%3A6493fda0-91f8-11ec-bd24-23d965feca4f.YKRF%2BNhTSyAOJufKB2VSnGEc%2B5cnjmJO1Kvd6NagNTo'
        }

        r = requests.request("POST", url, headers=headers, data=payload)
        
        # print(r.text)
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text
        Authorization="Bearer " + a["access_token"]
        break
    return Authorization