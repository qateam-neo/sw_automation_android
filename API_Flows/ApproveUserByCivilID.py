import json
import requests
from BlueScreens import Signyourcontract_Blue
from selenium.webdriver.support.ui import WebDriverWait # needs to be used when creating a function everytime
from selenium.webdriver.support import expected_conditions # needs to be used when creating a function everytime
from selenium.webdriver.common.by import By
from Constants_Technical_Variables import Constants


from ManualReport import ReportResultsAPICollection # needs to be used when creating a function everytime

def ApproveUserByCivilID(driver,ReportDriver,Credentials):

    # try:
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/btn_book")))
    #     driver.press_keycode(4)
    # except:
    #     print("Page stuck!!")
        
    # print("Approving user from Admin: ")
    
        #KYC
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)
            
    API_Name="Approve user"
    r = requests.post(
        Constants.SW_UAT_URL+"external/project-connect/dev/profile/approve",
    
        data=json.dumps({
            "civil_id_number": JSON["KYC_3.0"]["PersonalInfo_Fields"]["CivilID"]
           }),
        headers={
            "Content-Type":"application/json"
        }
    )
    

    a=r.json()
    # print(a)
    StatusCode=str(r.status_code)
    Response=r.text
    ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response)

    while True:
        try:
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvTime")
            break
        except:
            try:driver.press_keycode(4)
            except:print("The back hasn't clicked (press_keycode 4)")