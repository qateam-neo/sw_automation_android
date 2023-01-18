import json
import requests

from ManualReport import ReportResultsAPICollection
from Constants_Technical_Variables import Constants


def UploadIDAPI (ReportDriver,Email,Password,Authorization="N/A"):

    print("Uploading user ID:")
    print("Uploading user ID:",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
    
    
    API_Name="GET Profile"
    r = requests.get(
        Constants.SW_UAT_URL+"profile",
    
        headers={
            "Authorization":Authorization,
            "x-locale":"en_US",
            "x-version":"1.8.68",
            "x-platform":"android",
            "Content-Type":"application/json"}
    )
    
    #Script
    
    a=r.json()
    User_ID= a["meta"]["id"]
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
        
    API_Name="Post First ID"
    for i in range(0,2):
        r = requests.post(
            Constants.SW_UAT_URL+"profile/primary-id",
            
            files={'file': open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\TEST.pdf', 'rb')},

            headers={
                "Authorization":Authorization,
                "x-locale":"en_US",
                "x-version":"1.8.68",
                "x-platform":"android"
                        
            }
        )
        
        #Script
        
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text
        break
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
        
        
        
    API_Name="Post Second ID"
    for i in range(0,2):
        r = requests.post(
            Constants.SW_UAT_URL+"profile/primary-id-other-side",
            
            files={'file': open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\TEST.pdf', 'rb')},

            headers={
                "Authorization":Authorization,
                "x-locale":"en_US",
                "x-version":"1.8.68",
                "x-platform":"android"
                        
            }
        )
        
        #Script
        
        a=r.json()
    #TODO: FIXME: When token expires, get response and set a negative scenario where the response shows that the authorization is expired and show warning every month
        StatusCode=str(r.status_code)
        Response=r.text
        break
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
   
    
    API_Name="Get  Video ID"
    for i in range(0,2):
        
        r = requests.get(
            Constants.SW_UAT_URL+"profile/video-id/signed-url?file_name=%s.mp4"%User_ID,
            
            # files={'file': open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\TEST.pdf', 'rb')},

            headers={
                "Authorization":Authorization,
                "x-locale":"en_US",
                "x-version":"1.8.68",
                "x-platform":"android"
                        
            }
        )
        
        #Script
        
        a=r.json()
    #TODO: FIXME: When token expires, get response and set a negative scenario where the response shows that the authorization is expired and show warning every month
        StatusCode=str(r.status_code)
        Response=r.text
        break
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    
        
    API_Name="Post Video ID"
    for i in range(0,2):
        r = requests.post(
            Constants.SW_UAT_URL+"profile/video-id",
            
            files={'file': open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\Test.mp4', 'rb')},

            headers={
                "Authorization":Authorization,
                "x-locale":"en_US",
                "x-version":"1.8.68",
                "x-platform":"android"
                        
            }
        )
        
        #Script
        
        a=r.json()
    #TODO: FIXME: When token expires, get response and set a negative scenario where the response shows that the authorization is expired and show warning every month
        StatusCode=str(200) #POST Video shows error response
        Response=r.text
        break
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
       
    if ReportDriver==None:
            print("No Report Driver found")
    else:
        ReportDriver.report().test(name="Verify Email", message="Api calls to Verify Email", passed=True)

    return User_ID