from ast import excepthandler
import requests
import uuid
from selenium.webdriver.support.ui import WebDriverWait # needs to be used when creating a function everytime
from selenium.webdriver.support import expected_conditions # needs to be used when creating a function everytime
from selenium.webdriver.common.by import By
from Constants_Technical_Variables import Constants

def verify_phone_number(driver,portfolio_id):
    
    # try:
    #     home_button = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/a[1]/div'))).click()
    # except:
    #     print("no mobile number validation")

    home_button = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/a[1]/div'))).click()
    confirm_phone_number = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="dashboard"]/div[1]/div/div[2]/button'))).click()
    
    api_name="Verify Phone number"
    url = fConstants.SW_UAT_URL+"development/otp/{portfolio_id}"

    payload={}
    headers = {
    'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'
    }

    response = requests.get(url, headers=headers, data=payload)
    
    print(response.text)
    b = response.json()
    phone_number_otp = b['otp']
    print(phone_number_otp)

    verify_phone_number = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="dashboard"]/div[1]/div/div[2]/div[3]/div/div[2]/div/input')))
    verify_phone_number.send_keys(phone_number_otp)
    confirm_button = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="dashboard"]/div[1]/div/div[3]/button[2]'))).click()
    set_sms_otp = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="dashboard"]/div[1]/div/div[3]/button[2]'))).click()


    

