import sys
from time import sleep
import requests
from colorama import Fore
from BlueScreens import Signyourcontract_Blue
from CheckIfPageLoading import CheckIfPageLoading

from ManualReport import ReportResultsAPICollection
from Constants_Technical_Variables import Constants



def SignContractAPI (driver,ReportDriver,User_ID):
       
    #Script
    # print('portfolio_id', portfolio_id)
    CheckIfPageLoading(driver)
    # Signyourcontract_Blue(driver, ReportDriver)
    
    
    Authorization="#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#"
    print("Attempting to sign contract:")
    t=3
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\tPlease Wait "+timer+" more seconds while we sign your Contract...", end="\r")
        sleep(1)
        t -= 1
    ERASE_LINE = '\x1b[2K' 
    sys.stdout.write(ERASE_LINE) 



    
    
    
    API_Name="Sign Contract API"
    r = requests.put(
        Constants.SW_UAT_URL+"development/"+User_ID+"/set-contract-signed",
    
        headers={
            "Authorization":Authorization,
            "Content-Type":"application/json",
            "x-locale":"en_US",
            "x-version":"1.0",
            "x-platform":"web"
                    
        }
    )
    
    
    #Script
    
    a=r.json()
 #TODO: FIXME: When token expires, get response and set a negative scenario where the response shows that the authorization is expired and show warning every month
    StatusCode=r.status_code
    Response=r.text
    # while True:        
    #     try:
    #         WebDriverWait(driver,6).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")))
    #         break
    #     except:
    #         driver.press_keycode(4)
    if StatusCode == 200 or StatusCode == 201 or StatusCode == 202:
        print(Fore.GREEN+'\tContract is signed'+Fore.RESET)
    else:
        print(Fore.RED+'\tIssue in Signing, Contract is not signed'+Fore.RESET)
        print(Fore.RED+'\tError shown was the following: '+Response+Fore.RESET)
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)
