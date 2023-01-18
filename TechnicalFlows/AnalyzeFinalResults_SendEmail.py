import json
from time import sleep
from SendEmail import SendEmail
from SendSlack import slack_frontend


def AnalyzeFinalResults(Statuses):
    slack=slack_frontend()
    FinalTestPassed=True
    try:
        for ELEM in Statuses:
            if ELEM == False:
                FinalTestPassed=False
                break
            else:
                FinalTestPassed=True
    except:
        if Statuses:
            FinalTestPassed=True
        else:
            FinalTestPassed=False
            
    if FinalTestPassed==True:
        # SendEmail(Passed=True)
        slack.send_results(Passed=True)
        
    else:
        # SendEmail(Passed=False)
        slack.send_results(Passed=False)
            #TODO: Email Template for Failed Report
    sleep(3)
    if FinalTestPassed:
        a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        # print(json_object)
        
        json_object["TechnicalVariables"]["TestisDone"] = "True"

        a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
        json.dump(json_object, a_file)
        a_file.close()
    elif FinalTestPassed == False:
        a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        # print(json_object)
        
        json_object["TechnicalVariables"]["TestisDone"] = "Fail"

        a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
        json.dump(json_object, a_file)
        a_file.close()

    # try:ReportDriver.quit()
    # except:print("Report Driver is not available")