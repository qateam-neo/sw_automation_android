import requests

from Constants_Technical_Variables import Constants

def verify_phone_number(portfolio_id):
    url = Constants.SW_UAT_URL+"development/otp/{portfolio_id}"

    payload={}
    headers = {
    'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)