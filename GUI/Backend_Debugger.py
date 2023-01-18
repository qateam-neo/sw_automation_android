import json
import SystemPathGUI 
from RiskEngine_API import RiskEngine_API

from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.ttk import *
import tkinter as tk
from UserAPIs import User_Info
from Admin_APIs import Admin_APIs
from EmailExists import CheckIfEmailExists_ReturnUser_ID, PJConnect_CheckIfEmailExists_ReturnUser_ID
from PostTokenAPI import PostTokenAPI


Admin=Admin_APIs()
UserInfo=User_Info()
Linked=False

Auth=PostTokenAPI("roy.braish+admin@neo.ae")
AuthSuccess=Admin.ValidateAdminAuth(Auth)
RiskEngineInfo=RiskEngine_API(AdminAuthorization=Auth)
RiskEngineInfo.setheader()

def ValidateAuth(AuthSuccess):
    
    if AuthSuccess!= True:
        while True:
            ManualAdminAuth = askstring("Error Authenticating Admin","Enter Admin Bearer Token Manually: ",show="*")
            print(ManualAdminAuth)
            if ManualAdminAuth==None:
                master.quit()
                master.destroy()
                break
            elif ManualAdminAuth=="":
                print("Ask Again")
            else:
                AuthSuccess=Admin.ValidateAdminAuth(ManualAdminAuth)
                if AuthSuccess == True:
                    break


def DisableButtons():
    for Button in InputButtons:
        try: Button.config(state="disabled")
        except:Button.config(state="readonly")
    
def EnableButtons():
    for Button in InputButtons:
        try:Button.config(state="normal")
        except: Button.config(state="enabled")


def link_to_fe_test():
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
        JSON=json.load(file)
    Email=JSON["SingleUserDetails"]["Email"]
    if "null" in Email.lower(): messagebox.showwarning("No Email Shown!", "We haven't found any email saved or linked, \nPlease make sure that your tests are running and try again...")
    global Linked
    if Linked==False:
        EmailCheckboxValue.set(True)
        EmailEntryValue.set(Email)
        # EmailEntry.config(state="disabled",background="green")
        Linked=True
        link_to_fe_test_button.config(text="Disconnect",background="#d97577",foreground="#000000")
        VerifyEmail()
    else:
        EmailCheckboxValue.set(False)
        # EmailEntryValue.set(Email)
        # EmailEntry.config(state="disabled",background="green")
        Linked=False
        link_to_fe_test_button.config(text="Link to FE Test",background="white",foreground="#000000")
        EmailEntry.config(state="normal",background="white")
        VerifyEmail()

    
def Closeallwindows():

    for View in Topview:
        try:
            if 'normal' == View.state():
                Running=True
            else:
                Running=False
        except:
            Running=False

        if Running:
            View.destroy()



def VerifyEmail(Email="N/A"):
    if EmailCheckboxValue.get():
        if any(c.isalpha() for c in EmailEntryValue.get()): 
            try: User_ID=CheckIfEmailExists_ReturnUser_ID(EmailEntryValue.get()) 
            except: 
                messagebox.showwarning("User not found!", "We haven't found any email saved or linked, \nPlease make sure to enter CMNO in case of connect user...")
        else:User_ID= PJConnect_CheckIfEmailExists_ReturnUser_ID(EmailEntryValue.get())
    else:
        User_ID="N/A"

        
    if User_ID==False and EmailCheckboxValue.get():
        EmailCheckboxValue.set(False)
        
        EmailEntry.config(state='normal',background="red")
        EmailEntry.focus_set()
        DisableButtons()

    elif User_ID !=False and EmailCheckboxValue.get():
        
        EmailCheckboxValue.set(True)
        EmailEntry.config(state="disabled",background="green")
        Admin.__init__(Email=str(EmailEntryValue.get()))
        UserInfo.__init__(str(EmailEntryValue.get()))
        RiskEngineInfo.__init__(str(EmailEntryValue.get()))


        Analyze_User_Status()
        EnableButtons()


    
    elif EmailCheckboxValue.get()==False:
        EmailCheckboxValue.set(False)
        
        EmailEntry.config(state="normal",background="white")
        EmailEntry.focus_set()
        DisableButtons()
        Label_UserStatus.config(text="",font=( "default",8, "bold"),foreground="#b9b513")
        if link_to_fe_test_button.cget('text')=="Disconnect":
            link_to_fe_test_button.config(text="Link to FE Test",background="white",foreground="#000000")

            
    

# def ValidateAuth(AuthSuccess):
    
#     if AuthSuccess!= True:
#         # while True:
#         #     ManualAdminAuth = askstring("Error Authenticating Admin","Enter Admin Bearer Token Manually: ",show="*")
#         #     print(ManualAdminAuth)
#         #     if ManualAdminAuth==None:
#         #         master.quit()
#         #         master.destroy()
#         #         break
#         #     elif ManualAdminAuth=="":
#         #         print("Ask Again")
#         #     else:
#         #         AuthSuccess=Admin.ValidateAdminAuth(ManualAdminAuth)
#         #         if AuthSuccess == True:
#         #             break
#         print("Admin Authorization Ignored!! APIs are offline. ")
#         messagebox.showinfo("Admin authorization","Admin Authorization Ignored!! \nAPIs are offline.")


def Analyze_User_Status():
    global StatusMessage
    StatusMessage=UserInfo.StatusInfoAPI_ReturnJSON()
    User_on_KYC=False
    User_before_kyc=False
    if StatusMessage["meta"]["has_verified_transaction"] == True:
        Step=""
        Label_UserStatus.config(text="⚫ Active\n"+Step,font=( "default",8, "bold"),foreground="#057e0c")
    elif StatusMessage["meta"]["has_transaction"] ==True and StatusMessage["meta"]["has_verified_transaction"] == False:
        Step="Initial Deposit Pending Activation"
        Label_UserStatus.config(text="⚫ Pending\nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")
    elif StatusMessage["meta"]["is_approved"] == True:
        Step="User is Approved, Pending Initial Deposit..."
        Label_UserStatus.config(text="⚫ Pending\nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")
    elif StatusMessage["meta"]["is_contract_confirmed"] or StatusMessage["meta"]["signed_contract"]:
        Step="Signed Contract, Pending Approval..."
        Label_UserStatus.config(text="⚫ Pending\nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")
    elif StatusMessage["meta"]["is_classification_confirmed"] :
        Step="Classification Confirmed, Pending contract signature..."
        Label_UserStatus.config(text="⚫ Pending\nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")
    elif StatusMessage["meta"]["uploaded_civilID"] or StatusMessage["meta"]["is_eid_verified"] or(StatusMessage["meta"]["primary_id_front_scanned"] and StatusMessage["meta"]["primary_id_back_scanned"] and StatusMessage["meta"]["secondary_id_scanned"]):
        KYC_StatusMessage=UserInfo.KYCInfoAPI_ReturnJSON()
        User_on_KYC=True
        User_before_kyc=False

    elif StatusMessage["meta"]["uploaded_civilID"] ==False or StatusMessage["meta"]["is_eid_verified"] == False or StatusMessage["meta"]["primary_id_front_scanned"] ==False or StatusMessage["meta"]["primary_id_back_scanned"] ==False or StatusMessage["meta"]["secondary_id_scanned"] ==False:
        User_before_kyc=True
        User_on_KYC=False

        
    
        
    if User_on_KYC:
        try: 
            KYC_StatusMessage["meta"]["kyc"]["political_position_existing"]
            KYC_StatusMessage["meta"]["kyc"]["us_citizen"]
            KYC_StatusMessage["meta"]["kyc"]["pays_taxes_in_other_country"]
            Step="KYC Additional Info Confirmed, Pending confirm classification..."
            Label_UserStatus.config(text="⚫ Pending (KYC)\nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")
        except:
            try: 
                KYC_StatusMessage["meta"]["kyc"]["trading_experience"]
                KYC_StatusMessage["meta"]["kyc"]["income_source"]
                KYC_StatusMessage["meta"]["kyc"]["bank_name"]
                Step="KYC Income and Wealth Confirmed, Pending Additional Info..."
                Label_UserStatus.config(text="⚫ Pending (KYC)\nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")
            except:
                try:
                    KYC_StatusMessage["meta"]["kyc"]["board_membership_existing"]
                    KYC_StatusMessage["meta"]["kyc"]["employment_status"]
                    Step="KYC Employment Confirmed, Pending Income and Wealth Info..."
                    Label_UserStatus.config(text="⚫ Pending (KYC)\nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513") 
                except:
                    try:
                        KYC_StatusMessage["meta"]["kyc"]["address_house"]
                        KYC_StatusMessage["meta"]["kyc"]["contact_mobile_number"]
                        KYC_StatusMessage["meta"]["kyc"]["address_street"]
                        Step="KYC Address Confirmed, Pending Employment Info..."
                        Label_UserStatus.config(text="⚫ Pending (KYC)\nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")   
                    except:
                        try:
                            KYC_StatusMessage["meta"]["kyc"]["sex"]
                            KYC_StatusMessage["meta"]["kyc"]["civil_id_number"]
                            KYC_StatusMessage["meta"]["kyc"]["civil_id_serial"]
                            Step="KYC Personal Info Confirmed, Pending Address Info..."
                            Label_UserStatus.config(text="⚫ Pending (KYC)\nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")   
                        except:
                            User_before_kyc=True

    if User_before_kyc:
        if StatusMessage["meta"]["email_is_verified"]==False:
            Step="User Sign up Confirmed, Pending Verifying Email..."
            Label_UserStatus.config(text="⚫ Pending \nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")   
        elif StatusMessage["meta"]["uploaded_civilID"] or StatusMessage["meta"]["is_eid_verified"] :
            Step="User Upload IDs Confirmed, Pending KYC..."
            Label_UserStatus.config(text="⚫ Pending \nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")   
            
            
        elif StatusMessage["meta"]["primary_id_front_scanned"]==False:
            Step="User verify email Confirmed, Pending Uploading IDs..."
            Label_UserStatus.config(text="⚫ Pending \nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")   

        elif StatusMessage["meta"]["primary_id_back_scanned"] == False :
            Step="User Front ID Confirmed, Pending Back ID..."
            Label_UserStatus.config(text="⚫ Pending \nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")   

        elif StatusMessage["meta"]["secondary_id_scanned"] == False:
            Step="User Front and Back ID Confirmed, Pending Video ID..."
            Label_UserStatus.config(text="⚫ Pending \nUser Last complete step is: "+Step,font=( "default",8, "bold"),foreground="#b9b513")   





    
def findStatus():
    text_box_Status.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Status.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Status.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Status.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Status.tag_config('found', background='orange')
        text_box_Status.focus_set()
        if text_box_Status.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=StatusWindow)

def OpenStatusWindow():
    global StatusWindow

    try:
        if 'normal' == StatusWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        StatusWindow.focus_set()
    elif Running==False:    
        StatusWindow = Toplevel()
        Topview.append(StatusWindow)
        StatusWindow.title("Status Information")
        StatusWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        StatusWindow.geometry("+%d+%d" %(x+500,y+10))
        
        message =UserInfo.StatusInfoAPI()
        global text_box_Status
        text_box_Status = Text(
            StatusWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Status.insert('end', message)
        text_box_Status.config(state='disabled')

        sb_Status = Scrollbar(StatusWindow,command=text_box_Status.yview,orient="vertical")
        text_box_Status.config(yscrollcommand=sb_Status.set)
        sb_Status.pack(side=RIGHT,fill="y",pady=65)
        text_box_Status.pack(expand=True,side=BOTTOM)


        global FindEntryStatus
        global FindEntryValue_Status
        FindEntryValue_Status=StringVar()
        Label(StatusWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryStatus = tk.Entry(StatusWindow,textvariable=FindEntryValue_Status)
        FindEntryStatus.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryStatus.focus_set()


        FindButtonStatus = Button(StatusWindow, text='Find')
        FindButtonStatus.pack(side=RIGHT)
        FindButtonStatus.config(command=findStatus)



def findKYC():
    text_box_KYC.tag_remove('found', '1.0', END)
    ser = FindEntryValue_KYC.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_KYC.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_KYC.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_KYC.tag_config('found', background='orange')
        text_box_KYC.focus_set()
        if text_box_KYC.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=KYCWindow)

def OpenKYCWindow():
    global KYCWindow
    
    
    try:
        if 'normal' == KYCWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        KYCWindow.focus_set()
    elif Running==False:    
    
        KYCWindow = Toplevel()
        Topview.append(KYCWindow)
        KYCWindow.title("KYC 3.0 Information")
        KYCWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        KYCWindow.geometry("+%d+%d" %(x+550,y+10))
        


        message = UserInfo.KYCInfoAPI()
        global text_box_KYC
        text_box_KYC = Text(
            KYCWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_KYC.insert('end', message)
        text_box_KYC.config(state='disabled')
        
        sb_KYC = Scrollbar(KYCWindow,command=text_box_KYC.yview,orient="vertical")
        text_box_KYC.config(yscrollcommand=sb_KYC.set)
        sb_KYC.pack(side=RIGHT,fill="y",pady=65)
        text_box_KYC.pack(expand=True,side=BOTTOM)

        global FindEntryKYC
        global FindEntryValue_KYC
        FindEntryValue_KYC=StringVar()
        Label(KYCWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryKYC = tk.Entry(KYCWindow,textvariable=FindEntryValue_KYC)
        FindEntryKYC.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryKYC.focus_set()


        FindButtonKYC = Button(KYCWindow, text='Find')
        FindButtonKYC.pack(side=RIGHT)
        FindButtonKYC.config(command=findKYC)



def findProfile():
    text_box_Profile.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Profile.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Profile.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Profile.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Profile.tag_config('found', background='orange')
        text_box_Profile.focus_set()
        if text_box_Profile.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=ProfileWindow)

def OpenProfileWindow():
    global ProfileWindow

    try:
        if 'normal' == ProfileWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        ProfileWindow.focus_set()
    elif Running==False:    
        ProfileWindow = Toplevel()
        Topview.append(ProfileWindow)
        ProfileWindow.title("Profile Information")
        ProfileWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        ProfileWindow.geometry("+%d+%d" %(x+600,y+10))
        
        message =UserInfo.ProfileInfoAPI()
        global text_box_Profile
        text_box_Profile = Text(
            ProfileWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Profile.insert('end', message)
        text_box_Profile.config(state='disabled')

        sb_Profile = Scrollbar(ProfileWindow,command=text_box_Profile.yview,orient="vertical")
        text_box_Profile.config(yscrollcommand=sb_Profile.set)
        sb_Profile.pack(side=RIGHT,fill="y",pady=65)
        text_box_Profile.pack(expand=True,side=BOTTOM)


        global FindEntryProfile
        global FindEntryValue_Profile
        FindEntryValue_Profile=StringVar()
        Label(ProfileWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryProfile = tk.Entry(ProfileWindow,textvariable=FindEntryValue_Profile)
        FindEntryProfile.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryProfile.focus_set()


        FindButtonProfile = Button(ProfileWindow, text='Find')
        FindButtonProfile.pack(side=RIGHT)
        FindButtonProfile.config(command=findProfile)



def findPortfolio():
    text_box_Portfolio.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Portfolio.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Portfolio.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Portfolio.tag_config('found', background='orange')
        text_box_Portfolio.focus_set()
        if text_box_Portfolio.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=PortfolioWindow)

def OpenPortfolioWindow():
    global PortfolioWindow

    try:
        if 'normal' == PortfolioWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        PortfolioWindow.focus_set()
    elif Running==False:    
        PortfolioWindow = Toplevel()
        Topview.append(PortfolioWindow)
        PortfolioWindow.title("Portfolio Information")
        PortfolioWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        PortfolioWindow.geometry("+%d+%d" %(x+650,y+10))
        
        message =UserInfo.PortfolioInfoAPI()
        global text_box_Portfolio
        text_box_Portfolio = Text(
            PortfolioWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Portfolio.insert('end', message)
        text_box_Portfolio.config(state='disabled')

        sb_Portfolio = Scrollbar(PortfolioWindow,command=text_box_Portfolio.yview,orient="vertical")
        text_box_Portfolio.config(yscrollcommand=sb_Portfolio.set)
        sb_Portfolio.pack(side=RIGHT,fill="y",pady=65)
        text_box_Portfolio.pack(expand=True,side=BOTTOM)


        global FindEntryPortfolio
        global FindEntryValue_Portfolio
        FindEntryValue_Portfolio=StringVar()
        Label(PortfolioWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryPortfolio = tk.Entry(PortfolioWindow,textvariable=FindEntryValue_Portfolio)
        FindEntryPortfolio.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryPortfolio.focus_set()


        FindButtonPortfolio = Button(PortfolioWindow, text='Find')
        FindButtonPortfolio.pack(side=RIGHT)
        FindButtonPortfolio.config(command=findPortfolio)


#?ADMIN INFO BELOW!!!
#ADMIN INFO BELOW!!!


def findAdminInfo():
    text_box_Admin_Info.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Info.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Info.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Info.tag_config('found', background='orange')
        text_box_Admin_Info.focus_set()
        if text_box_Admin_Info.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=AdminInfoWindow)

def OpenAdminInfoWindow():
    global AdminInfoWindow

    try:
        if 'normal' == AdminInfoWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        AdminInfoWindow.focus_set()
    elif Running==False:    
        AdminInfoWindow = Toplevel()
        Topview.append(AdminInfoWindow)
        AdminInfoWindow.title("User Admin Information")
        AdminInfoWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        AdminInfoWindow.geometry("+%d+%d" %(x+700,y+10))
        
        message =Admin.Info_API()
        
        
        global text_box_Admin_Info
        text_box_Admin_Info = Text(
            AdminInfoWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Info.insert('end', message)
        text_box_Admin_Info.config(state='disabled')

        sb_AdminInfo = Scrollbar(AdminInfoWindow,command=text_box_Admin_Info.yview,orient="vertical")
        text_box_Admin_Info.config(yscrollcommand=sb_AdminInfo.set)
        sb_AdminInfo.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Info.pack(expand=True,side=BOTTOM)


        global FindEntryAdminInfo
        global FindEntryValue_AdminInfo
        FindEntryValue_AdminInfo=StringVar()
        Label(AdminInfoWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryAdminInfo = tk.Entry(AdminInfoWindow,textvariable=FindEntryValue_AdminInfo)
        FindEntryAdminInfo.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryAdminInfo.focus_set()


        FindButtonAdminInfo = Button(AdminInfoWindow, text='Find')
        FindButtonAdminInfo.pack(side=RIGHT)
        FindButtonAdminInfo.config(command=findAdminInfo)



def findAdminAddress():
    text_box_Admin_Address.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Address.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Address.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Address.tag_config('found', background='orange')
        text_box_Admin_Address.focus_set()
        if text_box_Admin_Address.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=AdminAddressWindow)

def OpenAdminAddressWindow():
    global AdminAddressWindow

    try:
        if 'normal' == AdminAddressWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        AdminAddressWindow.focus_set()
    elif Running==False:    
        AdminAddressWindow = Toplevel()
        Topview.append(AdminAddressWindow)
        AdminAddressWindow.title("Admin Address Information")
        AdminAddressWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        AdminAddressWindow.geometry("+%d+%d" %(x+750,y+10))
        
        message =Admin.Address_API()
        
        
        global text_box_Admin_Address
        text_box_Admin_Address = Text(
            AdminAddressWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Address.insert('end', message)
        text_box_Admin_Address.config(state='disabled')

        sb_AdminAddress = Scrollbar(AdminAddressWindow,command=text_box_Admin_Address.yview,orient="vertical")
        text_box_Admin_Address.config(yscrollcommand=sb_AdminAddress.set)
        sb_AdminAddress.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Address.pack(expand=True,side=BOTTOM)


        global FindEntryAdminAddress
        global FindEntryValue_AdminAddress
        FindEntryValue_AdminAddress=StringVar()
        Label(AdminAddressWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryAdminAddress = tk.Entry(AdminAddressWindow,textvariable=FindEntryValue_AdminAddress)
        FindEntryAdminAddress.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryAdminAddress.focus_set()


        FindButtonAdminAddress = Button(AdminAddressWindow, text='Find')
        FindButtonAdminAddress.pack(side=RIGHT)
        FindButtonAdminAddress.config(command=findAdminAddress)



def findAdminSummary():
    text_box_Admin_Summary.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Summary.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Summary.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Summary.tag_config('found', background='orange')
        text_box_Admin_Summary.focus_set()
        if text_box_Admin_Summary.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=AdminSummaryWindow)

def OpenAdminSummaryWindow():
    global AdminSummaryWindow

    try:
        if 'normal' == AdminSummaryWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        AdminSummaryWindow.focus_set()
    elif Running==False:    
        AdminSummaryWindow = Toplevel()
        Topview.append(AdminSummaryWindow)
        AdminSummaryWindow.title("Admin Summary information")
        AdminSummaryWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        AdminSummaryWindow.geometry("+%d+%d" %(x+800,y+10))
        
        message =Admin.Summary_API()
        
        
        global text_box_Admin_Summary
        text_box_Admin_Summary = Text(
            AdminSummaryWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Summary.insert('end', message)
        text_box_Admin_Summary.config(state='disabled')

        sb_AdminSummary = Scrollbar(AdminSummaryWindow,command=text_box_Admin_Summary.yview,orient="vertical")
        text_box_Admin_Summary.config(yscrollcommand=sb_AdminSummary.set)
        sb_AdminSummary.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Summary.pack(expand=True,side=BOTTOM)


        global FindEntryAdminSummary
        global FindEntryValue_AdminSummary
        FindEntryValue_AdminSummary=StringVar()
        Label(AdminSummaryWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryAdminSummary = tk.Entry(AdminSummaryWindow,textvariable=FindEntryValue_AdminSummary)
        FindEntryAdminSummary.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryAdminSummary.focus_set()


        FindButtonAdminSummary = Button(AdminSummaryWindow, text='Find')
        FindButtonAdminSummary.pack(side=RIGHT)
        FindButtonAdminSummary.config(command=findAdminSummary)



def findAdminBank():
    text_box_Admin_Bank.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Bank.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Bank.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Bank.tag_config('found', background='orange')
        text_box_Admin_Bank.focus_set()
        if text_box_Admin_Bank.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=AdminBankWindow)

def OpenAdminBankWindow():
    global AdminBankWindow

    try:
        if 'normal' == AdminBankWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        AdminBankWindow.focus_set()
    elif Running==False:    
        AdminBankWindow = Toplevel()
        Topview.append(AdminBankWindow)
        AdminBankWindow.title("Admin Bank information")
        AdminBankWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        AdminBankWindow.geometry("+%d+%d" %(x+850,y+10))
        
        message =Admin.Bank_API()
        
        
        global text_box_Admin_Bank
        text_box_Admin_Bank = Text(
            AdminBankWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Bank.insert('end', message)
        text_box_Admin_Bank.config(state='disabled')

        sb_AdminBank = Scrollbar(AdminBankWindow,command=text_box_Admin_Bank.yview,orient="vertical")
        text_box_Admin_Bank.config(yscrollcommand=sb_AdminBank.set)
        sb_AdminBank.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Bank.pack(expand=True,side=BOTTOM)


        global FindEntryAdminBank
        global FindEntryValue_AdminBank
        FindEntryValue_AdminBank=StringVar()
        Label(AdminBankWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryAdminBank = tk.Entry(AdminBankWindow,textvariable=FindEntryValue_AdminBank)
        FindEntryAdminBank.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryAdminBank.focus_set()


        FindButtonAdminBank = Button(AdminBankWindow, text='Find')
        FindButtonAdminBank.pack(side=RIGHT)
        FindButtonAdminBank.config(command=findAdminBank)



def findAdminKYC_CID():
    text_box_Admin_KYC_CID.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_KYC_CID.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_KYC_CID.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_KYC_CID.tag_config('found', background='orange')
        text_box_Admin_KYC_CID.focus_set()
        if text_box_Admin_KYC_CID.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=AdminKYC_CIDWindow)

def OpenAdminKYC_CIDWindow():
    global AdminKYC_CIDWindow

    try:
        if 'normal' == AdminKYC_CIDWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        AdminKYC_CIDWindow.focus_set()
    elif Running==False:    
        AdminKYC_CIDWindow = Toplevel()
        Topview.append(AdminKYC_CIDWindow)
        AdminKYC_CIDWindow.title("Admin KYC_CID information")
        AdminKYC_CIDWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        AdminKYC_CIDWindow.geometry("+%d+%d" %(x+900,y+10))
        
        message =Admin.KYC_CID_Status_API()
        
        
        global text_box_Admin_KYC_CID
        text_box_Admin_KYC_CID = Text(
            AdminKYC_CIDWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_KYC_CID.insert('end', message)
        text_box_Admin_KYC_CID.config(state='disabled')

        sb_AdminKYC_CID = Scrollbar(AdminKYC_CIDWindow,command=text_box_Admin_KYC_CID.yview,orient="vertical")
        text_box_Admin_KYC_CID.config(yscrollcommand=sb_AdminKYC_CID.set)
        sb_AdminKYC_CID.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_KYC_CID.pack(expand=True,side=BOTTOM)


        global FindEntryAdminKYC_CID
        global FindEntryValue_AdminKYC_CID
        FindEntryValue_AdminKYC_CID=StringVar()
        Label(AdminKYC_CIDWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryAdminKYC_CID = tk.Entry(AdminKYC_CIDWindow,textvariable=FindEntryValue_AdminKYC_CID)
        FindEntryAdminKYC_CID.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryAdminKYC_CID.focus_set()


        FindButtonAdminKYC_CID = Button(AdminKYC_CIDWindow, text='Find')
        FindButtonAdminKYC_CID.pack(side=RIGHT)
        FindButtonAdminKYC_CID.config(command=findAdminKYC_CID)



def findAdminSteps():
    text_box_Admin_Steps.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Steps.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Steps.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Steps.tag_config('found', background='orange')
        text_box_Admin_Steps.focus_set()
        if text_box_Admin_Steps.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=AdminStepsWindow)

def OpenAdminStepsWindow():
    global AdminStepsWindow

    try:
        if 'normal' == AdminStepsWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        AdminStepsWindow.focus_set()
    elif Running==False:    
        AdminStepsWindow = Toplevel()
        Topview.append(AdminStepsWindow)
        AdminStepsWindow.title("Admin Steps information")
        AdminStepsWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        AdminStepsWindow.geometry("+%d+%d" %(x+950,y+10))
        
        message =Admin.Steps_API()
        
        
        global text_box_Admin_Steps
        text_box_Admin_Steps = Text(
            AdminStepsWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Steps.insert('end', message)
        text_box_Admin_Steps.config(state='disabled')

        sb_AdminSteps = Scrollbar(AdminStepsWindow,command=text_box_Admin_Steps.yview,orient="vertical")
        text_box_Admin_Steps.config(yscrollcommand=sb_AdminSteps.set)
        sb_AdminSteps.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Steps.pack(expand=True,side=BOTTOM)


        global FindEntryAdminSteps
        global FindEntryValue_AdminSteps
        FindEntryValue_AdminSteps=StringVar()
        Label(AdminStepsWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryAdminSteps = tk.Entry(AdminStepsWindow,textvariable=FindEntryValue_AdminSteps)
        FindEntryAdminSteps.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryAdminSteps.focus_set()


        FindButtonAdminSteps = Button(AdminStepsWindow, text='Find')
        FindButtonAdminSteps.pack(side=RIGHT)
        FindButtonAdminSteps.config(command=findAdminSteps)



def findAdminETF_Portfolio():
    text_box_Admin_ETF_Portfolio.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_ETF_Portfolio.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_ETF_Portfolio.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_ETF_Portfolio.tag_config('found', background='orange')
        text_box_Admin_ETF_Portfolio.focus_set()
        if text_box_Admin_ETF_Portfolio.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=AdminETF_PortfolioWindow)

def OpenAdminETF_PortfolioWindow():
    global AdminETF_PortfolioWindow

    try:
        if 'normal' == AdminETF_PortfolioWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        AdminETF_PortfolioWindow.focus_set()
    elif Running==False:    
        AdminETF_PortfolioWindow = Toplevel()
        Topview.append(AdminETF_PortfolioWindow)
        AdminETF_PortfolioWindow.title("Admin ETF_Portfolio information")
        AdminETF_PortfolioWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        AdminETF_PortfolioWindow.geometry("+%d+%d" %(x+1000,y+10))
        
        message =Admin.ETF_Portfolio_API()
        
        
        global text_box_Admin_ETF_Portfolio
        text_box_Admin_ETF_Portfolio = Text(
            AdminETF_PortfolioWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_ETF_Portfolio.insert('end', message)
        text_box_Admin_ETF_Portfolio.config(state='disabled')

        sb_AdminETF_Portfolio = Scrollbar(AdminETF_PortfolioWindow,command=text_box_Admin_ETF_Portfolio.yview,orient="vertical")
        text_box_Admin_ETF_Portfolio.config(yscrollcommand=sb_AdminETF_Portfolio.set)
        sb_AdminETF_Portfolio.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_ETF_Portfolio.pack(expand=True,side=BOTTOM)


        global FindEntryAdminETF_Portfolio
        global FindEntryValue_AdminETF_Portfolio
        FindEntryValue_AdminETF_Portfolio=StringVar()
        Label(AdminETF_PortfolioWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryAdminETF_Portfolio = tk.Entry(AdminETF_PortfolioWindow,textvariable=FindEntryValue_AdminETF_Portfolio)
        FindEntryAdminETF_Portfolio.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryAdminETF_Portfolio.focus_set()


        FindButtonAdminETF_Portfolio = Button(AdminETF_PortfolioWindow, text='Find')
        FindButtonAdminETF_Portfolio.pack(side=RIGHT)
        FindButtonAdminETF_Portfolio.config(command=findAdminETF_Portfolio)



def findAdminMMF_Portfolio():
    text_box_Admin_MMF_Portfolio.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_MMF_Portfolio.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_MMF_Portfolio.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_MMF_Portfolio.tag_config('found', background='orange')
        text_box_Admin_MMF_Portfolio.focus_set()
        if text_box_Admin_MMF_Portfolio.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=AdminMMF_PortfolioWindow)

def OpenAdminMMF_PortfolioWindow():
    global AdminMMF_PortfolioWindow

    try:
        if 'normal' == AdminMMF_PortfolioWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        AdminMMF_PortfolioWindow.focus_set()
    elif Running==False:    
        AdminMMF_PortfolioWindow = Toplevel()
        Topview.append(AdminMMF_PortfolioWindow)
        AdminMMF_PortfolioWindow.title("Admin MMF_Portfolio information")
        AdminMMF_PortfolioWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        AdminMMF_PortfolioWindow.geometry("+%d+%d" %(x+1050,y+10))
        
        message =Admin.MMF_Portfolio_API()
        
        
        global text_box_Admin_MMF_Portfolio
        text_box_Admin_MMF_Portfolio = Text(
            AdminMMF_PortfolioWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_MMF_Portfolio.insert('end', message)
        text_box_Admin_MMF_Portfolio.config(state='disabled')

        sb_AdminMMF_Portfolio = Scrollbar(AdminMMF_PortfolioWindow,command=text_box_Admin_MMF_Portfolio.yview,orient="vertical")
        text_box_Admin_MMF_Portfolio.config(yscrollcommand=sb_AdminMMF_Portfolio.set)
        sb_AdminMMF_Portfolio.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_MMF_Portfolio.pack(expand=True,side=BOTTOM)


        global FindEntryAdminMMF_Portfolio
        global FindEntryValue_AdminMMF_Portfolio
        FindEntryValue_AdminMMF_Portfolio=StringVar()
        Label(AdminMMF_PortfolioWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryAdminMMF_Portfolio = tk.Entry(AdminMMF_PortfolioWindow,textvariable=FindEntryValue_AdminMMF_Portfolio)
        FindEntryAdminMMF_Portfolio.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryAdminMMF_Portfolio.focus_set()


        FindButtonAdminMMF_Portfolio = Button(AdminMMF_PortfolioWindow, text='Find')
        FindButtonAdminMMF_Portfolio.pack(side=RIGHT)
        FindButtonAdminMMF_Portfolio.config(command=findAdminMMF_Portfolio)



def findAdminFunds():
    text_box_Admin_Funds.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Funds.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Funds.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Funds.tag_config('found', background='orange')
        text_box_Admin_Funds.focus_set()
        if text_box_Admin_Funds.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=AdminFundsWindow)

def OpenAdminFundsWindow():
    global AdminFundsWindow

    try:
        if 'normal' == AdminFundsWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        AdminFundsWindow.focus_set()
    elif Running==False:    
        AdminFundsWindow = Toplevel()
        Topview.append(AdminFundsWindow)
        AdminFundsWindow.title("Admin Funds information")
        AdminFundsWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        AdminFundsWindow.geometry("+%d+%d" %(x+1100,y+10))
        
        message =Admin.Funds_API()
        
        
        global text_box_Admin_Funds
        text_box_Admin_Funds = Text(
            AdminFundsWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Funds.insert('end', message)
        text_box_Admin_Funds.config(state='disabled')

        sb_AdminFunds = Scrollbar(AdminFundsWindow,command=text_box_Admin_Funds.yview,orient="vertical")
        text_box_Admin_Funds.config(yscrollcommand=sb_AdminFunds.set)
        sb_AdminFunds.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Funds.pack(expand=True,side=BOTTOM)


        global FindEntryAdminFunds
        global FindEntryValue_AdminFunds
        FindEntryValue_AdminFunds=StringVar()
        Label(AdminFundsWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryAdminFunds = tk.Entry(AdminFundsWindow,textvariable=FindEntryValue_AdminFunds)
        FindEntryAdminFunds.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryAdminFunds.focus_set()


        FindButtonAdminFunds = Button(AdminFundsWindow, text='Find')
        FindButtonAdminFunds.pack(side=RIGHT)
        FindButtonAdminFunds.config(command=findAdminFunds)



def findAdminDeposits():
    text_box_Admin_Deposits.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Deposits.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Deposits.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Deposits.tag_config('found', background='orange')
        text_box_Admin_Deposits.focus_set()
        if text_box_Admin_Deposits.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=AdminDepositsWindow)

def OpenAdminDepositsWindow():
    global AdminDepositsWindow

    try:
        if 'normal' == AdminDepositsWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        AdminDepositsWindow.focus_set()
    elif Running==False:    
        AdminDepositsWindow = Toplevel()
        Topview.append(AdminDepositsWindow)
        AdminDepositsWindow.title("Admin Deposits information")
        AdminDepositsWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        AdminDepositsWindow.geometry("+%d+%d" %(x+1150,y+10))
        
        message =Admin.Deposits_API()
        
        
        global text_box_Admin_Deposits
        text_box_Admin_Deposits = Text(
            AdminDepositsWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Deposits.insert('end', message)
        text_box_Admin_Deposits.config(state='disabled')

        sb_AdminDeposits = Scrollbar(AdminDepositsWindow,command=text_box_Admin_Deposits.yview,orient="vertical")
        text_box_Admin_Deposits.config(yscrollcommand=sb_AdminDeposits.set)
        sb_AdminDeposits.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Deposits.pack(expand=True,side=BOTTOM)


        global FindEntryAdminDeposits
        global FindEntryValue_AdminDeposits
        FindEntryValue_AdminDeposits=StringVar()
        Label(AdminDepositsWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryAdminDeposits = tk.Entry(AdminDepositsWindow,textvariable=FindEntryValue_AdminDeposits)
        FindEntryAdminDeposits.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryAdminDeposits.focus_set()


        FindButtonAdminDeposits = Button(AdminDepositsWindow, text='Find')
        FindButtonAdminDeposits.pack(side=RIGHT)
        FindButtonAdminDeposits.config(command=findAdminDeposits)



def findAdminWithdrawals():
    text_box_Admin_Withdrawals.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Withdrawals.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Withdrawals.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Withdrawals.tag_config('found', background='orange')
        text_box_Admin_Withdrawals.focus_set()
        if text_box_Admin_Withdrawals.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=AdminWithdrawalsWindow)

def OpenAdminWithdrawalsWindow():
    global AdminWithdrawalsWindow

    try:
        if 'normal' == AdminWithdrawalsWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        AdminWithdrawalsWindow.focus_set()
    elif Running==False:    
        AdminWithdrawalsWindow = Toplevel()
        Topview.append(AdminWithdrawalsWindow)
        AdminWithdrawalsWindow.title("Admin Withdrawals information")
        AdminWithdrawalsWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        AdminWithdrawalsWindow.geometry("+%d+%d" %(x+1200,y+10))
        
        message =Admin.Withdrawals_API()
        
        
        global text_box_Admin_Withdrawals
        text_box_Admin_Withdrawals = Text(
            AdminWithdrawalsWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Withdrawals.insert('end', message)
        text_box_Admin_Withdrawals.config(state='disabled')

        sb_AdminWithdrawals = Scrollbar(AdminWithdrawalsWindow,command=text_box_Admin_Withdrawals.yview,orient="vertical")
        text_box_Admin_Withdrawals.config(yscrollcommand=sb_AdminWithdrawals.set)
        sb_AdminWithdrawals.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Withdrawals.pack(expand=True,side=BOTTOM)


        global FindEntryAdminWithdrawals
        global FindEntryValue_AdminWithdrawals
        FindEntryValue_AdminWithdrawals=StringVar()
        Label(AdminWithdrawalsWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryAdminWithdrawals = tk.Entry(AdminWithdrawalsWindow,textvariable=FindEntryValue_AdminWithdrawals)
        FindEntryAdminWithdrawals.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryAdminWithdrawals.focus_set()


        FindButtonAdminWithdrawals = Button(AdminWithdrawalsWindow, text='Find')
        FindButtonAdminWithdrawals.pack(side=RIGHT)
        FindButtonAdminWithdrawals.config(command=findAdminWithdrawals)




def findpaci():
    text_box_Admin_Info.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Info.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Info.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Info.tag_config('found', background='orange')
        text_box_Admin_Info.focus_set()
        if text_box_Admin_Info.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=paciWindow)

def OpenpaciWindow():
    global paciWindow

    try:
        if 'normal' == paciWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        paciWindow.focus_set()
    elif Running==False:    
        paciWindow = Toplevel()
        Topview.append(paciWindow)
        paciWindow.title("User Admin Information")
        paciWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        paciWindow.geometry("+%d+%d" %(x+700,y+10))
        
        message =RiskEngineInfo.test_user_paci()
        
        
        global text_box_Admin_Info
        text_box_Admin_Info = Text(
            paciWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Info.insert('end', message)
        text_box_Admin_Info.config(state='disabled')

        sb_paci = Scrollbar(paciWindow,command=text_box_Admin_Info.yview,orient="vertical")
        text_box_Admin_Info.config(yscrollcommand=sb_paci.set)
        sb_paci.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Info.pack(expand=True,side=BOTTOM)


        global FindEntrypaci
        global FindEntryValue_paci
        FindEntryValue_paci=StringVar()
        Label(paciWindow,text='Find Flag:').pack(side=LEFT)
        FindEntrypaci = tk.Entry(paciWindow,textvariable=FindEntryValue_paci)
        FindEntrypaci.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntrypaci.focus_set()


        FindButtonpaci = Button(paciWindow, text='Find')
        FindButtonpaci.pack(side=RIGHT)
        FindButtonpaci.config(command=findpaci)



def findworld_check():
    text_box_Admin_Info.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Info.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Info.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Info.tag_config('found', background='orange')
        text_box_Admin_Info.focus_set()
        if text_box_Admin_Info.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=world_checkWindow)

def Openworld_checkWindow():
    global world_checkWindow

    try:
        if 'normal' == world_checkWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        world_checkWindow.focus_set()
    elif Running==False:    
        world_checkWindow = Toplevel()
        Topview.append(world_checkWindow)
        world_checkWindow.title("User Admin Information")
        world_checkWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        world_checkWindow.geometry("+%d+%d" %(x+700,y+10))
        
        message =RiskEngineInfo.test_user_world_check()
        
        
        global text_box_Admin_Info
        text_box_Admin_Info = Text(
            world_checkWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Info.insert('end', message)
        text_box_Admin_Info.config(state='disabled')

        sb_world_check = Scrollbar(world_checkWindow,command=text_box_Admin_Info.yview,orient="vertical")
        text_box_Admin_Info.config(yscrollcommand=sb_world_check.set)
        sb_world_check.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Info.pack(expand=True,side=BOTTOM)


        global FindEntryworld_check
        global FindEntryValue_world_check
        FindEntryValue_world_check=StringVar()
        Label(world_checkWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryworld_check = tk.Entry(world_checkWindow,textvariable=FindEntryValue_world_check)
        FindEntryworld_check.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryworld_check.focus_set()


        FindButtonworld_check = Button(world_checkWindow, text='Find')
        FindButtonworld_check.pack(side=RIGHT)
        FindButtonworld_check.config(command=findworld_check)





def findkyc():
    text_box_Admin_Info.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Info.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Info.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Info.tag_config('found', background='orange')
        text_box_Admin_Info.focus_set()
        if text_box_Admin_Info.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=kycWindow)

def OpenkycWindow():
    global kycWindow

    try:
        if 'normal' == kycWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        kycWindow.focus_set()
    elif Running==False:    
        kycWindow = Toplevel()
        Topview.append(kycWindow)
        kycWindow.title("User Admin Information")
        kycWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        kycWindow.geometry("+%d+%d" %(x+700,y+10))
        
        message =RiskEngineInfo.test_user_kyc
        
        
        global text_box_Admin_Info
        text_box_Admin_Info = Text(
            kycWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Info.insert('end', message)
        text_box_Admin_Info.config(state='disabled')

        sb_kyc = Scrollbar(kycWindow,command=text_box_Admin_Info.yview,orient="vertical")
        text_box_Admin_Info.config(yscrollcommand=sb_kyc.set)
        sb_kyc.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Info.pack(expand=True,side=BOTTOM)


        global FindEntrykyc
        global FindEntryValue_kyc
        FindEntryValue_kyc=StringVar()
        Label(kycWindow,text='Find Flag:').pack(side=LEFT)
        FindEntrykyc = tk.Entry(kycWindow,textvariable=FindEntryValue_kyc)
        FindEntrykyc.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntrykyc.focus_set()


        FindButtonkyc = Button(kycWindow, text='Find')
        FindButtonkyc.pack(side=RIGHT)
        FindButtonkyc.config(command=findkyc)




def findpep():
    text_box_Admin_Info.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Info.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Info.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Info.tag_config('found', background='orange')
        text_box_Admin_Info.focus_set()
        if text_box_Admin_Info.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=pepWindow)

def OpenpepWindow():
    global pepWindow

    try:
        if 'normal' == pepWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        pepWindow.focus_set()
    elif Running==False:    
        pepWindow = Toplevel()
        Topview.append(pepWindow)
        pepWindow.title("User Admin Information")
        pepWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        pepWindow.geometry("+%d+%d" %(x+700,y+10))
        
        message =RiskEngineInfo.test_user_pep()
        
        
        global text_box_Admin_Info
        text_box_Admin_Info = Text(
            pepWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Info.insert('end', message)
        text_box_Admin_Info.config(state='disabled')

        sb_pep = Scrollbar(pepWindow,command=text_box_Admin_Info.yview,orient="vertical")
        text_box_Admin_Info.config(yscrollcommand=sb_pep.set)
        sb_pep.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Info.pack(expand=True,side=BOTTOM)


        global FindEntrypep
        global FindEntryValue_pep
        FindEntryValue_pep=StringVar()
        Label(pepWindow,text='Find Flag:').pack(side=LEFT)
        FindEntrypep = tk.Entry(pepWindow,textvariable=FindEntryValue_pep)
        FindEntrypep.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntrypep.focus_set()


        FindButtonpep = Button(pepWindow, text='Find')
        FindButtonpep.pack(side=RIGHT)
        FindButtonpep.config(command=findpep)




def findcountries():
    text_box_Admin_Info.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Info.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Info.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Info.tag_config('found', background='orange')
        text_box_Admin_Info.focus_set()
        if text_box_Admin_Info.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=countriesWindow)

def OpencountriesWindow():
    global countriesWindow

    try:
        if 'normal' == countriesWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        countriesWindow.focus_set()
    elif Running==False:    
        countriesWindow = Toplevel()
        Topview.append(countriesWindow)
        countriesWindow.title("User Admin Information")
        countriesWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        countriesWindow.geometry("+%d+%d" %(x+700,y+10))
        
        message =RiskEngineInfo.test_user_countries()
        
        
        global text_box_Admin_Info
        text_box_Admin_Info = Text(
            countriesWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Info.insert('end', message)
        text_box_Admin_Info.config(state='disabled')

        sb_countries = Scrollbar(countriesWindow,command=text_box_Admin_Info.yview,orient="vertical")
        text_box_Admin_Info.config(yscrollcommand=sb_countries.set)
        sb_countries.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Info.pack(expand=True,side=BOTTOM)


        global FindEntrycountries
        global FindEntryValue_countries
        FindEntryValue_countries=StringVar()
        Label(countriesWindow,text='Find Flag:').pack(side=LEFT)
        FindEntrycountries = tk.Entry(countriesWindow,textvariable=FindEntryValue_countries)
        FindEntrycountries.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntrycountries.focus_set()


        FindButtoncountries = Button(countriesWindow, text='Find')
        FindButtoncountries.pack(side=RIGHT)
        FindButtoncountries.config(command=findcountries)




def findemployment():
    text_box_Admin_Info.tag_remove('found', '1.0', END)
    ser = FindEntryValue_Portfolio.get()
    if ser:
        idx = '1.0'
        while True:
            idx = text_box_Admin_Info.search(ser, idx, nocase=1,stopindex=END)
            if not idx: break 

            lastidx = '%s+%dc' % (idx, len(ser))
            text_box_Admin_Info.tag_add('found', idx, lastidx)
            idx = lastidx
        text_box_Admin_Info.tag_config('found', background='orange')
        text_box_Admin_Info.focus_set()
        if text_box_Admin_Info.tag_ranges('found')==():
            messagebox.showinfo(title="Not Found", message="Flag is not found!!",parent=employmentWindow)

def OpenemploymentWindow():
    global employmentWindow

    try:
        if 'normal' == employmentWindow.state():
            Running=True
        else:
            Running=False
    except:
        Running=False
    # if 'normal' == KYCWindow.state():
    #     print("KYC window is running")
        
    if Running:
        employmentWindow.focus_set()
    elif Running==False:    
        employmentWindow = Toplevel()
        Topview.append(employmentWindow)
        employmentWindow.title("User Admin Information")
        employmentWindow.geometry('800x1000')
        x = master.winfo_x()
        y = master.winfo_y()
        employmentWindow.geometry("+%d+%d" %(x+700,y+10))
        
        message =RiskEngineInfo.test_user_employment()
        
        
        global text_box_Admin_Info
        text_box_Admin_Info = Text(
            employmentWindow,
            foreground="blue",
            height=55,
            width=100,
            background="#c0c0c0",
            wrap='word'
        )
        text_box_Admin_Info.insert('end', message)
        text_box_Admin_Info.config(state='disabled')

        sb_employment = Scrollbar(employmentWindow,command=text_box_Admin_Info.yview,orient="vertical")
        text_box_Admin_Info.config(yscrollcommand=sb_employment.set)
        sb_employment.pack(side=RIGHT,fill="y",pady=65)
        text_box_Admin_Info.pack(expand=True,side=BOTTOM)


        global FindEntryemployment
        global FindEntryValue_employment
        FindEntryValue_employment=StringVar()
        Label(employmentWindow,text='Find Flag:').pack(side=LEFT)
        FindEntryemployment = tk.Entry(employmentWindow,textvariable=FindEntryValue_employment)
        FindEntryemployment.pack(side=LEFT, fill=BOTH, expand=1)
        FindEntryemployment.focus_set()


        FindButtonemployment = Button(employmentWindow, text='Find')
        FindButtonemployment.pack(side=RIGHT)
        FindButtonemployment.config(command=findemployment)



global InputButtons,Topview
Topview=[]
InputButtons=[]
master = Tk()
master.minsize(width=375,height=1000)
# master.attributes('-zoomed', True)
# master.state('zoomed')
master.geometry("+%d+%d" %(0,0))
master.iconbitmap(r"C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\GUI\\NEOLogo.ico")
master.title("Backend Panel Check")

# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file = r"C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\GUI\\NEOLogo.png")
img1 = img.subsample(5, 5)
Label(master, image = img1).grid(row = 0, column = 0,
       columnspan = 5, rowspan = 1)



global EmailLabel
EmailLabel = Label(master, text = "Email: ")
EmailLabel.grid(row = 3, column = 0)
        
global EmailEntry
EmailEntryValue=StringVar()
EmailEntry=tk.Entry(master,textvariable=EmailEntryValue,width=60)
EmailEntry.config(font=("TkDefaultFont", 8))
# EmailEntry.place(height=20,width=10 )
EmailEntry.grid(row = 3, column = 1,columnspan=2 ,pady=5)
EmailEntry.config(state="normal")


global EmailCheckbox
EmailCheckboxValue=BooleanVar()
EmailCheckbox= Checkbutton(master, 
               text="Confirm",
               variable=EmailCheckboxValue,onvalue=True,offvalue=False,command=VerifyEmail)
EmailCheckbox.grid(row = 5, column = 2,sticky=W)


CloseAllButton = tk.Button(master, text = "Close",command= Closeallwindows,width=8,font=( "default",7, "bold"))
CloseAllButton.grid(row = 5, column = 0,sticky=E)


RefreshButton = tk.Button(master, text = "Refresh",command= Analyze_User_Status,width=8,font=( "default",7, "bold"))
RefreshButton.grid(row = 5, column = 1,sticky=W)
InputButtons.append(RefreshButton)




link_to_fe_test_button = tk.Button(master, text = "Link to FE Test",command= link_to_fe_test,width=12,font=( "default",7, "bold"))
link_to_fe_test_button.grid(row = 5, column = 3,sticky=W)
# InputButtons.append(link_to_fe_test_button)



# separator = Separator(master, orient='horizontal')
# separator.grid(row=6,column=0,columnspan=4, sticky="ew", padx=10, pady=10)

Label_UserStatus=Label(master, text="")
Label_UserStatus.config(font=( "default",8, "bold"),foreground="#057e0c")
Label_UserStatus.grid(row=6,column=0,columnspan=4)

# Step="KYC Personal Info"
# Label_UserStop=Label(master, text="User Last complete step is: "+Step)
# Label_UserStop.config(font=( "default",8, "bold"),foreground="#9d9d00")
# Label_UserStop.grid(row=7,column=0,columnspan=3)

Label1=Label(master, text="Access User's Info.")
Label1.config(font=( "default",20, "bold"),foreground="#7857fd")
Label1.grid(row=9,column=0,columnspan=3,sticky=W,rowspan=2,ipady=30,padx=10)

separator1 = Separator(master, orient='horizontal')
separator1.grid(row=10,column=0,columnspan=4, sticky="ew", padx=10, pady=15)

StatusButton = Button(master, text = "Open User's Status",command= OpenStatusWindow,width=30)
StatusButton.grid(row = 11, column = 0,columnspan=3)
InputButtons.append(StatusButton)

KYCButton = Button(master, text = "Open User's KYC",command= OpenKYCWindow,width=30)
KYCButton.grid(row = 12, column = 0,columnspan=3)
InputButtons.append(KYCButton)

ProfileButton = Button(master, text = "Open User's Profile Info",command= OpenProfileWindow,width=30)
ProfileButton.grid(row = 13, column=0,columnspan=3)
InputButtons.append(ProfileButton)
ProfileButton.config(state="disabled")

PortfolioButton = Button(master, text = "Open User's Portfolio Info",command= OpenPortfolioWindow,width=30)
PortfolioButton.grid(row = 14, column=0,columnspan=3)
InputButtons.append(PortfolioButton)

# Blank=Label(master, text="")
# Blank.config(font=("default",20, "bold"),foreground="#7857fd")
# Blank.grid(row=14,column=0,columnspan=3,sticky=N,rowspan=2,ipady=15)


Label2=Label(master, text="Access User's Admin Info.")
Label2.config(font=("default",20, "bold"),foreground="#7857fd")
Label2.grid(row=15,column=0,columnspan=3,sticky=W,rowspan=2,ipady=10,padx=10)

separator2 = Separator(master, orient='horizontal')
separator2.grid(row=17,column=0,columnspan=4, sticky="ew", pady=15)

AdminInfoButton = Button(master, text = "Open User's Admin Info",command= OpenAdminInfoWindow,width=30)
AdminInfoButton.grid(row = 18, column=0,columnspan=3)
InputButtons.append(AdminInfoButton)

AdminAddressButton = Button(master, text = "Open User's Address Admin Info",command= OpenAdminAddressWindow,width=30)
AdminAddressButton.grid(row = 19, column=0,columnspan=3)
InputButtons.append(AdminAddressButton)

AdminSummaryButton = Button(master, text = "Open User's Summary Admin Info",command= OpenAdminSummaryWindow,width=30)
AdminSummaryButton.grid(row = 20, column=0,columnspan=3)
InputButtons.append(AdminSummaryButton)


AdminBankButton = Button(master, text = "Open User's Bank Admin Info",command= OpenAdminBankWindow,width=30)
AdminBankButton.grid(row = 21, column=0,columnspan=3)
InputButtons.append(AdminBankButton)


Admin_KYC_CID_Button = Button(master, text = "Open User's KYC CID Admin Info",command= OpenAdminKYC_CIDWindow,width=30)
Admin_KYC_CID_Button.grid(row = 22, column=0,columnspan=3)
InputButtons.append(Admin_KYC_CID_Button)


AdminStepsButton = Button(master, text = "Open User's Steps Admin Info",command= OpenAdminStepsWindow,width=30)
AdminStepsButton.grid(row = 23, column=0,columnspan=3)
InputButtons.append(AdminStepsButton)


AdminETFPortfolioButton = Button(master, text = "Open User's ETF Portfolios Admin Info",command= OpenAdminETF_PortfolioWindow,width=30)
AdminETFPortfolioButton.grid(row = 24, column=0,columnspan=3)
InputButtons.append(AdminETFPortfolioButton)


AdminMMFPortfolioButton = Button(master, text = "Open User's MMF Portfolios Admin Info",command= OpenAdminMMF_PortfolioWindow,width=30)
AdminMMFPortfolioButton.grid(row = 25, column=0,columnspan=3)
InputButtons.append(AdminMMFPortfolioButton)


AdminFundsButton = Button(master, text = "Open User's Funds Admin Info",command= OpenAdminFundsWindow,width=30)
AdminFundsButton.grid(row = 26, column=0,columnspan=3)
InputButtons.append(AdminFundsButton)


AdminDepositsButton = Button(master, text = "Open User's Deposits Admin Info",command= OpenAdminDepositsWindow,width=30)
AdminDepositsButton.grid(row = 27, column=0,columnspan=3)
InputButtons.append(AdminDepositsButton)


AdminWithdrawalsButton = Button(master, text = "Open User's Withdrawals Admin Info",command= OpenAdminWithdrawalsWindow,width=30)
AdminWithdrawalsButton.grid(row = 28, column=0,columnspan=3)
InputButtons.append(AdminWithdrawalsButton)


# AdminCivilIDsButton = Button(master, text = "Open User's CivilIDs Admin Info",command= OpenProfileWindow,width=30)
# AdminCivilIDsButton.grid(row = 12, column=0,columnspan=3)
# InputButtons.append(AdminCivilIDsButton)
# AdminCivilIDsButton.config(state="disabled")


# AdminContractButton = Button(master, text = "Open User's Contract Admin Info",command= OpenProfileWindow,width=30)
# AdminContractButton.grid(row = 12, column=0,columnspan=3)
# InputButtons.append(AdminContractButton)
# AdminContractButton.config(state="disabled")




Label2=Label(master, text="Access User's Risk Engine")
Label2.config(font=("default",20, "bold"),foreground="#7857fd")
Label2.grid(row=30,column=0,columnspan=3,sticky=W,rowspan=2,ipady=10,padx=10)

separator2 = Separator(master, orient='horizontal')
separator2.grid(row=32,column=0,columnspan=4, sticky="ew", pady=15)

paciButton = Button(master, text = "Open PACI Info",command= OpenpaciWindow,width=30)
paciButton.grid(row = 33, column=0,columnspan=3)
InputButtons.append(paciButton)

world_checkButton = Button(master, text = "Open World Check Info",command= Openworld_checkWindow,width=30)
world_checkButton.grid(row = 34, column=0,columnspan=3)
InputButtons.append(world_checkButton)

kycButton = Button(master, text = "Open KYC Info",command= OpenkycWindow,width=30)
kycButton.grid(row = 35, column=0,columnspan=3)
InputButtons.append(kycButton)

pepButton = Button(master, text = "Open PEP Info",command= OpenpepWindow,width=30)
pepButton.grid(row = 36, column=0,columnspan=3)
InputButtons.append(pepButton)

countriesButton = Button(master, text = "Open Countries Info",command= OpencountriesWindow,width=30)
countriesButton.grid(row = 37, column=0,columnspan=3)
InputButtons.append(countriesButton)

employmentButton = Button(master, text = "Open Employment Info",command= OpenemploymentWindow,width=30)
employmentButton.grid(row = 38, column=0,columnspan=3)
InputButtons.append(employmentButton)





# DisableButtons()
DisableButtons()
# ValidateAuth(AuthSuccess)

    
        


try:    mainloop()
except: print("Window Destroyed!!")


