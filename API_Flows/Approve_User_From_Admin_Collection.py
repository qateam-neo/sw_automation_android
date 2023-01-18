

import json
import requests

from ManualReport import ReportResultsAPICollection
from Constants_Technical_Variables import Constants


def APIScript_RunCollection_ApproveUserAdmin(ReportDriver,Email,AdminAuthorization):
    User_ID=None
        
    print("Approving user from Admin: ")
        
    API_Name="GET User ID"
    r = requests.get(
        Constants.SW_UAT_URL+"admin/profile?user_filter_type=all&offset=0&limit=1000&investment_type=all&q=",
    
        params={
            "user_filter_type":"all",
            "offset":'0',
            "limit":"1000",
            "investment_type":"all"
        },
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
    
    #Script
    
    a=r.json()
    for ELEM in a["meta"]["data"]:
        # print(ELEM["email"])
        if ELEM["email"]==Email.lower():
            User_ID=ELEM["id"]
            break
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    # print(a)
    # print(User_ID)
    
    API_Name="GET Admin Info"
    r = requests.get(
        Constants.SW_UAT_URL+"admin/profile/%s/info"%User_ID,
    
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
    
    #Script
    
    a=r.json()
    # print(a)
    PhoneNumber=a["meta"]["phone_number"]
    SerialID=a["meta"]["serial_id"]
    CivilIDExpiry=a["meta"]["civil_id_expiry_date"]
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    API_Name="Set Risk Classification"

    r = requests.put(
        Constants.SW_UAT_URL+"admin/profile/b74df86e-4098-4d11-80ac-adb7c1595838",

        data=json.dumps({
            "contact_mobile_number":PhoneNumber,
            "civil_id_expiry_date":CivilIDExpiry,
            "civil_id_serial":SerialID,
            "risk_level":"Low"
            }),
        
        
        headers={
            'Accept': '*/*' ,
            'Accept-Language': 'en-US,en;q=0.9' ,
            'Authorization': AdminAuthorization,
            'Connection': 'keep-alive' ,
            'Content-Type': 'application/json' ,
            'ContentType': 'application/json' ,
            'Origin': 'https://admin.nbkcapital-smartwealth.com' ,
            'Referer': 'https://admin.nbkcapital-smartwealth.com/' ,
            'Sec-Fetch-Dest': 'empty' ,
            'Sec-Fetch-Mode': 'cors' ,
            'Sec-Fetch-Site': 'same-site' ,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'X-Locale': 'en_US' ,
            'X-Platform': 'web' ,
            'X-Version': '2.0' ,
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0' ,
            'sec-ch-ua-platform': '"Windows"'
                    
        }
    )
    
    #Script
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    API_Name="Set RM Code"
    r = requests.put(
        Constants.SW_UAT_URL+"admin/rm/user/"+User_ID,

        data=json.dumps({
            "rm_id":None
            }),
        
        headers={
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.9",
            "Authorization": AdminAuthorization,
            "Connection":"keep-alive",
            "Content-Type":"application/json",
            "ContentType":"application/json",
            "Origin":"https://admin.nbkcapital-smartwealth.com",
            "Referer":"https://admin.nbkcapital-smartwealth.com/",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-site",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "X-Locale":'en_US',
            "X-Platform":"web",
            "X-Version":"2.0",
            "sec-ch-ua-mobile":"?0",
            "sec-ch-ua-platform":"Windows"
                    
        }
    )
    
    #Script
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    
    
    
    API_Name="Clear World check"
    r = requests.put(
        Constants.SW_UAT_URL+"admin/profile/%s/manual_validation?step_identifier=STEP_WORLD_CHECK_APPROVAL&step_status=APPROVED"%User_ID,

        params={
            "step_identifier":"STEP_WORLD_CHECK_APPROVAL",
            "step_status":"APPROVED"
        },
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
    
    #Script
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    
    API_Name="Clear PEP"
    r = requests.put(
        Constants.SW_UAT_URL+"admin/profile/%s/manual_validation?step_identifier=PEP_APPROVAL&step_status=APPROVED"%User_ID,

        params={
            "step_identifier":"PEP_APPROVAL",
            "step_status":"APPROVED"
        },
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
    
    #Script
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    
    API_Name="Clear Country"
    r = requests.put(
        Constants.SW_UAT_URL+"admin/profile/%s/manual_validation?step_identifier=STEP_AML_COUNTRIES_APPROVAL&step_status=APPROVED"%User_ID,

        params={
            "step_identifier":"STEP_AML_COUNTRIES_APPROVAL",
            "step_status":"APPROVED"
        },
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
    
    #Script
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    
    API_Name="Clear Employment"
    r = requests.put(
        Constants.SW_UAT_URL+"admin/profile/%s/manual_validation?step_identifier=STEP_AML_EMPLOYMENT_APPROVAL&step_status=APPROVED"%User_ID,

        params={
            "step_identifier":"STEP_AML_EMPLOYMENT_APPROVAL",
            "step_status":"APPROVED"
        },
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
    
    #Script
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    
    API_Name="Clear Civil ID"
    r = requests.put(
        Constants.SW_UAT_URL+"admin/profile/%s/manual_validation?step_identifier=VERIFY_CIVIL_ID_AND_PASSPORT&step_status=APPROVED"%User_ID,

        params={
            "step_identifier":"VERIFY_CIVIL_ID_AND_PASSPORT",
            "step_status":"APPROVED"
        },
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
    
    #Script
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    
    API_Name="Clear Contract"
    r = requests.put(
        Constants.SW_UAT_URL+"admin/profile/%s/manual_validation?step_identifier=CONTRACT_SIGNING_APPROVAL&step_status=APPROVED"%User_ID,

        params={
            "step_identifier":"CONTRACT_SIGNING_APPROVAL",
            "step_status":"APPROVED"
        },
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
    
    
    
    #Script
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    
    
    
    API_Name="Upload Corruption document"
    r = requests.post(
        Constants.SW_UAT_URL+"admin/project-connect/%s/user-document?file_type=google_corruption_check"%User_ID,

        params={
            "file_type":"google_corruption_check"
        },
        files={'file': open('TEST.pdf', 'rb')},
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
       #Script
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    API_Name="Upload Money Laundering document"
    r = requests.post(
        Constants.SW_UAT_URL+"admin/project-connect/%s/user-document?file_type=google_money_laundering_check"%User_ID,
        params={
            "file_type":"google_money_laundering_check"
        },
        files={'file': open('TEST.pdf', 'rb')},
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
       #Script
    
    if r.status_code !=200 and r.status_code !=201:
        TestsPassed=False
    
    
     
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    
    API_Name="Upload Risk Matrix document"
    r = requests.post(
        Constants.SW_UAT_URL+"admin/project-connect/%s/user-document?file_type=google_risk_matrix"%User_ID,
        params={
            "file_type":"google_risk_matrix"
        },
        files={'file': open('TEST.pdf', 'rb')},
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                            }
    )
       #Script
    
    if r.status_code !=200 and r.status_code !=201:
        TestsPassed=False
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    
    API_Name="Upload Team Lead Document"
    r = requests.post(
        Constants.SW_UAT_URL+"admin/project-connect/%s/user-document?file_type=team_lead_approval"%User_ID,
        params={
            "file_type":"team_lead_approval"
        },
        files={'file': open('TEST.pdf', 'rb')},
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",

                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
       #Script
    
    if r.status_code !=200 and r.status_code !=201:
        TestsPassed=False
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    
    API_Name="DCEO Approval"
    r = requests.post(
        Constants.SW_UAT_URL+"admin/project-connect/%s/user-document?file_type=dceo_approval"%User_ID,
        params={
            "file_type":"dceo_approval"
        },
        files={'file': open('TEST.pdf', 'rb')},
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
       #Script
    
    if r.status_code !=200 and r.status_code !=201:
        TestsPassed=False
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
    
    API_Name="Final Approval button"
    r = requests.put(
        Constants.SW_UAT_URL+"admin/profile/%s/validation?step_identifier=ACCOUNT_MANUAL_APPROVAL&step_status=APPROVED"%User_ID,
        params={
            "step_identifier":"ACCOUNT_MANUAL_APPROVAL",
            "step_status":"APPROVED"
        },
        
        headers={
                "authority": "sw-api.nbkcapital-smartwealth.com",
                "x-version": "1.0",
                "sec-ch-ua-mobile": "?0",
                "authorization": AdminAuthorization,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                "x-locale": "en_US",
                "x-platform": "web",
                "contenttype": "application/json",
                "accept": "*/*",
                "origin": "https://admin.nbkcapital-smartwealth.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://admin.nbkcapital-smartwealth.com/",
                "accept-language": "en-US,en;q=0.9"
                    
        }
    )
       #Script
    
    if r.status_code !=200 and r.status_code !=201:
        TestsPassed=False
    
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)

    if ReportDriver==None:
        print("No Report Driver found")
    else:
        ReportDriver.report().test(name="APICALLS", message="Api calls approve user admin", passed=True)
    return User_ID