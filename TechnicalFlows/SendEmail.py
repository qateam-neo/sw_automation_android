# from email import encoders
# from email.mime.application import MIMEApplication
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# import smtplib
# from email.mime.text import MIMEText
# from colorama import Fore
import requests
import json
from colorama import Fore
from trycourier import Courier


def SendEmail(Passed,EmailTO="roy.braish@neo.ae",User_Type="N/A", RiskScore="N/A",OnboardingFlow="N/A",EmailFROM="roy.braish@neo.ae"):


    if Passed:
        url = "https://api.courier.com/send"

        payload = {
        "message": {
            "template": "RS3AVR4T5Q4J4GKGWDWD3Y3H4B82",
            "to": {
            "email": "roy.braish@neo.ae"
            }
        }
        }
        headers = {
        "Authorization":"Bearer pk_test_9NQ9RFP981MEEVGDHV2QZ9BQRH9N"    ,
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.status_code)
        
    elif Passed==False and (User_Type =="N/A" or OnboardingFlow == "N/A" or RiskScore=="N/A"):
        
        url = "https://api.courier.com/send"

        payload = {
        "message": {
            "template": "RVFS3043PNMHR9M6YSDCVS2HEH54",
            "to": {
            "email": "roy.braish@neo.ae"
            },
            "data": {
                "user_type":User_Type,
                "RiskScore": RiskScore,
                "OnboardingFlow":OnboardingFlow
                }
        }
        }
        headers = {
        "Authorization":"Bearer pk_prod_RHHQFJ0M2Q43CJHPPTBZE6RJ71DN"    ,
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        
        if response.status_code == 200 or response.status_code==201  or response.status_code==202:
            print(Fore.GREEN+"Test is Done and Email is Send!!"+Fore.RESET)
        else:
            print(Fore.YELLOW+"Test is Done and Email is NOT Sent!!"+Fore.RESET)

    
    else:
        url = "https://api.courier.com/send"

        payload = {
        "message": {
            "template": "4F4FJNSSCRMW05N0XV7WD85G6PF7",
            "to": {
            "email": "roy.braish@neo.ae"
            },
            "data": {
                "user_type":User_Type,
                "RiskScore": RiskScore,
                "OnboardingFlow":OnboardingFlow
                }
        }
        }
        headers = {
        "Authorization":"Bearer pk_prod_RHHQFJ0M2Q43CJHPPTBZE6RJ71DN"    ,
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        
        if response.status_code == 200 or response.status_code==201  or response.status_code==202:
            print(Fore.GREEN+"Test is Done and Email is Send!!"+Fore.RESET)
        else:
            print(Fore.YELLOW+"Test is Done and Email is NOT Sent!!"+Fore.RESET)


#             # data={"variables":"awesomeness"}
#         )

#         client = Courier(auth_token="pk_prod_RHHQFJ0M2Q43CJHPPTBZE6RJ71DN")

#         r = client.send_message(
#         message={
#             "to": {EmailTO},
#             "template": "RS3AVR4T5Q4J4GKGWDWD3Y3H4B82",

#         }
#         )

    
#         #Script
    
#     a=r.json()
# #TODO: FIXME: When token expires, get response and set a negative scenario where the response shows that the authorization is expired and show warning every month
#     StatusCode=str(r.status_code)
#     Response=r.text
# #         # while True:        
# #         #     try:
# #         #         WebDriverWait(driver,6).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")))
# #         #         break
# #         #     except:
# #         #         driver.press_keycode(4)
#     print(StatusCode)    
#     if StatusCode == 200 or StatusCode == 201 :
#         print(Fore.GREEN+'\tContract is signed'+Fore.RESET)
#     else:
#         print(Fore.RED+'\tIssue in Signing, Contract is not signed'+Fore.RESET)
#         print(Fore.RED+'\tError shown was the following: '+Response+Fore.RESET)
    # client = Courier(auth_token="pk_prod_RHHQFJ0M2Q43CJHPPTBZE6RJ71DN")

    # resp = client.send_message(
    # message=json.dumps(list({
    #     "to": {"roy.braish@neo.ae"},
    #     "template": "RS3AVR4T5Q4J4GKGWDWD3Y3H4B82",
    #     "data": {
    #     "variables": "awesomeness",
    #     },
    # }))
    # )

    # print(resp['requestId'])