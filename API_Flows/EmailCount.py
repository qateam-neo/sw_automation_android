import json
from time import sleep
import requests
from Constants_Technical_Variables import Constants #HTTPS this is HTTP


def EmailCountAPI( ReportDriver,FeatureName,OnboardingFlow,User_Type):
    url = "https://api.nbkcapital-smartwealth.com/api/v2/development/email-count?prefix=roy.braish+"+FeatureName.lower()+FeatureName.lower()+FeatureName.lower()
    payload={}
    headers = {
    'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'
    }
    for i in range(0,2):
        response = requests.request("GET", url, headers=headers, data=payload)
        break
    count = response.json()["count"]
    print(count)
    return count + 1


def EmailCountAPI_SingleUser_ReturnFullEmail( ReportDriver,Email):
    print(Email)
    Prefix=[]
    for i in range(len(Email)-1,0,-1):
        # print(Email[i])
        # print(i)
        # print(Prefix)
        # print("")
        
        if Email[i]=="@":
            for j in range(i-1,-1,-1):
                if Email[j].isdigit():
                    # print("Skip Numbers")
                    sleep(0.1)
                else:
                    Prefix.append(Email[j])
            i=(-3)

    Prefix.reverse()
    FullPrefix="".join(Prefix)
    # print(FullPrefix)
    print(FullPrefix)


    if "+" in FullPrefix:
        url= "https://api.nbkcapital-smartwealth.com/api/v2/development/email-count?prefix="+FullPrefix
    # else:
    #     url= "http://api.nbkcapital-smartwealth.com/api/v2/development/email-count?prefix=roy.braish"+FullPrefix
    payload={}
    headers = {
    'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    
    if response.status_code == 200 or response.status_code == "200" or response.status_code == "201" or response.status_code == 201:
        count = response.json()["count"]
        # print(count)
        Email=FullPrefix+str(int(count)+1)+"@neo.ae"
        
                
        a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        # print(json_object)
        
        json_object["SingleUserDetails"]["Email"] = Email


        a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
        json.dump(json_object, a_file)
        a_file.close()

    return Email