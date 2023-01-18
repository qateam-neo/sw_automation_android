import requests
from selenium.webdriver.support.ui import WebDriverWait # needs to be used when creating a function everytime
from selenium.webdriver.support import expected_conditions # needs to be used when creating a function everytime
from selenium.webdriver.common.by import By
from Constants_Technical_Variables import Constants

def WithdrawalOTP_API(portfolio_id):

    url = Constants.SW_UAT_URL+"development/withdrawal/token/"+portfolio_id

    payload={}
    headers = {
    'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    b = response.json()
    withdrawal_otp = b['otp']
    print(withdrawal_otp)
    
    return withdrawal_otp

