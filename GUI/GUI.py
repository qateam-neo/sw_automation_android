import sys

sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\GUI")
import SystemPathGUI
print(sys.path)
from cgitb import text
from datetime import datetime
import json
from logging import PlaceHolder
import os
from time import sleep
from tkinter import *
from tkinter.ttk import *
import natsort
import tkinter as tk
from TestRailReporting import GetTestCaseTitle, GetTestRunTitle



# creating main tkinter window/toplevel
with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
# Load its content and make a new dictionary
    JSONFile=json.load(file)

    
def GITPULLAnswer():
    global GIT_Answer
    GIT_Answer=GIT.get()
    
    if GIT.get() and JSONModified.get() and BuildName.get() and TextDone.get() and BuildName.get()!="Choose Build Here" and (TestType.get()=="Full Smoke Tests" or (TestType.get()=="Single User Test" and UserType.get() != "User Type" and OnboardingFlow != "Onboarding Flow" and RiskScore != "Risk Score" and InitialDepositMethod.get()!="Initial Deposit Method") )and ((TestType.get()=="Single User Test" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Report Using TestRail" and RunIDDone.get()) or ((TestType.get()=="Single User Test" and ReportingOption.get()=="Report Using TestRail" and caseIDDone.get()))):
        DoneButton.config(state="enabled")
    else:
        DoneButton.config(state="disabled")
             
def JSONAnswer():
    global JSON
    JSON=JSONModified.get()
    
    if GIT.get() and JSONModified.get() and BuildName.get() and TextDone.get() and BuildName.get()!="Choose Build Here" and (TestType.get()=="Full Smoke Tests" or (TestType.get()=="Single User Test" and UserType.get() != "User Type" and OnboardingFlow != "Onboarding Flow" and RiskScore != "Risk Score" and InitialDepositMethod.get()!="Initial Deposit Method") )and ((TestType.get()=="Single User Test" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Report Using TestRail" and RunIDDone.get()) or ((TestType.get()=="Single User Test" and ReportingOption.get()=="Report Using TestRail" and caseIDDone.get()))):
        DoneButton.config(state="enabled")
    else:
        DoneButton.config(state="disabled")

def TestRailFun(m):
    global TestRailAnswer
    TestRailAnswer= ReportingOption.get()
    if TestRailAnswer == "Report Using TestRail"and TestType.get()=="Full Smoke Tests":
        RunidEntry.grid(row=0,column=8, sticky=W)
        Testraillabel.grid(row = 0, column = 7, sticky = W)
        runidcheckbox.grid(row = 0, column = 9,pady = 3)
        Testraillabel.config(text="Run_id:")
        
        caseidcheckbox.grid_forget()
        caseidEntry.grid_forget()
        caseiderrorlabel.grid_forget() 
        CaseIDInfoLabel.grid_forget()



    elif TestRailAnswer=="Report Using TestRail" and TestType.get()=="Single User Test":
        caseidEntry.grid(row = 0,column = 8, sticky=W)
        caseidcheckbox.grid(row = 0,column = 9, sticky=W)
        caseiderrorlabel.grid(row = 1, column = 6, sticky = W,columnspan=4)
        if caseIDDone.get()==False:CaseIDInfoLabel.grid(row=0,column=6,columnspan=2,sticky=S)
        Testraillabel.grid(row = 0,column = 7, sticky=W)
        Testraillabel.config(text="Case_id:")
        
        RunidEntry.grid_forget()
        runidcheckbox.grid_forget()
        runiderrorlabel.grid_forget()

        

    elif TestRailAnswer != "Report Using TestRail"and(TestType.get()=="Full Smoke Tests" or TestType.get()=="Single User Test") :
        RunidEntry.grid_forget()
        runidcheckbox.grid_forget()
        runiderrorlabel.grid_forget()

        Testraillabel.grid_forget()

        caseidcheckbox.grid_forget()
        caseidEntry.grid_forget()
        caseiderrorlabel.grid_forget()
        CaseIDInfoLabel.grid_forget()

    # elif TestRailAnswer != "Report Using TestRail"and TestType.get()=="Single User Test":
    #     caseidcheckbox.grid_forget()
    #     Testraillabel.grid_forget()
    #     caseidEntry.grid_forget()
    #     caseidEntry.grid_forget()
    #     caseidcheckbox.grid_forget()

    else:
        caseidcheckbox.grid_forget()
        Testraillabel.grid_forget()
        caseidEntry.grid_forget()
        CaseIDInfoLabel.grid_forget()

    print(ReportingOption.get())

    if GIT.get() and JSONModified.get() and BuildName.get() and TextDone.get() and BuildName.get()!="Choose Build Here" and (TestType.get()=="Full Smoke Tests" or (TestType.get()=="Single User Test" and UserType.get() != "User Type" and OnboardingFlow != "Onboarding Flow" and RiskScore != "Risk Score" and InitialDepositMethod.get()!="Initial Deposit Method") )and ((TestType.get()=="Single User Test" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Report Using TestRail" and RunIDDone.get()) or ((TestType.get()=="Single User Test" and ReportingOption.get()=="Report Using TestRail" and caseIDDone.get()))):
        DoneButton.config(state="enabled")
    else:
        DoneButton.config(state="disabled")

def ValidateRunID():
    Enter=True
    
    if run_id.get()=="" and RunIDDone.get():
        RunIDDone.set(False)
        
        RunidEntry.config(state='normal',background="red")
 
        RunidEntry.focus_set()
        
        runiderrorlabel.config(font=("TkDefaultFont", 8),foreground="red",text="Run ID can't be empty!")

    elif " " in run_id.get() or "-" in run_id.get() or run_id.get().isdigit()==False :
        RunIDDone.set(False)
        
        RunidEntry.config(state='normal',background="red")
 
        RunidEntry.focus_set()
        
        runiderrorlabel.config(font=("TkDefaultFont", 8),foreground="red",text="Run ID should be an Integer!")
    elif run_id.get() !="" and RunIDDone.get():

        RunidEntry.config(state="readonly")
        runiderrorlabel.config(font=("TkDefaultFont", 8),foreground="green",text="")
        
    elif RunIDDone.get() ==False:
        RunidEntry.config(state='normal',background="white")
        runiderrorlabel.config(text="")
        Enter=False
   

    if RunIDDone.get() and Enter:
        x=GetTestRunTitle(run_id.get())
        if x!=False:
            runiderrorlabel.config(font=("TkDefaultFont", 8),foreground="green",text="Test Run Title: "+x)
            runiderrorlabel.grid(row = 1, column = 6, sticky = W,columnspan=4)
            RunIDDone.set(True)
            RunidEntry.config(state="readonly")

        else:
            RunIDDone.set(False)
            
            RunidEntry.config(state='normal',background="red")
    
            RunidEntry.focus_set()
            runiderrorlabel.config(font=("TkDefaultFont", 8),foreground="red",text="Run ID is not Valid!")
            runiderrorlabel.grid(row = 1, column = 6, sticky = W,columnspan=4)


   
    if GIT.get() and JSONModified.get() and BuildName.get() and TextDone.get() and BuildName.get()!="Choose Build Here" and (TestType.get()=="Full Smoke Tests" or (TestType.get()=="Single User Test" and UserType.get() != "User Type" and OnboardingFlow != "Onboarding Flow" and RiskScore != "Risk Score" and InitialDepositMethod.get()!="Initial Deposit Method") )and ((TestType.get()=="Single User Test" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Report Using TestRail" and RunIDDone.get()) or ((TestType.get()=="Single User Test" and ReportingOption.get()=="Report Using TestRail" and caseIDDone.get()))):
        DoneButton.config(state="enabled")
    else:
        DoneButton.config(state="disabled")

def ValidateCaseID():
    Enter=True
    if case_id.get()=="" and caseIDDone.get():
        caseIDDone.set(False)
        
        caseidEntry.config(state='normal',background="red")
 
        caseidEntry.focus_set()
        
        caseiderrorlabel.config(font=("TkDefaultFont", 8),foreground="red",text="Run ID can't be empty!")
        runiderrorlabel.grid_forget()
        
    elif " " in case_id.get() or "-" in case_id.get() or (case_id.get().isdigit()==False and "," not in case_id.get()) :
        caseIDDone.set(False)
        
        caseidEntry.config(state='normal',background="red")
 
        caseidEntry.focus_set()
        
        caseiderrorlabel.config(font=("TkDefaultFont", 8),foreground="red",text="Run ID should be an Integer!")
        runiderrorlabel.grid_forget()
    

    elif case_id.get() !="" and caseIDDone.get():
        caseIDDone.set(True)
        caseidEntry.config(state="readonly")
        caseiderrorlabel.config(font=("TkDefaultFont", 8),foreground="green",text="")
        runiderrorlabel.grid_forget()
        
    elif caseIDDone.get() ==False:
        caseidEntry.config(state='normal',background="white")
        caseiderrorlabel.config(text="")
        Enter=False
        runiderrorlabel.grid_forget()
        CaseIDInfoLabel.grid(row=0,column=6,columnspan=2,sticky=S)

    
    global MultipleCasesTitles
    MultipleCasesTitles=[]
    if caseIDDone.get() and Enter:
        Text=""
        print(case_id.get())
        Cases=case_id.get()
        Cases=Cases.split(",")
        print(Cases)
        for elem in Cases:
            print(elem)
            x=GetTestCaseTitle(elem)
            MultipleCasesTitles.append(x)
            if x!=False:

                Text=Text+("Test Case: "+x+"\n")
                caseiderrorlabel.config(font=("TkDefaultFont", 8),foreground="green",text=Text)
                caseiderrorlabel.grid(row = 1, column = 6, sticky = W,columnspan=4)
                caseIDDone.set(True)
                caseidEntry.config(state="readonly")
                CaseIDInfoLabel.grid_forget()
                
            else:
                caseIDDone.set(False)
                
                caseidEntry.config(state='normal',background="red")
        
                caseidEntry.focus_set()
                caseiderrorlabel.config(font=("TkDefaultFont", 8),foreground="red",text="Test Case is not Valid!")
                caseiderrorlabel.grid(row = 1, column = 6, sticky = W,columnspan=4)
                runiderrorlabel.grid_forget()

    if GIT.get() and JSONModified.get() and BuildName.get() and TextDone.get() and BuildName.get()!="Choose Build Here" and (TestType.get()=="Full Smoke Tests" or (TestType.get()=="Single User Test" and UserType.get() != "User Type" and OnboardingFlow != "Onboarding Flow" and RiskScore != "Risk Score") )and (TestType.get()=="Single User Test" or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Report Using TestRail" and caseIDDone.get())):
        DoneButton.config(state="enabled")
    else:
        DoneButton.config(state="disabled")

def ChooseTestType(y):
    global RiskScore,OnboardingFlow,StopFlag
    OnboardingFlow=OnbFlow.get()
    RiskScore=Risk_Score.get()
    StopFlag=Stop.get()

    F.config(state='normal',background="white")
    K.config(text="")
    if TestType.get()=="Full Smoke Tests":
        print(RunidEntry["state"])

        w3.grid_forget()
        w4.grid_forget()
        w5.grid_forget()
        w6.grid_forget()
        w7.grid_forget()
        label1.config(text='Enter Feature Name: (Example: roy.braish+(FeatureName)@neo.ae)')
        F.config(state="normal")
        ReportDropdown.grid(row=0,column=6, sticky=W,pady = 1)
        if "Report" in ReportingOption.get() and "TestRail" in ReportingOption.get():
            Testraillabel.grid(row = 0, column = 7, sticky = W)
            Testraillabel.config(text="Run_id:")
            
            ReportDropdown.grid(row=0,column=6, sticky=W,pady = 1)
            
            runiderrorlabel.grid(row = 1, column = 6, sticky = W,columnspan=4)
            runidcheckbox.grid(row = 0, column = 9,pady = 3)
            RunidEntry.grid(row=0,column=8, sticky=W)
            
            caseiderrorlabel.grid_forget() 
            caseidcheckbox.grid_forget()
            caseidEntry.grid_forget()
            CaseIDInfoLabel.grid_forget()


            # caseidcheckbox.grid(row = 0, column = 9,pady = 3)
        elif "Don't" in ReportingOption.get():
            runidcheckbox.grid_forget()
            runiderrorlabel.grid_forget()
            RunidEntry.grid_forget()
            
            Testraillabel.grid_forget()
            CaseIDInfoLabel.grid_forget()

            caseidcheckbox.grid_forget()
            caseidEntry.grid_forget()
            caseiderrorlabel.grid_forget() 

        else:
            runidcheckbox.grid_forget()
            runiderrorlabel.grid_forget()
            RunidEntry.grid_forget()
            
            Testraillabel.grid_forget()

            caseidcheckbox.grid_forget()
            caseidEntry.grid_forget()
            caseiderrorlabel.grid_forget() 
            CaseIDInfoLabel.grid_forget()

        
    if TestType.get()=="Single User Test":
        
        w3.grid(row=4,column=1, sticky=W,pady = 1,columnspan = 1)
        w4.grid(row=4,column=2, sticky=W,pady = 1,columnspan = 1)
        w5.grid(row=4,column=3, sticky=W,pady = 1,columnspan = 1)
        w6.grid(row=4,column=5, sticky=W,pady = 1,columnspan = 2)
        w7.grid(row=4,column=4, sticky=W,pady = 1,columnspan = 1)
        ReportDropdown.grid(row=0,column=6, sticky=W,pady = 1)
        
        if "Report" in ReportingOption.get() and "TestRail" in ReportingOption.get():
            Testraillabel.grid(row = 0, column = 7, sticky = W)
            Testraillabel.config(text="Case_id:")
            
            caseidcheckbox.grid(row = 0, column = 9,pady = 3)
            caseidEntry.grid(row=0,column=8, sticky=W)
            caseiderrorlabel.grid(row = 1, column = 6, sticky = W,columnspan=4)
            # CaseIDInfoLabel.grid(row=0,column=6,columnspan=2,sticky=S)

            runidcheckbox.grid_forget()
            RunidEntry.grid_forget()
            runiderrorlabel.grid_forget() 

            
        elif "Don't" in ReportingOption.get():
            runidcheckbox.grid_forget()
            RunidEntry.grid_forget()
            runiderrorlabel.grid_forget() 
            
            Testraillabel.grid_forget()

            caseiderrorlabel.grid_forget() 
            caseidcheckbox.grid_forget()
            caseidEntry.grid_forget()
            CaseIDInfoLabel.grid_forget()

        else:
            runidcheckbox.grid_forget()
            RunidEntry.grid_forget()
            runiderrorlabel.grid_forget() 

            Testraillabel.grid_forget()

            caseidcheckbox.grid_forget()
            caseidEntry.grid_forget()
            caseiderrorlabel.grid_forget()
            CaseIDInfoLabel.grid_forget()


        

        
        if  (UserType.get()).lower() == "islamic":
            InitialDepositMethod.set("Bank Transfer")
            w7.configure(state="disabled")
        elif (UserType.get()).lower() == "etf":
            # w7.destroy()
            w7.configure(state="normal")
            
        label1.config(text='Enter Full Email: (Example: roy.braish+test@neo.ae)')
        F.config(state="normal")



    if GIT.get() and JSONModified.get() and BuildName.get() and TextDone.get() and BuildName.get()!="Choose Build Here" and (TestType.get()=="Full Smoke Tests" or (TestType.get()=="Single User Test" and UserType.get() != "User Type" and OnboardingFlow != "Onboarding Flow" and RiskScore != "Risk Score" and InitialDepositMethod.get()!="Initial Deposit Method") )and ((TestType.get()=="Single User Test" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Report Using TestRail" and RunIDDone.get()) or ((TestType.get()=="Single User Test" and ReportingOption.get()=="Report Using TestRail" and caseIDDone.get()))):
        DoneButton.config(state="enabled")
    else:
        DoneButton.config(state="disabled")
        
def ChooseBuild(x):
    global BUILDNAME
    BUILDNAME=BuildName.get()

    if GIT.get() and JSONModified.get() and BuildName.get() and TextDone.get() and BuildName.get()!="Choose Build Here" and (TestType.get()=="Full Smoke Tests" or (TestType.get()=="Single User Test" and UserType.get() != "User Type" and OnboardingFlow != "Onboarding Flow" and RiskScore != "Risk Score" and InitialDepositMethod.get()!="Initial Deposit Method") )and ((TestType.get()=="Single User Test" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Report Using TestRail" and RunIDDone.get()) or ((TestType.get()=="Single User Test" and ReportingOption.get()=="Report Using TestRail" and caseIDDone.get()))):
            DoneButton.config(state="enabled")
    else:
        DoneButton.config(state="disabled")
    print(caseIDDone.get())

def GetFeatureName():
    global FeatureName
    FeatureName=Feature.get()
    
    if GIT.get() and JSONModified.get() and BuildName.get() and TextDone.get() and BuildName.get()!="Choose Build Here" and (TestType.get()=="Full Smoke Tests" or (TestType.get()=="Single User Test" and UserType.get() != "User Type" and OnboardingFlow != "Onboarding Flow" and RiskScore != "Risk Score" and InitialDepositMethod.get()!="Initial Deposit Method") )and ((TestType.get()=="Single User Test" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Report Using TestRail" and RunIDDone.get()) or ((TestType.get()=="Single User Test" and ReportingOption.get()=="Report Using TestRail" and caseIDDone.get()))):
        DoneButton.config(state="enabled")
    else:
        DoneButton.config(state="disabled")
    
def TextValidate():
    global textcheckbox

    if Feature.get() == "" and TextDone.get():
        #Set focus here and keep enabled
        TextDone.set(False)
        
        F.config(state='normal',background="red")
 
        F.focus_set()
        # K=Label(master,text="Feature name can't be empty!")
        
        K.config(font=("TkDefaultFont", 8),foreground="red",text="Feature name can't be empty!")
        # K.grid(row = 5, column = 4, sticky = W,columnspan=4)
        
    elif TestType.get() =="Full Smoke Tests":
        if " " in Feature.get() or "_" in Feature.get() or "-" in Feature.get() or "+" in Feature.get() or "@" in Feature.get() or "." in Feature.get():
            #Set focus here and keep enabled
            TextDone.set(False)
            
            F.config(state='normal',background="red")
            F.focus_set()
            
            K.config(font=("TkDefaultFont", 8),foreground="red",text= "Feature name can't contain spaces, symbols or special characters!")
         
        elif Feature.get() != "" and TextDone.get():

            F.config(state="readonly")
            textcheckbox=TextDone.get()
            
            # K=Label(master,text="Feature name is accepted!")
            K.config(font=("TkDefaultFont", 8),foreground="green",text="Feature name is accepted!")
            # K.grid(row = 5, column = 4, sticky = W,columnspan=4)
            
        elif TextDone.get()==False:

            F.config(state='normal',background="white")
            K.config(text="")
            
    elif TestType.get()=="Single User Test":
        
        if "@" not in Feature.get() or "." not in Feature.get():
            #Set focus here and keep enabled
            TextDone.set(False)
            
            F.config(state='normal',background="red")
            F.focus_set()
            
            K.config(font=("TkDefaultFont", 8),foreground="red",text= "Email should Contain @domain.com")
         
        
        elif " " in Feature.get():
            #Set focus here and keep enabled
            TextDone.set(False)
            
            F.config(state='normal',background="red")
            F.focus_set()
            
            K.config(font=("TkDefaultFont", 8),foreground="red",text= "Feature name can't contain spaces, symbols or special characters!")
         
        elif Feature.get() != "" and TextDone.get():

            F.config(state="readonly")
            textcheckbox=TextDone.get()
            
            # K=Label(master,text="Feature name is accepted!")
            K.config(font=("TkDefaultFont", 8),foreground="green",text="Feature name is accepted!")
            # K.grid(row = 5, column = 4, sticky = W,columnspan=4)
            
        elif TextDone.get()==False:

            F.config(state='normal',background="white")
            K.config(text="")
            
    if GIT.get() and JSONModified.get() and BuildName.get() and TextDone.get() and BuildName.get()!="Choose Build Here" and (TestType.get()=="Full Smoke Tests" or (TestType.get()=="Single User Test" and UserType.get() != "User Type" and OnboardingFlow != "Onboarding Flow" and RiskScore != "Risk Score" and InitialDepositMethod.get()!="Initial Deposit Method") )and ((TestType.get()=="Single User Test" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Don't Report Results") or (TestType.get()=="Full Smoke Tests" and ReportingOption.get()=="Report Using TestRail" and RunIDDone.get()) or ((TestType.get()=="Single User Test" and ReportingOption.get()=="Report Using TestRail" and caseIDDone.get()))):
        DoneButton.config(state="enabled")
    else:
        DoneButton.config(state="disabled")
    
def printAll():
    GetFeatureName()
    print("UI is complete, proceed to pulling from Github...")
    
    
        
    if Stop.get() == 'Stop At':
        sleep(1)
        ## Set as Null here in json file
        StopFlag = "Null"
        
    
    if TestType.get() == "Full Smoke Tests" :
        a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        # print(json_object)

        json_object["TechnicalVariables"]["GITpull"] = GIT_Answer
        json_object["TechnicalVariables"]["FeatureName"] = FeatureName
        json_object["TechnicalVariables"]["BuildName"] = BUILDNAME
        json_object["TechnicalVariables"]["TestisDone"]=="False"

        if "Report" in ReportingOption.get() and "TestRail" in ReportingOption.get():
            json_object["TestRailSmokeTests"]["Status"] = "enabled"
            json_object["TestRailSmokeTests"]["run_id"] = str(run_id.get())
            json_object["TestRailSmokeTests"]["SingleCase"] = "False"
            json_object["TestRailSmokeTests"]["SingleTestCaseID"] = "Null"
            json_object["TestRailSmokeTests"]["SingleTestCaseTitle"] = "Null"

        else:
            json_object["TestRailSmokeTests"]["Status"] = "disabled"
            json_object["TestRailSmokeTests"]["run_id"] = "Null"
            json_object["TestRailSmokeTests"]["SingleCase"] = "False"
            json_object["TestRailSmokeTests"]["SingleTestCaseID"] = "Null"
            json_object["TestRailSmokeTests"]["SingleTestCaseTitle"] = "Null"



        json_object["SingleUserDetails"]["TestType"] = TestType.get()
        json_object["SingleUserDetails"]["Email"] = "Null"
        json_object["SingleUserDetails"]["User_Type"] = "Null"
        json_object["SingleUserDetails"]["OnboardingFlow"] = "Null"
        json_object["SingleUserDetails"]["RiskScore"] ="Null"
        json_object["SingleUserDetails"]["InitialDepositMethod"] ="Null"
        json_object["SingleUserDetails"]["StopFlag"] = "Null"

        t = datetime.now().time()
        TestEndedseconds = (t.hour * 60 + t.minute) * 60 + t.second
        Time_in_Tkinter=TestEndedseconds - TestStartedseconds
        json_object["TechnicalVariables"]["Time_in_Tkinter"] = Time_in_Tkinter

        a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
        json.dump(json_object, a_file)
        a_file.close()
        ERRORCODE=4
        
    elif TestType.get() == "Single User Test":
        
        a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        # print(json_object)
        
        json_object["TechnicalVariables"]["GITpull"] = GIT_Answer
        json_object["TechnicalVariables"]["BuildName"] = BUILDNAME
        json_object["TechnicalVariables"]["FeatureName"] = "Null"
        json_object["TechnicalVariables"]["TestisDone"]=="False"
        
        if "Report" in ReportingOption.get() and "TestRail" in ReportingOption.get():
            json_object["TestRailSmokeTests"]["Status"] = "enabled"
            json_object["TestRailSmokeTests"]["run_id"] = "Null"
            json_object["TestRailSmokeTests"]["SingleCase"] = "True"
            if "," in case_id.get():
                s=case_id.get()
                s=s.split(",")
                for elem in s:
                    print(elem)
                json_object["TestRailSmokeTests"]["SingleTestCaseID"] = s
                json_object["TestRailSmokeTests"]["SingleTestCaseTitle"] = MultipleCasesTitles
            else:
                s=[str(case_id.get())]
                json_object["TestRailSmokeTests"]["SingleTestCaseID"] = s
                json_object["TestRailSmokeTests"]["SingleTestCaseTitle"] = GetTestCaseTitle(case_id.get())

        else:
            json_object["TestRailSmokeTests"]["Status"] = "disabled"
            json_object["TestRailSmokeTests"]["run_id"] = "Null"
            json_object["TestRailSmokeTests"]["SingleCase"] = "False"
            json_object["TestRailSmokeTests"]["SingleTestCaseID"] = "Null"
            json_object["TestRailSmokeTests"]["SingleTestCaseTitle"] = "Null"


        json_object["SingleUserDetails"]["TestType"] = TestType.get()
        json_object["SingleUserDetails"]["Email"] = FeatureName
        json_object["SingleUserDetails"]["User_Type"] = UserType.get()
        json_object["SingleUserDetails"]["OnboardingFlow"] = OnboardingFlow
        json_object["SingleUserDetails"]["RiskScore"] =RiskScore
        json_object["SingleUserDetails"]["InitialDepositMethod"] =InitialDepositMethod.get()

        json_object["SingleUserDetails"]["StopFlag"] = Stop.get()

        t = datetime.now().time()
        TestEndedseconds = (t.hour * 60 + t.minute) * 60 + t.second
        Time_in_Tkinter=TestEndedseconds - TestStartedseconds
        json_object["TechnicalVariables"]["Time_in_Tkinter"] = Time_in_Tkinter

        a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
        json.dump(json_object, a_file)
        a_file.close()
        ERRORCODE = 1
    



    master.quit()
    os._exit(ERRORCODE)


    
master = Tk()
master.minsize(width=1000,height=700)
# master.attributes('-zoomed', True)
master.state('zoomed')
master.iconbitmap(r"C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\GUI\\icon.ico")
master.title("Smoke Tests info and Credentials")

t = datetime.now().time()
TestStartedseconds = (t.hour * 60 + t.minute) * 60 + t.second



# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file = r"C:\Users\Roy Braish\Roy Personal\Appium-Automation-Python\GUI\NEOLogo.png")
img1 = img.subsample(2, 2)
Label(master, image = img1).grid(row = 0, column = 0,
       columnspan = 5, rowspan = 1)


# this will create a label widget
l1 = Label(master, text = "Pull Code from Github?")
l1.grid(row = 2, column = 0, sticky = W)

global a1
global a2
GIT = StringVar()
a1= Radiobutton(master, 
               text="True",
               variable=GIT,
               value="True",command=GITPULLAnswer)
a2=Radiobutton(master, 
               text="False",
               variable=GIT,
               value="False",command=GITPULLAnswer)
a1.grid(row = 2, column = 3,columnspan=2)
a2.grid(row = 2, column = 4,columnspan=1)



separator = Separator(master, orient='horizontal')
separator.grid(row=3,column=0,columnspan=4, sticky="ew", padx=10, pady=10)


TestType = StringVar()
OPTIONS=["Single User Test","Full Smoke Tests"]
global w2
w2=OptionMenu(master,TestType, "Test Type",*OPTIONS,command=ChooseTestType)
w2.grid(row=4,column=0, sticky=W,pady = 1,columnspan = 1)


UserType = StringVar()
OPTIONS=["ETF","Islamic"]
global w3
w3=OptionMenu(master,UserType, "User Type",*OPTIONS,command=ChooseTestType)
w3.grid(row=4,column=1, sticky=W,pady = 1,columnspan = 1)

OnbFlow = StringVar()
OPTIONS=["Predefined","Customized"]
global w4
w4=OptionMenu(master,OnbFlow, "Onboarding Flow",*OPTIONS,command=ChooseTestType)
w4.grid(row=4,column=2, sticky=W,pady = 1,columnspan = 1)

Risk_Score = StringVar()
OPTIONS=["1","2","3","4","5","6","7","8","9","10"]
global w5
w5=OptionMenu(master,Risk_Score, "Risk Score",*OPTIONS,command=ChooseTestType)
w5.grid(row=4,column=3, sticky=W,pady = 1,columnspan = 1)

InitialDepositMethod = StringVar()
OPTIONS=["Bank Transfer","KNET"]
global w7
w7=OptionMenu(master,InitialDepositMethod, "Initial Deposit Method",*OPTIONS,command=ChooseTestType)
w7.grid(row=4,column=4, sticky=W,pady = 1,columnspan = 1)

Stop = StringVar()
OPTIONS=["Verify Email Step","Upload IDs","KYC Personal Info.","KYC Address Info","KYC Employment Info","KYC Income and Wealth Info","KYC Additional Info","Confirm Classification step","Contract Not Signed Step","Contract Signed Step, Not Approved.","Pending Initial Deposit","Active User","Active User + Additional Deposit","Active User + Partial Withdrawal", "Active User + Full Withdrawal"]
global w6
w6=OptionMenu(master,Stop, "Stop At",*OPTIONS,command=ChooseTestType)
w6.grid(row=4,column=5, sticky=W,pady = 1,columnspan = 2)



separator = Separator(master, orient='horizontal')
separator.grid(row=5,column=0,columnspan=4, sticky="ew", padx=10, pady=10)
global label1
label1 = Label(master, text = "Enter Full Email: (Example: roy.braish+test@neo.ae)")
label1.grid(row = 6, column = 0, sticky = W)

w3.grid_forget()
w4.grid_forget()
w5.grid_forget()
w6.grid_forget()
w7.grid_forget()
        
global F
Feature=StringVar()
F=tk.Entry(master,textvariable = Feature,validate="focus",width=40)
F.grid(row = 6, column = 4, sticky = W,columnspan=4, padx=10, pady=10)
F.config(state="readonly")

global b1
TextDone=BooleanVar()
b1= Checkbutton(master, 
               text="Confirm",
               variable=TextDone,onvalue=True,offvalue=False,command=TextValidate)
b1.grid(row = 6, column = 7,pady = 3)

global K
K=Label(master,text="")
K.config(font=("TkDefaultFont", 8),foreground="blue")
K.grid(row = 7, column = 4, sticky = W,columnspan=4)

separator = Separator(master, orient='horizontal')
separator.grid(row=7,column=0,columnspan=4, sticky="ew", padx=10, pady=10)



l2 = Label(master, text = "Please Modify your JSON file found in your directory. \n(Appium Automation Python/BaseClasses) ")
l2.grid(row = 8, column = 0, sticky = W)

global x1
JSONModified=BooleanVar()
x1= Checkbutton(master, 
               text="Done",
               variable=JSONModified,onvalue=True,offvalue=False,command=JSONAnswer)
x1.grid(row = 8, column = 3,pady = 3,columnspan = 2)


separator = Separator(master, orient='horizontal')
separator.grid(row=9,column=0,columnspan=4, sticky="ew", padx=10, pady=10)


l1 = Label(master, text = "Choose a Build: ")
l1.grid(row = 10, column = 0, sticky = W)

X=os.listdir('C:\\Users\\Roy Braish\\Roy Personal\\SW Android Builds')
Builds=natsort.natsorted(X)

OPTIONS=[]
count =1
for Build in Builds:
    OPTIONS.append(Build)

BuildName = StringVar()
 
global w
w=OptionMenu(master,BuildName, "Choose Build Here",*OPTIONS,command=ChooseBuild)
w.grid(row=11,column=4, sticky=W,pady = 1,columnspan = 1)


DoneButton = Button(master, text = "Done!",command= printAll,width=20,state= DISABLED)
DoneButton.grid(row = 12, column = 1, sticky = E,columnspan=3)

global ReportingOption
ReportingOption = StringVar()
OPTIONS=["Don't Report Results","Report Using TestRail"]
global ReportDropdown
ReportDropdown=OptionMenu(master,ReportingOption, "Test Reporting",*OPTIONS,command=TestRailFun)
ReportDropdown.grid(row=0,column=6, sticky=W,pady = 1)
ReportDropdown.grid_forget()


global caseidcheckbox
global caseIDDone
caseIDDone=BooleanVar()
caseidcheckbox= Checkbutton(master, 
            text="Confirm",
            variable=caseIDDone,onvalue=True,offvalue=False,command=ValidateCaseID)
caseidcheckbox.grid(row = 0, column = 9,pady = 3)
caseidcheckbox.grid_forget()

global Testraillabel
Testraillabel = Label(master, text = "Run_id:")
Testraillabel.grid(row = 0, column = 7, sticky = W)
Testraillabel.grid_forget()
        
global RunidEntry
global run_id
run_id = StringVar()
RunidEntry=tk.Entry(master,textvariable=run_id)
RunidEntry.grid(row=0,column=8, sticky=W)
RunidEntry.grid_forget()

global runidcheckbox
global RunIDDone
RunIDDone=BooleanVar()
runidcheckbox= Checkbutton(master, 
            text="Confirm",
            variable=RunIDDone,onvalue=True,offvalue=False,command=ValidateRunID)
runidcheckbox.grid(row = 0, column = 9,pady = 3)
runidcheckbox.grid_forget()

global runiderrorlabel
runiderrorlabel=Label(master,text="")
runiderrorlabel.config(font=("TkDefaultFont", 8),foreground="blue")
runiderrorlabel.grid(row = 1, column = 6, sticky = W,columnspan=4)
runiderrorlabel.grid_forget()

global caseiderrorlabel
caseiderrorlabel=Label(master,text="")
caseiderrorlabel.config(font=("TkDefaultFont", 8),foreground="blue")
caseiderrorlabel.grid(row = 1, column = 6, sticky = W,columnspan=4)
caseiderrorlabel.grid_forget()

global caseidEntry
global case_id
case_id = StringVar()
caseidEntry=tk.Entry(master,textvariable=case_id)
caseidEntry.grid(row=0,column=8, sticky=W)
caseidEntry.grid_forget()

global case_id_note
global CaseIDInfoLabel
case_id_note=StringVar()
CaseIDInfoLabel=Label(master,text="You can add multiple cases, for example: 3260,3261,3262,3263")
CaseIDInfoLabel.config(font=("TkDefaultFont", 8),foreground="Blue")
CaseIDInfoLabel.grid(row=0,column=6,columnspan=2,sticky=S)
CaseIDInfoLabel.grid_forget()



mainloop()


