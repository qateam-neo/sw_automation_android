import json
from time import sleep
import requests
from Constants_Technical_Variables import Constants
from GesturesAndMotions import taponcoordinates

from ManualReport import ReportResultsAPICollection


def ActivateUser(ReportDriver,driver,User_ID):
 
    print("Activating user: ")
    API_Name="Activate User API"
    Amount=10000
    r = requests.post(
        Constants.SW_UAT_URL+"development/activate/"+User_ID,
        data=json.dumps({
            "initial_investment":Amount
            }),
        
        headers={	
                "Authorization": "#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#",
				"Content-Type": "application/json",
				"x-locale": "en_US",
				"x-version": "1.0",
				"x-platform": "web",
                }
    )
    
    #Script
    
    a=r.json()
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
    if ReportDriver==None:
        print("No Report Driver found, Activate user!")
    else:
        ReportDriver.report().test(name="Activate User", message="Api calls to activate user's account", passed=True)
    
    
        #Refresh Application
    driver.press_keycode(3)
    sleep(0.5)
    driver.press_keycode(187)
    sleep(0.5)
    taponcoordinates(driver,550,850)

