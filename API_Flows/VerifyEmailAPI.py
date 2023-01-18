

import json
import os
from colorama import Fore
import requests
from Constants_Technical_Variables import Constants

from ManualReport import ReportResultsAPICollection


def VerifyEmailAPI (ReportDriver,Email,Password,Authorization="N/A"):
        
    print ("Verifying Email Address: ")
    print ("Verifying Email Address: ",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))


    API_Name="Get User Profile"
    for i in range(0,2):
        r = requests.get(
            Constants.SW_UAT_URL+"profile",
        
            headers={
                "Authorization":Authorization,
                "Content-Type":"application/json",
                "x-locale":"en_US",
                "x-version":"1.0",
                "x-platform":"android"
                        
            }
            
        )
        
        #Script
        
        a=r.json()
        Auth0_UserID=a["meta"]["auth0_id"]
        StatusCode=str(r.status_code)
        Response=r.text
        break
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
        
        
    API_Name="Verify Email API"
    for i in range(0,2):
        r = requests.patch(
            "https://staging-nbksmartwealth.eu.auth0.com/api/v2/users/"+Auth0_UserID,
        
        
            data={
                "email":Email,
                "email_verified": "true",
                "verify_email":"true"
            },
            headers={
                "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1xcHNlck9mQzJyT0l6ZjhxMWdUTyJ9.eyJpc3MiOiJodHRwczovL3N0YWdpbmctbmJrc21hcnR3ZWFsdGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImdhbEtZWlJKbzZ1eUFsZ2ZYZEFZazdvVWRUMmk1cllGQGNsaWVudHMiLCJhdWQiOiJodHRwczovL3N0YWdpbmctbmJrc21hcnR3ZWFsdGguZXUuYXV0aDAuY29tL2FwaS92Mi8iLCJpYXQiOjE2NzAyMzY1MjcsImV4cCI6MTY3MjgyODUyNywiYXpwIjoiZ2FsS1laUkpvNnV5QWxnZlhkQVlrN29VZFQyaTVyWUYiLCJzY29wZSI6InJlYWQ6Y2xpZW50X2dyYW50cyBjcmVhdGU6Y2xpZW50X2dyYW50cyBkZWxldGU6Y2xpZW50X2dyYW50cyB1cGRhdGU6Y2xpZW50X2dyYW50cyByZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgY3JlYXRlOnVzZXJzIHJlYWQ6dXNlcnNfYXBwX21ldGFkYXRhIHVwZGF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgZGVsZXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBjcmVhdGU6dXNlcnNfYXBwX21ldGFkYXRhIGNyZWF0ZTp1c2VyX3RpY2tldHMgcmVhZDpjbGllbnRzIHVwZGF0ZTpjbGllbnRzIGRlbGV0ZTpjbGllbnRzIGNyZWF0ZTpjbGllbnRzIHJlYWQ6Y2xpZW50X2tleXMgdXBkYXRlOmNsaWVudF9rZXlzIGRlbGV0ZTpjbGllbnRfa2V5cyBjcmVhdGU6Y2xpZW50X2tleXMgcmVhZDpjb25uZWN0aW9ucyB1cGRhdGU6Y29ubmVjdGlvbnMgZGVsZXRlOmNvbm5lY3Rpb25zIGNyZWF0ZTpjb25uZWN0aW9ucyByZWFkOnJlc291cmNlX3NlcnZlcnMgdXBkYXRlOnJlc291cmNlX3NlcnZlcnMgZGVsZXRlOnJlc291cmNlX3NlcnZlcnMgY3JlYXRlOnJlc291cmNlX3NlcnZlcnMgcmVhZDpkZXZpY2VfY3JlZGVudGlhbHMgdXBkYXRlOmRldmljZV9jcmVkZW50aWFscyBkZWxldGU6ZGV2aWNlX2NyZWRlbnRpYWxzIGNyZWF0ZTpkZXZpY2VfY3JlZGVudGlhbHMgcmVhZDpydWxlcyB1cGRhdGU6cnVsZXMgZGVsZXRlOnJ1bGVzIGNyZWF0ZTpydWxlcyByZWFkOnJ1bGVzX2NvbmZpZ3MgdXBkYXRlOnJ1bGVzX2NvbmZpZ3MgZGVsZXRlOnJ1bGVzX2NvbmZpZ3MgcmVhZDplbWFpbF9wcm92aWRlciB1cGRhdGU6ZW1haWxfcHJvdmlkZXIgZGVsZXRlOmVtYWlsX3Byb3ZpZGVyIGNyZWF0ZTplbWFpbF9wcm92aWRlciBibGFja2xpc3Q6dG9rZW5zIHJlYWQ6c3RhdHMgcmVhZDp0ZW5hbnRfc2V0dGluZ3MgdXBkYXRlOnRlbmFudF9zZXR0aW5ncyByZWFkOmxvZ3MgcmVhZDpzaGllbGRzIGNyZWF0ZTpzaGllbGRzIGRlbGV0ZTpzaGllbGRzIHVwZGF0ZTp0cmlnZ2VycyByZWFkOnRyaWdnZXJzIHJlYWQ6Z3JhbnRzIGRlbGV0ZTpncmFudHMgcmVhZDpndWFyZGlhbl9mYWN0b3JzIHVwZGF0ZTpndWFyZGlhbl9mYWN0b3JzIHJlYWQ6Z3VhcmRpYW5fZW5yb2xsbWVudHMgZGVsZXRlOmd1YXJkaWFuX2Vucm9sbG1lbnRzIGNyZWF0ZTpndWFyZGlhbl9lbnJvbGxtZW50X3RpY2tldHMgcmVhZDp1c2VyX2lkcF90b2tlbnMgY3JlYXRlOnBhc3N3b3Jkc19jaGVja2luZ19qb2IgZGVsZXRlOnBhc3N3b3Jkc19jaGVja2luZ19qb2IgcmVhZDpjdXN0b21fZG9tYWlucyBkZWxldGU6Y3VzdG9tX2RvbWFpbnMgY3JlYXRlOmN1c3RvbV9kb21haW5zIHJlYWQ6ZW1haWxfdGVtcGxhdGVzIGNyZWF0ZTplbWFpbF90ZW1wbGF0ZXMgdXBkYXRlOmVtYWlsX3RlbXBsYXRlcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.z6QOzSTGgCiTXKP4UVcgQulwhvLTAY1ct-hKYwMfpbRoYRfoHKnfPfke4881riknEKH2nr2Q-d4Q6aT_roYxe9qmfLCL6Jq7_nT5bmq2Cgbz8fWTr_lAdjFDdnfAdG3k3_gi5clTOSVb1f5lTWEYn_Pa3Yk45obCP9pJrKC882hayxQkVh7exJ7mL7CoDCGLO_M7RlIxkocpcW1tmRQcb4XQnnj9fKeHnmMRPW6DmnO3nCYyDA7li3ORYIkF9Gp_x6kt12KYaOe7neqtwljdPMsC-2bQWnJ02AGL0JeXGhXtxqSm55ENJLyP2rd4Nff5Ry_4MtFW0-rM6fXTcjDGQQ",
            }
        )
        
        #Script
        
        a=r.json()
    #TODO: FIXME: When token expires, get response and set a negative scenario where the response shows that the authorization is expired and show warning every month
        StatusCode=str(r.status_code)
        Response=r.text
        break
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    if "Expired token" in Response:
        print (Fore.RED+"\tERROR in admin API authorization!!!! "+Fore.RESET)
        print (Fore.RED+"\tPlease Enter a new Authorization token and Retry!! "+Fore.RESET)

        I=input("\tYou can verify email manually and enter (Verified) to proceed: ")
        if "verified" in I.lower() :
            print (Fore.GREEN+"\tEmail is Verified manually, proceeding with the code!! "+Fore.RESET)
        else:
            raise SystemExit
        
    
    if ReportDriver==None:
        print("No Report Driver found")
    else:
        ReportDriver.report().test(name="Verify Email", message="Api calls to Verify Email", passed=True)
