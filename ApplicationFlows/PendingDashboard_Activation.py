
from time import sleep
from ActivateUser import ActivateUser
from Approve_User_From_Admin_Collection import APIScript_RunCollection_ApproveUserAdmin
from GesturesAndMotions import RefreshScreenusingswipe, taponcoordinates
from KYC import KYC_FillAll
from PendingDashboard import PendingDashboard
from PerformInitialDepositFlow import InitialDepositFlow
from SignContractFlow import SignContract
from UploadIDs import UploadIDsAndCaptureVideo


def PendingDashboardSteps_untilActiveDashboard(driver,ReportDriver,JSON,Credentials,AdminAuthorization=None):
    	
    PendingDashboard_StepsDone= PendingDashboard(driver,ReportDriver)
    print((PendingDashboard_StepsDone))

    if PendingDashboard_StepsDone==[False,False,False]:
        UploadIDsAndCaptureVideo(driver,ReportDriver)
        
        PendingDashboard(driver,ReportDriver)
        KYC_FillAll(driver,ReportDriver,JSON)
        SignContract(driver,ReportDriver)
        sleep(3)
        
        User_ID= APIScript_RunCollection_ApproveUserAdmin(ReportDriver,Credentials["Email"],AdminAuthorization)
        
        #Refresh Application
        driver.press_keycode(187)
        sleep(2)
        taponcoordinates(driver,550,850)
        
        PendingDashboard(driver,ReportDriver)
        InitialDepositFlow(driver,ReportDriver,User_ID,"Bank Transfer",Credentials["User_Type"])
        
        ActivateUser(ReportDriver,User_ID)
        
        #Refresh Application
        driver.press_keycode(187)
        sleep(2)
        taponcoordinates(driver,550,850)
        
        try:RefreshScreenusingswipe(driver)
        except:print("Can't Refresh Screen")
        
        
        
    elif PendingDashboard_StepsDone==[True,False,False]:
        # KYC_FillAll(driver,ReportDriver,JSON)
        KYC_FillAll(driver,ReportDriver,JSON)
        SignContract(driver,ReportDriver)
        
        User_ID= APIScript_RunCollection_ApproveUserAdmin(ReportDriver,Credentials["Email"],AdminAuthorization)
        
        #Refresh Application
        driver.press_keycode(187)
        sleep(2)
        taponcoordinates(driver,550,850)
        
        PendingDashboard(driver,ReportDriver)
        InitialDepositFlow(driver,ReportDriver,User_ID,"Bank Transfer",Credentials["User_Type"])
        
        ActivateUser(ReportDriver,User_ID)
        
        #Refresh Application
        driver.press_keycode(187)
        sleep(2)
        taponcoordinates(driver,550,850)
        try:RefreshScreenusingswipe(driver)
        except:print("Can't Refresh Screen")

        
    elif PendingDashboard_StepsDone==[True,True,False]:
        
        User_ID= APIScript_RunCollection_ApproveUserAdmin(ReportDriver,Credentials["Email"],AdminAuthorization)
        # User_ID="6e0a8d9c-b0d7-494b-8b58-cebe712f2016"
        #Refresh Application
        driver.press_keycode(187)
        sleep(2)
        taponcoordinates(driver,550,850)
        
        PendingDashboard(driver,ReportDriver)
        InitialDepositFlow(driver,ReportDriver,User_ID,"Bank Transfer",Credentials["User_Type"])
        
        ActivateUser(ReportDriver,User_ID)
        
        #Refresh Application
        driver.press_keycode(187)
        sleep(2)
        taponcoordinates(driver,550,850)
        try:RefreshScreenusingswipe(driver)
        except:print("Can't Refresh Screen")
