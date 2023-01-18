
import subprocess
import sys


sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\GUI")
import SystemPathGUI
import json
from time import sleep
import tkinter
from tkinter import messagebox
import webbrowser
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from ClosePrograms import ClosePrograms
from SaveJSONFile import SaveJSONFile

from TestRailReporting import GetTestCaseURL, GetTestRunCases, SaveTestCase_Run_URL


oldline="null"
with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt", 'w') as f:
    f.write('Starting Code...\n')
sleep(5)
SaveJSONFile("TechnicalVariables,TestisDone","False")
SaveJSONFile("TechnicalVariables,progress",0)

with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
# Load its content and make a new dictionary
    JSONFile=json.load(file)
    
if JSONFile["TestRailSmokeTests"]["Status"]=="enabled":SaveTestCase_Run_URL()

run_id=JSONFile["TestRailSmokeTests"]["run_id"]
tempemail=JSONFile["SingleUserDetails"]["Email"]

if JSONFile["TestRailSmokeTests"]["Status"].lower() == "enabled":TestRail=True
else : TestRail=False

def OpenlocalReports():
    os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\Reports")
    
    
def OpenCloudReports():
    
    if TestRail:
        with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
        # Load its content and make a new dictionary
            JSONFile=json.load(file) 
        URL=JSONFile["TestRailSmokeTests"]["URL"]
        webbrowser.open(URL)
    else:messagebox.showwarning("No Test Run", "You haven't selected a test run at the beginning.\nCheck Reports locally.")
        
    
def OpenVideoRecordings():
    os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\VideoRecording")


def OpenScreenshots():
    os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\FailedScreenshots")
    
    
def LessInfo():
    master.geometry("1000x700")
    more_info_button.config(text="More Info? ",command=MoreInfo)
    info.grid_forget()
    LocalReports.grid_forget()
    if TestRail:
        RemoteReports.grid_forget()
    info1.grid_forget()
    VideoRecordingButton.grid_forget()
    info2.grid_forget()
    ScreenshotsButton.grid_forget()
    separator0.grid_forget()
    separator1.grid_forget()
    separator2.grid_forget()


def MoreInfo():
    master.geometry("1000x850")
    
    more_info_button.config(text="Less Info? ",command=LessInfo)
    global separator0
    separator0 = Separator(master, orient='horizontal')
    separator0.grid(row=11,column=0,columnspan=4, sticky="ew", padx=10, pady=10)
    
    global info
    info = Label(master,text="To access your Reports check the following links: ")
    info.grid(row=12,column=0,columnspan=4, sticky="w",rowspan=2)
    
    global LocalReports
    LocalReports= Button(master, text = "Access the reports locally", command= OpenlocalReports)
    LocalReports.grid(row=12,column=3,sticky="w")
    
    global RemoteReports
    RemoteReports= Button(master, text = "Access the TestRail Reports", command= OpenCloudReports)
    RemoteReports.grid(row=13,column=3,sticky="w")

    global separator1
    separator1 = Separator(master, orient='horizontal')
    separator1.grid(row=14,column=0,columnspan=4, sticky="ew", padx=10, pady=10)
    
    global info1
    info1 = Label(master,text="Access tests video Recordings (Failed and Successful): ")
    info1.grid(row=15,column=0,columnspan=4, sticky="w",rowspan=2)
    
    global VideoRecordingButton
    VideoRecordingButton= Button(master, text = "Access Recordings", command= OpenVideoRecordings)
    VideoRecordingButton.grid(row=15,column=3)
    
    global separator2
    separator2 = Separator(master, orient='horizontal')
    separator2.grid(row=16,column=0,columnspan=4, sticky="ew", padx=10, pady=10)
    

    global info2
    info2 = Label(master,text="Access tests Failed Screenshots ")
    info2.grid(row=17,column=0,columnspan=4, sticky="w",rowspan=2)
    
    global ScreenshotsButton
    ScreenshotsButton= Button(master, text = "Access Screenshots ", command= OpenScreenshots)
    ScreenshotsButton.grid(row=17,column=3)


def printonTkinter():
        
    global oldline
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt") as file:
        lines1 = file.readlines()
        lines = [line.rstrip() for line in lines1]
    
    if oldline=="null":
        while True:
            if lines[len(lines)-1]!="":
                oldline=lines[len(lines)-1]
                break
            elif lines[len(lines)-2]!="":
                oldline=lines[len(lines)-2]
                break
            elif lines[len(lines)-3]!="":
                oldline=lines[len(lines)-3]
                break
            elif lines[len(lines)-4]!="":
                oldline=lines[len(lines)-4]
                break
            elif lines[len(lines)-5]!="":
                oldline=lines[len(lines)-5]
                break
            elif lines[len(lines)-6]!="":
                oldline=lines[len(lines)-6]
                break
        
    else:
        while True:
            if lines[len(lines)-1]!="":
                index=1
                temp=lines[len(lines)-1]
                break
            elif lines[len(lines)-2]!="":
                index=2
                temp=lines[len(lines)-2]
                break
            elif lines[len(lines)-3]!="":
                index=3
                temp=lines[len(lines)-3]
                break
            elif lines[len(lines)-4]!="":
                index=4
                temp=lines[len(lines)-4]
                break
            elif lines[len(lines)-5]!="":
                index=5
                temp=lines[len(lines)-5]
                break
            elif lines[len(lines)-6]!="":
                index=6
                temp=lines[len(lines)-6]
                break   
            
        if oldline=="TestRail Reported:":
            sleep(10)
            with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt") as file:
                lines1 = file.readlines()
                lines = [line.rstrip() for line in lines1]


            Reported=[]
            for i in range(len(lines)-1,0,-1):

                if lines[i]!="TestRail Reported:" and lines[i]!="":
                    Reported.append(lines[i])     
                elif "testrail reported" in lines[i].lower():
                    break
            Reported.reverse()
            entry3.configure(state= "normal")
            for elem in Reported:
                if not "test started" in elem:
                    entry3.insert(END, elem+"\n")
                    TestStarted=False
                else:TestStarted=True        
            x=float(entry3.index('end-1c').split('.')[0])
            entry3.tag_add("TestRailReported", str(x-len(Reported)) ,str(x-1+0.91)) # tag name my_hg is created 
            print(x-len(Reported)-1)
            entry3.tag_config("TestRailReported",foreground="purple")
            try:temp=Reported[len(Reported)-1]
            except:temp=Reported[len(Reported)-2]
            oldline=temp
            if TestStarted:
                entry3.insert(END, "\n\n")
                entry3.insert(END, temp+"\n")
            else:
                entry3.insert(END, "\n\n")

            new=False

            
            
        elif oldline != temp:
            oldline=temp
            entry3.configure(state= "normal")
            if "test started" in temp.lower():
                entry3.insert(END, "\n\n\n")
                entry3.insert(END, temp+"\n")
            else:
                entry3.insert(END, temp+"\n")
            new=True
            entry3.yview_pickplace("end")
            if temp=="TestRail Reported:":
                sleep(2)
        else:
            new=False

        if new:   
            if "Test Started" in temp:
                
                x=float(entry3.index('end-1c').split('.')[0])
                entry3.tag_add("TestDone", str(x-1) ,str(x-1.0+0.91)) # tag name my_hg is created 
                entry3.tag_config("TestDone",foreground="white",background="blue")
            elif "Test is Successful for" in temp:
                x=float(entry3.index('end-1c').split('.')[0])
                entry3.tag_add("TestDone", str(x-1) ,str(x-1.0+0.91)) # tag name my_hg is created 
                entry3.tag_config("TestDone",foreground="white",background="green")
            elif "NEW test Case reported(TEST success)  Test Ended at:" in temp:
                x=float(entry3.index('end-1c').split('.')[0])
                entry3.tag_add("TestDone", str(x-1) ,str(x-1.0+0.91)) # tag name my_hg is created 
                entry3.tag_config("TestDone",foreground="white",background="green")

            elif "TEST success" in temp or "successful" in temp or "Successful" in temp or temp=="Full Smoke Tests" or temp=="Single User Test":
                x=float(entry3.index('end-1c').split('.')[0])
                entry3.tag_add("Success", str(x-1) ,str(x-1.0+0.91)) # tag name my_hg is created 
                entry3.tag_config("Success",foreground="green")
            elif "TEST fail" in temp or "retrying" in temp or "Issue" in temp or "trying another" in temp or "fail" in temp.lower() or "expected" in temp.lower() or "actual" in temp.lower():
                x=float(entry3.index('end-1c').split('.')[0])
                entry3.tag_add("Fail", str(x-1) ,str(x-1.0+0.91)) # tag name my_hg is created 
                entry3.tag_config("Fail",foreground="red")
            elif "not shown" in temp or "not Found" in temp:
                x=float(entry3.index('end-1c').split('.')[0])
                entry3.tag_add("NotShown", str(x-1) ,str(x-1.0+0.91)) # tag name my_hg is created 
                entry3.tag_config("NotShown",foreground="#B7BE16")
            elif "solution" in temp.lower() or "solutions" in temp.lower():
                x=float(entry3.index('end-1c').split('.')[0])
                entry3.tag_add("solution", str(x-1) ,str(x-1.0+0.91)) # tag name my_hg is created 
                entry3.tag_config("solution",foreground="#45dcd5")

        entry3.configure(state= "disabled")
        print("temp =  "+temp) 

    print("oldline =  " +oldline)
    print("")

    return oldline

def progress(progress):
    if pb['value'] < 100:
        pb['value'] = progress


def WWW():
    global tempemail
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
    # Load its content and make a new dictionary
        JSONFile=json.load(file)
        # print(JSONFile["SingleUserDetails"]["Email"])
        # print(tempemail)
    if JSONFile["SingleUserDetails"]["TestType"]=="Single User Test":
        if JSONFile["SingleUserDetails"]["Email"]!=tempemail:
    
            tempemail=JSONFile["SingleUserDetails"]["Email"]
            EmailLabel.config(text=tempemail)
            EmailLabel.grid(row=10, column=1,columnspan=1,sticky='W')
        
    # TestisDone()
    # if JSONFile["TechnicalVariables"]["TestisDone"]=="True":
    if JSONFile["TechnicalVariables"]["TestisDone"]=="True":
        TestisDone()
    elif JSONFile["TechnicalVariables"]["TestisDone"]=="Fail":
        TesthasFailed()
    else:
        oldline=printonTkinter()
        master.after(1000,WWW)
    
    progress(JSONFile["TechnicalVariables"]["progress"])
    

def TestisDone():
    pb.grid_forget()
    ExitButton.grid_forget()
    l1.grid_forget()
    i.grid_forget()
    
    master.geometry("1000x700")

    LabelDone=Label(master,text="Your test is done!!! ")
    LabelDone.config(font=("TkDefaultFont", 40 ),foreground="green",text= "Your test is Done!")
    LabelDone.grid(row= 5, column=0,columnspan=2, sticky="w")
    
    global more_info_button
    more_info_button = Button(master, text = "More info? ",command= MoreInfo ,width=20)
    more_info_button.grid(row = 5, column = 3, sticky = E)

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    # print(json_object)
    
    json_object["TechnicalVariables"]["TestisDone"] = "False"

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
    

def TesthasFailed():
    
    pb.grid_forget()
    ExitButton.grid_forget()
    # l1.grid_forget()
    # i.grid_forget()
    
    master.geometry("1000x700")

    LabelDone=Label(master,text="Your test has Failed!!!")
    LabelDone.config(font=("TkDefaultFont", 40 ),foreground="red",text= "Your test has Failed!!!")
    LabelDone.grid(row= 5, column=0,columnspan=2, sticky="w")
    
    global more_info_button
    more_info_button = Button(master, text = "More info? ",command= MoreInfo ,width=20)
    more_info_button.grid(row = 5, column = 3, sticky = E)

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    # print(json_object)
    
    json_object["TechnicalVariables"]["TestisDone"] = "False"

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
    
def Debugger():
    SW_HIDE = 0
    info = subprocess.STARTUPINFO()
    # info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_HIDE


    subprocess.run(["start","/min",  "cmd", "/C", " cd / && cd C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\GUI && python Backend_Debugger.py"],startupinfo=info, shell=True)

    
def Exit():
    
    
    ClosePrograms()
    master.destroy()
    
        
master = Tk()
master.iconbitmap(r"C:\Users\Roy Braish\Roy Personal\Appium-Automation-Python\GUI\icon.ico")
master.title("Smoke Tests")
master.geometry("1000x700")


# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file = r"C:\Users\Roy Braish\Roy Personal\Appium-Automation-Python\GUI\neo-logo-header.png")
img1 = img.subsample(2, 2)
Label(master, image = img1).grid(row = 0, column = 0,
    columnspan = 5, rowspan = 1)


separator = Separator(master, orient='horizontal')
separator.grid(row=2,column=0,columnspan=4, sticky="ew", padx=10, pady=10)


global l1
l1 = Label(master, text = "Running Smoke Tests... ")
l1.grid(row = 3, column = 0, sticky = W)

global i
i = Separator(master, orient='horizontal')
i.grid(row=4,column=0,columnspan=4, sticky="ew", padx=10, pady=10)


global pb
pb = ttk.Progressbar(
master,
orient='horizontal',
mode='determinate',
length=600
)
# place the progressbar
pb.grid(column=0, row=5, columnspan=2, padx=10, pady=20)


global ExitButton
ExitButton = Button(master, text = "Exit",command= Exit ,width=20)
ExitButton.grid(row = 5, column = 3, sticky = E)


global Debugger_panel
Debugger_panel = Button(master, text = "Open Debugger Pannel",command= Debugger ,width=25)
Debugger_panel.grid(row = 5, column = 4, sticky = E)



with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt") as file:
        lines1 = file.readlines()
        lines = [line.rstrip() for line in lines1]

    
global entry3
Logs=StringVar()
entry3 = Text(master,width=114,height=15)
entry3.grid(column=0,row=6, columnspan=5, rowspan=3, sticky='W')


scrollbar = tkinter.Scrollbar(master,orient="vertical",bg="white") # height= not permitted here!
entry3.config(yscrollcommand= scrollbar.set)
scrollbar.config(command= entry3.yview)
scrollbar.grid(column=4, row=6, rowspan=3,  sticky='NS',columnspan=5)
#Set the state of Entry widget ReadOnly

entry3.configure(state= "normal")
qq=('\n'.join(lines1))

lines = qq.split("\n")
non_empty_lines = [line for line in lines if line.strip() != ""]

string_without_empty_lines = ""
for line in non_empty_lines:
      string_without_empty_lines += line + "\n"

print( string_without_empty_lines)
entry3.insert(END, (string_without_empty_lines))
entry3.configure(state= "disabled")
if JSONFile["SingleUserDetails"]["TestType"]=="Single User Test":
    
    TestTypelabel=Label(master,text=JSONFile["SingleUserDetails"]["TestType"])
    TestTypelabel.grid(row=10, column=0,sticky='W',columnspan=1)

    global EmailLabel
    EmailLabel=Label(master,text=JSONFile["SingleUserDetails"]["Email"])
    EmailLabel.grid(row=10, column=1,columnspan=1,sticky='W')
    # global tempemail
    # tempemail=JSONFile["SingleUserDetails"]["Email"]
    
    UserTypeLabel=Label(master,text=JSONFile["SingleUserDetails"]["User_Type"])
    UserTypeLabel.grid(row=10, column=2,columnspan=1)
    
    OnboardingFlowLabel=Label(master,text=JSONFile["SingleUserDetails"]["OnboardingFlow"])
    OnboardingFlowLabel.grid(row=10, column=3,columnspan=1)

    if JSONFile["SingleUserDetails"]["StopFlag"]=="Null":
        StopAtLabel=Label(master,text="Active User")
        StopAtLabel.grid(row=10, column=4,sticky='e')
    else:
        StopAtLabel=Label(master,text=JSONFile["SingleUserDetails"]["StopFlag"])
        StopAtLabel.grid(row=10, column=4,sticky='e')
    
    

# TestType = StringVar()
# OPTIONS=[True,False]
# global w2
# w2=OptionMenu(master,TestType, "Test Type",*OPTIONS)
# w2.grid(row=3,column=4, sticky=W,pady = 1,columnspan = 1)


master.after(2000,WWW)
mainloop()



