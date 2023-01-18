 

# case = client.send_get('get_results/5')
# print(case)
# result = client.send_post(
#             'add_result_for_case/%s/%s'%("R5","T262"),
#             {'status_id': 1, 'comment': "Testing is succes works...." })
# import dotenv,os,testrail
# import Conf_Reader
 
import json
from time import sleep
import requests

from SaveJSONFile import SaveJSONFile

def GetCases(run_id="FromJSON"):
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)
    if run_id == "FromJSON":
        run_id=JSON["TestRailSmokeTests"]["run_id"]
    if JSON["TestRailSmokeTests"]["Status"]=="enabled":
        for i in range(0,2):
            r = requests.get(
            "https://neoteam.testrail.io/index.php?/api/v2/get_tests/"+str(run_id),
            
            # data=payload,
            
            headers={	
                    'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                    "Content-Type": "application/json"
                }
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            # print(Response)
            # print("\n\n")
            break

    Predefined_ETF = []
    Customized_ETF = []
    Predefined_Islamic = []
    Customized_Islamic = []
    Active_onboarded_MMF =[]
    Offline_USD_NBK_Fund =[]
    Offline_KD_NBK_Fund =[]


    # print(StatusCode)

    for MiniJSON in a["tests"]:
        # print(MiniJSON)
        if MiniJSON["sections_display_order"]==2:
            Predefined_ETF.append(MiniJSON["case_id"])
        elif MiniJSON["sections_display_order"]==3:
            Customized_ETF.append(MiniJSON["case_id"])
        elif MiniJSON["sections_display_order"]==4:
            Predefined_Islamic.append(MiniJSON["case_id"])
        elif MiniJSON["sections_display_order"]==5:
            Customized_Islamic.append(MiniJSON["case_id"])
        elif MiniJSON["sections_display_order"]==7:
            Active_onboarded_MMF.append(MiniJSON["case_id"])
        elif MiniJSON["sections_display_order"]==8:
            Offline_USD_NBK_Fund.append(MiniJSON["case_id"])
        elif MiniJSON["sections_display_order"]==9:
            Offline_KD_NBK_Fund.append(MiniJSON["case_id"])
            
            
    Predefined_ETF_Titles = []
    Customized_ETF_Titles = []
    
    Predefined_Islamic_Titles = []
    Customized_Islamic_Titles = []
    
    Active_onboarded_MMF_Titles =[]
    Offline_USD_NBK_Fund_Titles =[]
    Offline_KD_NBK_Fund_Titles =[]


    for MiniJSON in a["tests"]:
        if MiniJSON["sections_display_order"]==2:
            Predefined_ETF_Titles.append(MiniJSON["title"])
        elif MiniJSON["sections_display_order"]==3:
            Customized_ETF_Titles.append(MiniJSON["title"])
        elif MiniJSON["sections_display_order"]==4:
            Predefined_Islamic_Titles.append(MiniJSON["title"])
        elif MiniJSON["sections_display_order"]==5:
            Customized_Islamic_Titles.append(MiniJSON["title"])
        elif MiniJSON["sections_display_order"]==7:
            Active_onboarded_MMF_Titles.append(MiniJSON["title"])
        elif MiniJSON["sections_display_order"]==8:
            Offline_USD_NBK_Fund_Titles.append(MiniJSON["title"])
        elif MiniJSON["sections_display_order"]==9:
            Offline_KD_NBK_Fund_Titles.append(MiniJSON["title"])


    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    # print(json_object)

    json_object["TestRailSmokeTests"]["TestCases"]["Cases_ids"]["Predefined_ETF"] = Predefined_ETF
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_ids"]["Customized_ETF"] = Customized_ETF
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_ids"]["Predefined_Islamic"] = Predefined_Islamic
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_ids"]["Customized_Islamic"] = Customized_Islamic
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_ids"]["Active_onboarded_MMF"] = Active_onboarded_MMF
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_ids"]["Offline_USD_NBK_Fund"] = Offline_USD_NBK_Fund
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_ids"]["Offline_KD_NBK_Fund"] = Offline_KD_NBK_Fund

    json_object["TestRailSmokeTests"]["TestCases"]["Cases_titles"]["Predefined_ETF_Titles"] = Predefined_ETF_Titles
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_titles"]["Customized_ETF_Titles"] = Customized_ETF_Titles
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_titles"]["Predefined_Islamic_Titles"] = Predefined_Islamic_Titles
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_titles"]["Customized_Islamic_Titles"] = Customized_Islamic_Titles
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_titles"]["Active_onboarded_MMF_Titles"] = Active_onboarded_MMF_Titles
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_titles"]["Offline_USD_NBK_Fund_Titles"] = Offline_USD_NBK_Fund_Titles
    json_object["TestRailSmokeTests"]["TestCases"]["Cases_titles"]["Offline_KD_NBK_Fund_Titles"] = Offline_KD_NBK_Fund_Titles



    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


def AnalyzeTestTrailResults(User_Type,OnboardingFlow,RiskScore=None,Status=None):
    print("User type: " + User_Type)
    print("Onboarding flow: " + OnboardingFlow)
    if User_Type.lower() == "etf" and OnboardingFlow.lower() == "predefined":
        TestRailReportSuccess("Predefined_ETF")
    if User_Type.lower() == "islamic" and OnboardingFlow.lower() == "predefined":
        TestRailReportSuccess("Predefined_Islamic")
    if User_Type.lower() == "etf" and OnboardingFlow.lower() == "customized":
        TestRailReportSuccess("Customized_ETF")
    if User_Type.lower() == "islamic" and OnboardingFlow.lower() == "customized":
        TestRailReportSuccess("Customized_Islamic")
    if User_Type.lower() == "offline" and OnboardingFlow.lower() == "n/a":
        TestRailReportSuccess("Offline_USD_NBK_Fund")
        TestRailReportSuccess("Offline_KD_NBK_Fund")
        TestRailReportSuccess("Active_onboarded_MMF")        

def AnalyzeTestTrailResults_Retest(User_Type,OnboardingFlow,ErrorMessage,RiskScore=None,Status=None):
    print("User type: " + User_Type)
    print("Onboarding flow: " + OnboardingFlow)
    
    if User_Type.lower() == "etf" and OnboardingFlow.lower() == "predefined":
        TestRailReportRetest("Predefined_ETF",ErrorMessage)
        
    if User_Type.lower() == "islamic" and OnboardingFlow.lower() == "predefined":
        TestRailReportRetest("Predefined_Islamic",ErrorMessage)
        
    if User_Type.lower() == "etf" and OnboardingFlow.lower() == "customized":
        TestRailReportRetest("Customized_ETF",ErrorMessage)
        
    if User_Type.lower() == "islamic" and OnboardingFlow.lower() == "customized":
        TestRailReportRetest("Customized_Islamic",ErrorMessage)
        
    if User_Type.lower() == "offline" and OnboardingFlow.lower() == "n/a":
        TestRailReportRetest("Offline_USD_NBK_Fund",ErrorMessage)
        TestRailReportRetest("Offline_KD_NBK_Fund",ErrorMessage)
        TestRailReportRetest("Active_onboarded_MMF",ErrorMessage)        

def AnalyzeTestTrailResults_Fail(User_Type,OnboardingFlow,ErrorMessage,RiskScore=None,Status=None):
    print("User type: " + User_Type)
    print("Onboarding flow: " + OnboardingFlow)
    
    if User_Type.lower() == "etf" and OnboardingFlow.lower() == "predefined":
        TestRailReportFail("Predefined_ETF",ErrorMessage)
        
    if User_Type.lower() == "islamic" and OnboardingFlow.lower() == "predefined":
        TestRailReportFail("Predefined_Islamic",ErrorMessage)
        
    if User_Type.lower() == "etf" and OnboardingFlow.lower() == "customized":
        TestRailReportFail("Customized_ETF",ErrorMessage)
        
    if User_Type.lower() == "islamic" and OnboardingFlow.lower() == "customized":
        TestRailReportFail("Customized_Islamic",ErrorMessage)
        
    if User_Type.lower() == "offline" and OnboardingFlow.lower() == "n/a":
        TestRailReportFail("Offline_USD_NBK_Fund",ErrorMessage)
        TestRailReportFail("Offline_KD_NBK_Fund",ErrorMessage)
        TestRailReportFail("Active_onboarded_MMF",ErrorMessage)        



def TestRailReportSuccess(Section,TestCases=[True],comments=None):
    
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)
    # if UserType.lower() == "etf_predefined":
    #     global payload
    SingleCase=JSON["TestRailSmokeTests"]["SingleCase"]
    SingleTestID=JSON["TestRailSmokeTests"]["SingleTestID"]
    payload={"results":[]}
    
    print("TestRail Reported:")
    print("TestRail Reported:", file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
    sleep(0.5)
    # print(json.dumps(payload))
    
    if SingleCase=="True":
        for Test_ID in SingleTestID:
            
            payloadSingleUser={
                                "status_id": 1,
                                "assignedto_id": 2,
                                "comment": "This test Passed as expected",
                                "version": JSON["TechnicalVariables"]["BuildName"],
                            }
            for i in range(0,2):
                print(Test_ID)
                r = requests.post(
                        "https://neoteam.testrail.io/index.php?/api/v2/add_result/"+str(Test_ID),
                        
                        data=json.dumps(payloadSingleUser),
                        
                        headers={	
                                'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                                "Content-Type": "application/json"
                        }
                    )
                        
                        #Script
                print(json.dumps(payloadSingleUser))      
                a=r.json()
                StatusCode=str(r.status_code)
                Response=r.text
                
                print(StatusCode)
                print(Response)

                break
            if JSON["TestRailSmokeTests"]["SingleTestCaseTitle"] ==False and len(JSON["TestRailSmokeTests"]["SingleTestCaseID"])>1:
                text=""
                Titles=[]
                Cases=JSON["TestRailSmokeTests"]["SingleTestCaseID"]
                Cases=Cases.split(",")
                for elem in Cases:
                    x=GetTestCaseTitle(elem)
                    Titles.append(x)
                    text=text+ x+"\n"
                SaveJSONFile("TestRailSmokeTests,SingleTestCaseTitle",Titles)
                print("\t"+x,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            elif JSON["TestRailSmokeTests"]["SingleTestCaseTitle"]==False and len(JSON["TestRailSmokeTests"]["SingleTestCaseID"])==1:
                x=GetTestCaseTitle(JSON["TestRailSmokeTests"]["SingleTestCaseID"])
                SaveJSONFile("TestRailSmokeTests,SingleTestCaseTitle",x)
                print("\t"+x,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

    else:       
        run_id=JSON["TestRailSmokeTests"]["run_id"]
        for i in range(0,len(JSON["TestRailSmokeTests"]["TestCases"]["Cases_ids"][Section])):
            payload["results"].append(
                {
                    "case_id": str(JSON["TestRailSmokeTests"]["TestCases"]["Cases_ids"][Section][i]),
                    "status_id": 1,
                    "assignedto_id": 2,
                    "comment": "This test Passed as expected",
                    "version":JSON["TechnicalVariables"]["BuildName"]

                })
        for i in range(0,2):
            
            r = requests.post(
                    "https://neoteam.testrail.io/index.php?/api/v2/add_results_for_cases/"+str(run_id),
                    
                    data=json.dumps(payload),
                    
                    headers={	
                            'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                            "Content-Type": "application/json"
                    }
                )
                    
                    #Script
                    
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            
            # print(StatusCode)
            # print(Response)

            break
        if SingleCase=="False":
        
            if Section == "Predefined_ETF":
                temp=0
            elif Section == "Customized_ETF":
                temp=1
            elif Section == "Predefined_Islamic":
                temp=2
            elif Section == "Customized_Islamic":
                temp=3
            
            

            for i in range(0,len(JSON["TestRailSmokeTests"]["TestCases"]["Cases_titles"][Section+"_Titles"])):
                print("\t"+JSON["TestRailSmokeTests"]["TestCases"]["Cases_titles"][Section+"_Titles"][i],file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

    
def TestRailReportFail(Section,ErrorMessage,TestCases=[True],comments=None):

    
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)
    # if UserType.lower() == "etf_predefined":
    #     global payload
    SingleCase=JSON["TestRailSmokeTests"]["SingleCase"]
    SingleTestID=JSON["TestRailSmokeTests"]["SingleTestID"]

    payload={"results":[]}

    print("TestRail Reported:")
    print("TestRail Reported:", file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
    sleep(0.5)
    # print(json.dumps(payload))
    count=(-1)
    if SingleCase=="True":
        for Test_ID in SingleTestID:
            
            payloadSingleUser={
                                "status_id": 5,
                                "assignedto_id": 2,
                                "comment": ErrorMessage,
                                "version": JSON["TechnicalVariables"]["BuildName"],
                            }
            for i in range(0,2):

                r = requests.post(
                        "https://neoteam.testrail.io/index.php?/api/v2/add_result/"+str(Test_ID),
                        
                        data=json.dumps(payloadSingleUser),
                        
                        headers={	
                                'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                                "Content-Type": "application/json"
                        }
                    )
                        
                        #Script
                
                print(json.dumps(payloadSingleUser))      
                a=r.json()
                StatusCode=str(r.status_code)
                Response=r.text
                
                print(StatusCode)
                # print(Response)

                break
            count=count+1
            print("\t"+JSON["TestRailSmokeTests"]["SingleTestCaseTitle"][count],file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

    else:
        run_id=JSON["TestRailSmokeTests"]["run_id"]
        for i in range(0,len(JSON["TestRailSmokeTests"]["TestCases"]["Cases_ids"][Section])):
            payload["results"].append(
                {
                    "case_id": str(JSON["TestRailSmokeTests"]["TestCases"]["Cases_ids"][Section][i]),
                    "status_id": 5,
                    "assignedto_id": 2,
                    "comment": "This test Failed",
                    "version":JSON["TechnicalVariables"]["BuildName"]

                })
        for i in range(0,2):
            
            r = requests.post(
                    "https://neoteam.testrail.io/index.php?/api/v2/add_results_for_cases/"+str(run_id),
                    
                    data=json.dumps(payload),
                    
                    headers={	
                            'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                            "Content-Type": "application/json"
                    }
                )
                    
                    #Script
                    
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            
            # print(StatusCode)
            # print(Response)

            break
        if SingleCase=="False":
        
            if Section == "Predefined_ETF":
                temp=0
            elif Section == "Customized_ETF":
                temp=1
            elif Section == "Predefined_Islamic":
                temp=2
            elif Section == "Customized_Islamic":
                temp=3
            
            

            for i in range(0,len(JSON["TestRailSmokeTests"]["TestCases"]["Cases_titles"][Section+"_Titles"])):
                print("\t"+JSON["TestRailSmokeTests"]["TestCases"]["Cases_titles"][Section+"_Titles"][i],file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
    

def TestRailReportRetest(Section,ErrorMessage="This user failed, we're retesting now...",TestCases=[True],comments=None):
    
    
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)
    # if UserType.lower() == "etf_predefined":
    #     global payload
    SingleCase=JSON["TestRailSmokeTests"]["SingleCase"]
    SingleTestID=JSON["TestRailSmokeTests"]["SingleTestID"]

    payload={"results":[]}

    print("TestRail Reported:")
    print("TestRail Reported:", file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
    sleep(0.5)
    # print(json.dumps(payload))
    count=(-1)
    if SingleCase=="True":
        for Test_ID in SingleTestID:
            
            payloadSingleUser={
                                "status_id": 4,
                                "assignedto_id": 2,
                                "comment": ErrorMessage,
                                "version": JSON["TechnicalVariables"]["BuildName"],
                            }
            for i in range(0,2):

                r = requests.post(
                        "https://neoteam.testrail.io/index.php?/api/v2/add_result/"+str(Test_ID),
                        
                        data=json.dumps(payloadSingleUser),
                        
                        headers={	
                                'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                                "Content-Type": "application/json"
                        }
                    )
                        
                        #Script
                
                print(json.dumps(payloadSingleUser))      
                a=r.json()
                StatusCode=str(r.status_code)
                Response=r.text
                
                print(StatusCode)
                # print(Response)

                break
            count=count+1
            print("\t"+JSON["TestRailSmokeTests"]["SingleTestCaseTitle"][count],file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

    else:
        run_id=JSON["TestRailSmokeTests"]["run_id"]
        for i in range(0,len(JSON["TestRailSmokeTests"]["TestCases"]["Cases_ids"][Section])):
            payload["results"].append(
                {
                    "case_id": str(JSON["TestRailSmokeTests"]["TestCases"]["Cases_ids"][Section][i]),
                    "status_id": 5,
                    "assignedto_id": 2,
                    "comment": "This test Failed",
                    "version":JSON["TechnicalVariables"]["BuildName"]

                })
        for i in range(0,2):
            
            r = requests.post(
                    "https://neoteam.testrail.io/index.php?/api/v2/add_results_for_cases/"+str(run_id),
                    
                    data=json.dumps(payload),
                    
                    headers={	
                            'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                            "Content-Type": "application/json"
                    }
                )
                    
                    #Script
                    
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            
            # print(StatusCode)
            # print(Response)

            break
        if SingleCase=="False":
        
            if Section == "Predefined_ETF":
                temp=0
            elif Section == "Customized_ETF":
                temp=1
            elif Section == "Predefined_Islamic":
                temp=2
            elif Section == "Customized_Islamic":
                temp=3
            
            

            for i in range(0,len(JSON["TestRailSmokeTests"]["TestCases"]["Cases_titles"][Section+"_Titles"])):
                print("\t"+JSON["TestRailSmokeTests"]["TestCases"]["Cases_titles"][Section+"_Titles"][i],file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))


def GetTestCaseTitle(Case_id):
    for i in range(0,2):
        
        r = requests.get(
            "https://neoteam.testrail.io/index.php?/api/v2/get_case/"+str(Case_id),
                
                # data=json.dumps(payload),
                
                headers={	
                        'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                        "Content-Type": "application/json"
                }
            )
                
                #Script
                
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text
        
        print(StatusCode)
        # print(Response)
        break
    if StatusCode == 200 or StatusCode =="200":
        print(a["title"])
        return a["title"]
    else:
        return False


def GetTestRunTitle(Run_ID):
    for i in range(0,2):
        
        r = requests.get(
            "https://neoteam.testrail.io/index.php?/api/v2/get_run/"+str(Run_ID),
                
                # data=json.dumps(payload),
                
                headers={	
                        'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                        "Content-Type": "application/json"
                }
            )
                
                #Script
                
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text
        
        print(StatusCode)
        print(Response)

        break
    if StatusCode == 200 or StatusCode =="200":
        return a["name"]
    else:
        return False
    
    
def GetProjectRuns():
    Android_Project_ID=2
    for i in range(0,2):
        
        r = requests.get(
            "https://neoteam.testrail.io/index.php?/api/v2/get_runs/"+str(Android_Project_ID),
                
                # data=json.dumps(payload),
                
                headers={	
                        'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                        "Content-Type": "application/json"
                }
            )
                
                #Script
                
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text
        
        print(StatusCode)
        # print(Response)
        break

    if StatusCode == 200 or StatusCode =="200":
        ActiveRunsID=[]
        ActiveRunsURL=[]
        for ELEM in a["runs"]:
            if ELEM["is_completed"]==False:
                ActiveRunsID.append(ELEM["id"])
                ActiveRunsURL.append(ELEM["url"])
        return ActiveRunsID
    else:
        return False
        
        
def GetTestRunCases(Run_ID,ExpectedTestCase="N/A"):
    
    for i in range(0,2):
        r = requests.get(
        "https://neoteam.testrail.io/index.php?/api/v2/get_tests/"+str(Run_ID),
        
        # data=payload,
        
        headers={	
                'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                "Content-Type": "application/json"
            }
        )
        
        #Script
        
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text
        # print(StatusCode)
        # print(Response)
        break
    
    Cases=[]
    TestID=[]
    for MiniJSON in a["tests"]:
        Cases.append(MiniJSON["case_id"])
        TestID.append(MiniJSON["id"])
    if StatusCode == 200 or StatusCode =="200":
        return [Cases,TestID]
    else:
        return False
 
 
def Return_TestID_from_CaseID(Run_ID,ExpectedCaseID):

    for i in range(0,2):
        r = requests.get(
        "https://neoteam.testrail.io/index.php?/api/v2/get_tests/"+str(Run_ID),
        
        # data=payload,
        
        headers={	
                'Authorization': 'Basic cWF0ZWFtQG5lby5hZTpuZW9AUUFfc2pzajl5d3k=',
                "Content-Type": "application/json"
            }
        )
         
        #Script
        
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text
        print(StatusCode)
        # print(Response)
        break
    
   
    for MiniJSON in a["tests"]:
        # print(MiniJSON["case_id"])
        # print(str(ExpectedCaseID))
        if str(MiniJSON["case_id"])==str(ExpectedCaseID):
            return MiniJSON["id"]
    return False
       
       
def GetTestCaseURL(Case_ID="FromJSON"):
    
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)

    if JSON["TestRailSmokeTests"]["Status"].lower() == "enabled":TestRail=True
    else : TestRail=False
    if "true" in JSON["TestRailSmokeTests"]["SingleCase"].lower() and TestRail:

        if Case_ID=="FromJSON":
            Case_ID=JSON["TestRailSmokeTests"]["SingleTestCaseID"]
            
        if "," in Case_ID:
            Case_ID=Case_ID.split(",")
            Case_ID=Case_ID[0]
            print(Case_ID)
        Runs=GetProjectRuns()
        
        for Run in Runs:
            print(Run)
            print(Case_ID)
            TestCaseID=Return_TestID_from_CaseID(Run,Case_ID)
            # print(TestCaseID)
        if TestCaseID!=False and len(JSON["TestRailSmokeTests"]["SingleTestCaseID"])>1:
            print ("Please access your Test Cases here: https://neoteam.testrail.io/index.php?/runs/view/"+str(Run)) 
            return "https://neoteam.testrail.io/index.php?/tests/view/"+str(Run)

        else:
            print ("Please access the Test Case here: https://neoteam.testrail.io/index.php?/tests/view/"+str(TestCaseID)) 
            return "https://neoteam.testrail.io/index.php?/tests/view/"+str(TestCaseID)
    elif TestRail:
        return "https://neoteam.testrail.io/index.php?/runs/view/"+str(JSON["TestRailSmokeTests"]["run_id"])
    else: return False
    


def SaveTestsIDJSON(Case_ID="FromJSON"):
    
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)
    # if UserType.lower() == "etf_predefined":
    if Case_ID=="FromJSON":
        Case_ID=JSON["TestRailSmokeTests"]["SingleTestCaseID"]
        
    # if "," in Case_ID:
    #     Case_ID=Case_ID.split(",")
    #     # print(Case_ID)
    # else:
    #     Case_ID=[Case_ID]
    Runs=GetProjectRuns()
    # print(Runs)
    testIDs=""
    print(Runs)
    print(Case_ID)
    for Run in Runs:
        for case in Case_ID:
            print(Run)
            print(case)
            TestCaseID=Return_TestID_from_CaseID(Run,case)
            print(TestCaseID)
            if TestCaseID!=False:
                testIDs=testIDs+str(TestCaseID)+","
                # print(testIDs)
                print(len(Case_ID)+1)
                print(len(testIDs.split(",")))
                if len(Case_ID)+1==len(testIDs.split(",")):
                    testIDs=testIDs[0:len(testIDs)-1]
                    print(testIDs)
                    
                
        print(len(Case_ID)+1)
        print(len(testIDs.split(",")))
        if len(Case_ID)+1==len(testIDs.split(",")):
            break
        
    testIDs=testIDs.split(",")
    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    # print(json_object)

    json_object["TestRailSmokeTests"]["SingleTestID"] = testIDs

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

def SaveTestCase_Run_URL(TestCase_ID="FromJSON",Run_ID="FromJSON"):
    
    sleep(2)
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)

    if JSON["TestRailSmokeTests"]["Status"].lower() == "enabled":TestRail=True
    else : TestRail=False
    if "true" in JSON["TestRailSmokeTests"]["SingleCase"].lower() and TestRail:

        if TestCase_ID=="FromJSON":
            Case_ID=JSON["TestRailSmokeTests"]["SingleTestCaseID"]
        else:
            Case_ID=TestCase_ID

        Case_ID=Case_ID[0]
        print(Case_ID)

        Runs=GetProjectRuns()
        print (Runs)
        for Run in Runs:
            print(Run)
            # print(JSON["TestRailSmokeTests"]["SingleTestCaseID"])
            TestCaseID=Return_TestID_from_CaseID(Run,Case_ID)
            print(TestCaseID)
            if TestCaseID!=False and len(JSON["TestRailSmokeTests"]["SingleTestCaseID"])>1:
                URL= "https://neoteam.testrail.io/index.php?/runs/view/"+str(Run)
                break
            
            elif TestCaseID!=False and len(JSON["TestRailSmokeTests"]["SingleTestCaseID"])==1:
                URL= "https://neoteam.testrail.io/index.php?/tests/view/"+str(TestCaseID)
                break
    elif TestRail:
        URL= "https://neoteam.testrail.io/index.php?/runs/view/"+str(JSON["TestRailSmokeTests"]["run_id"])

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    # print(json_object)

    try:json_object["TestRailSmokeTests"]["URL"] = URL
    except: print("Skipped URL")
    
    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

def SaveRun_TestCasesTitles(Run="FromJSON"):
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSON=json.load(file)
    # if UserType.lower() == "etf_predefined":
    if Run=="FromJSON":
        Run=JSON["TestRailSmokeTests"]["run_id"]

    