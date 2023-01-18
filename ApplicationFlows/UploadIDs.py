
from bdb import Breakpoint
import json
from time import sleep
from tkinter import E
from unittest import TestCase
from CheckFlowAndProceed import CheckFlow_ContinueReg_Showme
from EIDFallBackScreen import EIDFallBackScreen
from GesturesAndMotions import taponcoordinates
from GetStartedScreen import GetStartedScreen_SignIn
from ManualReport import ReportResults
from PendingDashboard import PendingDashboard
from PermissionSreens import PermissionScreensText
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from SignInScreen import SignInScreen_Test

from UploadIDAPI import UploadIDAPI

def UploadIDsAndCaptureVideo(driver,ReportDriver):
    
    EIDStarted=False
    TestCase ="Upload IDs and Capture Video"
    Status=True
    
    
    TestCase1 ="Accessing Permission to Camera and Microphone"
    try:
        print("Wait for Audio Toggle")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/audioToggleButton"))).click()
        print("Audio Toggle Button Found")
        EIDStarted=True
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase1, message="Permission is already granted", passed=True, screenshot=False)
    except:
        EIDStarted =False
        # PermissionScreensText(driver,ReportDriver)
        # ReportDriver.report().step(description=TestCase1, message=TestCase1+" is Successful!!", passed=True, screenshot=False)
    
    if EIDStarted==False:
        try:
            Areyoufacingissues =WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/descriptionTextView")))
        except:
            PermissionScreensText(driver,ReportDriver)
            PermissionGranted=True
    
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/audioToggleButton"))).click()
    except:
        print("Issue in EID going to fallback flow")      
    

    # try:
    #     UploadID2Button=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/secondCardView")))
    #     EIDFallback=True
    #     print("TryWorked")
    # except:
    #     EIDFallback=False
    Orientation="LANDSCAPE"
    # AudioToggleButton =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/audioToggleButton")))
    # AudioToggleButton.click()
    while Orientation!="PORTRAIT":
        WebDriverWait(driver, 70).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/descriptionTextView")))
        Orientation=driver.orientation
        if Orientation!="PORTRAIT":
            sleep(3)

        # Areyoufacingissues =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/descriptionTextView")
    YesButton= driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/yesButton")  
    YesButton.click()
    
    
    #Permission is asked again on EID Fallback
    # try:
    #     AllowWhileUsingTheApp=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
    #     AllowWhileUsingTheApp.click()
    # except:
    #     print("Permission not shown of fallback ID")
        
    EIDFallBackScreen(driver,ReportDriver)
    
    
    
        #### Upload first ID ####
        
    TestCase2 ="Uploading first ID"
    
    try:
        UploadID1Button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"neo.nbkc.smartwealth.demo:id/firstCardView")))
        ID1Uploaded=False
        UploadID1Button.click()
    except:
        ID1Uploaded=True
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase2, message=TestCase2+" is already uploaded!!", passed=True, screenshot=False)

        
        #Open Camera
        #Camera=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.ViewPager/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.ImageView")
        #Camera.click()


    if ID1Uploaded==False:

        try: WebDriverWait(driver,8).until(EC.visibility_of_element_located((By.ID,"android:id/text1")))
        except:
            driver.press_keycode(4)
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/firstCardView")
            sleep(2)
            try:driver.find_element(By.ID,"android:id/text1")
            except:
                print("Can't find the camera")
                Breakpoint()
                        
        elementList = driver.find_elements(By.ID,"android:id/text1")
        clickableElementList = driver.find_elements(By.ID,"android:id/sem_chooser_grid_item_view")

        print(len(elementList))
        print(len(clickableElementList))
        
        for i in range(0,len(elementList)):
            if elementList[i].text=="Camera":
                Camera=elementList[i]
                elementList[i].click()
                print("Camera Found and Clicked")
                break
            else:
                print( "Didn't find camera to click it")
        
        try:
            driver.find_elements(By.ID,"android:id/sem_chooser_grid_item_view")
            Camera.click()
        except:
            print ("Camera Clicked")
        
        # Samsung A52
        # Capture=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"com.sec.android.app.camera:id/normal_center_button")))
        
        Capture=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"com.android.camera2:id/shutter_button")))
        Capture.click()

        OkButton =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "com.android.camera2:id/done_button")))
        OkButton.click()
                        
        UsePhoto =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/uploadTextView")))
        UsePhoto.click()

        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase2, message=TestCase2+" is Successful!!", passed=True, screenshot=False)

        




    #### Upload second ID ####
        
    TestCase3 ="Uploading second ID"
        
    try:    
        UploadID2Button=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/secondCardView")))
        UploadID2Button.click()
        ID2Uploaded=False
    except:
        print("Not clickable")
        ID2Uploaded=True
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase2, message=TestCase2+" is already uploaded!!", passed=True, screenshot=False)
        SubmitButton=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton")
        SubmitButton.click()
        
        
                
        #Open Camera
        #Camera=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.ViewPager/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.ImageView")
        #Camera.click()

    if ID2Uploaded==False:    
        try: WebDriverWait(driver,8).until(EC.visibility_of_element_located((By.ID,"android:id/text1")))
        except:
            driver.press_keycode(4)
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/secondCardView")
            sleep(2)
            try:driver.find_element(By.ID,"android:id/text1")
            except:
                print("Can't find the camera")
                Breakpoint()
            

        elementList = driver.find_elements(By.ID,"android:id/text1")
        clickableElementList = driver.find_elements(By.ID,"android:id/sem_chooser_grid_item_view")

        print(len(elementList))
        print(len(clickableElementList))
        
        for i in range(0,len(elementList)):
            if elementList[i].text=="Camera":
                Camera=elementList[i]
                elementList[i].click()
                print("Camera Found and Clicked")
                break
            else:
                print( "Didn't find camera to click it")
        # Samsung A52
        # Capture=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"com.sec.android.app.camera:id/normal_center_button")))
        
        try:
            driver.find_elements(By.ID,"android:id/sem_chooser_grid_item_view")
            Camera.click()
        except:
            print ("Camera Clicked")
        
        Capture=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"com.android.camera2:id/shutter_button")))
        Capture.click()

        OkButton =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "com.android.camera2:id/done_button")))
        OkButton.click()
                        
        UsePhoto =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/uploadTextView")))
        UsePhoto.click()

        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase2, message=TestCase2+" is Successful!!", passed=True, screenshot=False)
        
        
        #Submit 2 IDS and take video
        SubmitButton=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/submitButton")))
        SubmitButton.click()
    
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase3, message=TestCase3+" is Successful!!", passed=True, screenshot=False)

        
        #### Take Video ID ####
    
    TestCase4="UploadVideoID"
    Title1=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvName")))
    Description1=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvRecordingStart")
    
    # Title1Expected1="For verification purposes, we need a recording of yourself saying a statement."
    # Description1Expected="Your information will be encrypted, stored securely, and only ever used to verify your identity."
    
    # if Title1 !=Title1Expected1:
    #         Status=False
    #         ReportResults(ReportDriver, driver, Status,TestCase,Title1.text,Title1Expected1)
            
    # if Description1 != Description1Expected:
    #         Status=False
    #         ReportResults(ReportDriver, driver, Status,TestCase,Description1.text,Description1Expected)
    
    
    NextButton=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/btnNext")))
    NextButton.click()

    #Permission is asked again on EID Fallback
    # try:
    #     AllowWhileUsingTheApp=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
    #     AllowWhileUsingTheApp.click()
    # except:
    #     print("Permission not shown of fallback video")

    RecordButton=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/recordButton")))
    RecordButton.click()

    sleep(2)

    StopButton=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/actionButton")))
    StopButton.click()

    sleep(1)
    
    SubmitButton=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btnSubmit")))
    SubmitButton.click()
    sleep(1)
    try:
        NextButton=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btnPositive")))
        NextButton.click()
        flag=True
    except:
        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnSubmit").click()
        flag=False

    try:
        NextButton=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btnPositive")))
        NextButton.click()
        flag=True
    except:
        print ("Uploading ID worked")

    if ReportDriver==None:
        print("No Report Driver found")
    elif Status==True:
        ReportDriver.report().step(description=TestCase4, message=TestCase4+" is Successful!!", passed=True, screenshot=False)
        ReportDriver.report().test(name=TestCase, message=TestCase+" is Successful!!", passed=True)
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)

def UploadIDsAndCaptureVideo_Detailed(driver,ReportDriver):
    
    EIDFallback=False
    TestCase ="Upload IDs and Capture Video"
    
    
    TestCase1 ="Accessing Permission to Camera and Microphone"
    try:
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tv_title")))
        PermissionScreensText(driver,ReportDriver)
        Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        Titles[0].click() # Go to EID flow    
    except:
        print("Access already granted")
        PermissionGranted=True
        
    if ReportDriver==None: print("No Report Driver found")
    else:ReportDriver.report().step(description=TestCase1, message=TestCase1+" is Successful!!", passed=True, screenshot=False)

    try:
        UploadID2Button=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/secondCardView")))
        EIDFallback=True
        print("TryWorked")
    except:
        EIDFallback=False

    if EIDFallback==False:
        print("ExceptWorked")
        AudioToggleButton =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/audioToggleButton")))
        AudioToggleButton.click()
            
        Areyoufacingissues =WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/descriptionTextView")))
        YesButton= driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/yesButton")  
        YesButton.click()
    
    
    #Permission is asked again on EID Fallback
    try:
        AllowWhileUsingTheApp=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
        AllowWhileUsingTheApp.click()
    except:
        print("Permission not shown of fallback ID")
        
    EIDFallBackScreen(driver,ReportDriver)
    
    
    
        #### Upload first ID ####
        
    TestCase2 ="Uploading first ID"
    
    try:
        UploadID1Button=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/firstCardView")
        UploadID1Button.click()
        
        #Open Camera
        #Camera=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.ViewPager/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.ImageView")
        #Camera.click()
        
        taponcoordinates(driver,270,1500)

        
        sleep(2)
        taponcoordinates(driver,350,1400)
        sleep(2)
        taponcoordinates(driver,500,1400)

        UsePhoto =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/uploadTextView")))
        UsePhoto.click()
        
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase2, message=TestCase2+" is Successful!!", passed=True, screenshot=False)

        
    except:
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase2, message=TestCase2+" is already uploaded!!", passed=True, screenshot=False)




        #### Upload second ID ####
        
    TestCase3 ="Uploading second ID"
        
    try:    
        UploadID2Button=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/secondCardView")))
        UploadID2Button.click()
        
        #Open Camera
        #Camera=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.ViewPager/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.ImageView")
        #Camera.click()
        
        taponcoordinates(driver,270,1500)
            
        sleep(2)
        taponcoordinates(driver,350,1400)
        sleep(2)
        taponcoordinates(driver,500,1400)

        UsePhoto =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/uploadTextView")))
        UsePhoto.click()
    
        #Submit 2 IDS and take video
        SubmitButton=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton")
        SubmitButton.click()
    
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase3, message=TestCase3+" is Successful!!", passed=True, screenshot=False)
    except:
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase3, message=TestCase3+" is already uploaded!!", passed=True, screenshot=False)
        SubmitButton=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton")
        SubmitButton.click()
        
        
        #### Take Video ID ####
    
    TestCase4="UploadVideoID"
    Title1=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvName")))
    Description1=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvRecordingStart")
    
    Title1Expected1="For verification purposes, we need a recording of yourself saying a statement."
    Description1Expected="Your information will be encrypted, stored securely, and only ever used to verify your identity."
    
    if Title1 !=Title1Expected1:
            Status=False
            ReportResults(ReportDriver, driver, Status,TestCase,Title1.text,Title1Expected1)
            
    if Description1 != Description1Expected:
            Status=False
            ReportResults(ReportDriver, driver, Status,TestCase,Description1.text,Description1Expected)
    
    
    NextButton=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnNext")
    NextButton.click()
    
    #Permission is asked again on EID Fallback
    try:
        AllowWhileUsingTheApp=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
        AllowWhileUsingTheApp.click()
    except:
        print("Permission not shown of fallback video")
    
    RecordButton=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/recordButton")))
    RecordButton.click()
    
    sleep(2)
    
    StopButton=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/actionButton")))
    StopButton.click()
    
    SubmitButton=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btnSubmit")))
    SubmitButton.click()
    
    
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status==True:
        ReportDriver.report().step(description=TestCase4, message=TestCase4+" is Successful!!", passed=True, screenshot=False)
        ReportDriver.report().test(name=TestCase, message=TestCase+" is Successful!!", passed=True)
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)

def UploadIDSmokeTests(driver,ReportDriver):
    
    EIDStarted=False
    TestCase ="Upload IDs and Capture Video"
    Status=True
    
    
    TestCase1 ="Accessing Permission to Camera and Microphone"
    PermissionScreensText(driver,ReportDriver)

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/audioToggleButton"))).click()
    except:
        print("Audio button not found")      
    


    Orientation="LANDSCAPE"
    # AudioToggleButton =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/audioToggleButton")))
    # AudioToggleButton.click()
    while Orientation!="PORTRAIT":
        WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/yesButton")))
        driver.orientation = "PORTRAIT"
        sleep(2)
        Orientation=driver.orientation
        if Orientation!="PORTRAIT":
            sleep(3)

        # Areyoufacingissues =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/descriptionTextView")
    YesButton= driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/yesButton")  
    YesButton.click()
    
    
    #Permission is asked again on EID Fallback
    # try:
    #     AllowWhileUsingTheApp=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
    #     AllowWhileUsingTheApp.click()
    # except:
    #     print("Permission not shown of fallback ID")
        
    # EIDFallBackScreen(driver,ReportDriver)
    
    
    
        #### Upload first ID ####
        
    TestCase2 ="Uploading first ID"
    
    try:
        UploadID1Button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"neo.nbkc.smartwealth.demo:id/firstCardView")))
        ID1Uploaded=False
        UploadID1Button.click()
    except:
        ID1Uploaded=True
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase2, message=TestCase2+" is already uploaded!!", passed=True, screenshot=False)

        
        #Open Camera
        #Camera=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.ViewPager/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.ImageView")
        #Camera.click()


    if ID1Uploaded==False:

        try: WebDriverWait(driver,8).until(EC.visibility_of_element_located((By.ID,"android:id/text1")))
        except:
            driver.press_keycode(4)
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/firstCardView")
            sleep(2)
            try:driver.find_element(By.ID,"android:id/text1")
            except:
                print("Can't find the camera")
                Breakpoint()
                        
        elementList = driver.find_elements(By.ID,"android:id/text1")
        clickableElementList = driver.find_elements(By.ID,"android:id/sem_chooser_grid_item_view")

        print(len(elementList))
        print(len(clickableElementList))
        
        for i in range(0,len(elementList)):
            if elementList[i].text=="Camera":
                Camera=elementList[i]
                elementList[i].click()
                print("Camera Found and Clicked")
                break
            else:
                print( "Didn't find camera to click it")
        
        try:
            driver.find_elements(By.ID,"android:id/sem_chooser_grid_item_view")
            Camera.click()
        except:
            print ("Camera Clicked")
        
        # Samsung A52
        # Capture=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"com.sec.android.app.camera:id/normal_center_button")))
        
        Capture=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"com.android.camera2:id/shutter_button")))
        Capture.click()

        
        
        try:                
            OkButton =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "com.android.camera2:id/done_button")))
            OkButton.click()
        except:
            driver.find_element(By.ID,"com.android.camera2:id/shutter_button").click()
            OkButton =WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "com.android.camera2:id/done_button")))
            OkButton.click()
        
        try:                
            UsePhoto =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/uploadTextView")))
            UsePhoto.click()
        except:
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/uploadTextView").click()
            UsePhoto =WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/uploadTextView")))
            UsePhoto.click()
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase2, message=TestCase2+" is Successful!!", passed=True, screenshot=False)

        




    #### Upload second ID ####
        
    TestCase3 ="Uploading second ID"
        
    try:    
        UploadID2Button=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/secondCardView")))
        UploadID2Button.click()
        ID2Uploaded=False
    except:
        print("Not clickable")
        ID2Uploaded=True
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase2, message=TestCase2+" is already uploaded!!", passed=True, screenshot=False)
        SubmitButton=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton")
        SubmitButton.click()
        
        
                
        #Open Camera
        #Camera=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.ViewPager/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.ImageView")
        #Camera.click()

    if ID2Uploaded==False:    
        try: WebDriverWait(driver,8).until(EC.visibility_of_element_located((By.ID,"android:id/text1")))
        except:
            driver.press_keycode(4)
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/secondCardView")
            sleep(2)
            try:driver.find_element(By.ID,"android:id/text1")
            except:
                print("Can't find the camera")
                Breakpoint()
            

        elementList = driver.find_elements(By.ID,"android:id/text1")
        clickableElementList = driver.find_elements(By.ID,"android:id/sem_chooser_grid_item_view")

        print(len(elementList))
        print(len(clickableElementList))
        
        for i in range(0,len(elementList)):
            if elementList[i].text=="Camera":
                Camera=elementList[i]
                elementList[i].click()
                print("Camera Found and Clicked")
                break
            else:
                print( "Didn't find camera to click it")
        # Samsung A52
        # Capture=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"com.sec.android.app.camera:id/normal_center_button")))
        
        try:
            driver.find_elements(By.ID,"android:id/sem_chooser_grid_item_view")
            Camera.click()
        except:
            print ("Camera Clicked")
        
        Capture=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"com.android.camera2:id/shutter_button")))
        Capture.click()

        try:                
            OkButton =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "com.android.camera2:id/done_button")))
            OkButton.click()
        except:
            driver.find_element(By.ID,"com.android.camera2:id/shutter_button").click()
            OkButton =WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "com.android.camera2:id/done_button")))
            OkButton.click()
        
        try:                
            UsePhoto =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/uploadTextView")))
            UsePhoto.click()
        except:
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/uploadTextView").click()
            UsePhoto =WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/uploadTextView")))
            UsePhoto.click()

        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase2, message=TestCase2+" is Successful!!", passed=True, screenshot=False)
        
        
        #Submit 2 IDS and take video
        SubmitButton=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/submitButton")))
        SubmitButton.click()
    
        if ReportDriver==None: print("No Report Driver found")
        else:ReportDriver.report().step(description=TestCase3, message=TestCase3+" is Successful!!", passed=True, screenshot=False)

        
        #### Take Video ID ####
    
    TestCase4="UploadVideoID"
    Title1=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvName")))
    Description1=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvRecordingStart")
    
    # Title1Expected1="For verification purposes, we need a recording of yourself saying a statement."
    # Description1Expected="Your information will be encrypted, stored securely, and only ever used to verify your identity."
    
    # if Title1 !=Title1Expected1:
    #         Status=False
    #         ReportResults(ReportDriver, driver, Status,TestCase,Title1.text,Title1Expected1)
            
    # if Description1 != Description1Expected:
    #         Status=False
    #         ReportResults(ReportDriver, driver, Status,TestCase,Description1.text,Description1Expected)
    
    
    NextButton=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/btnNext")))
    NextButton.click()

    #Permission is asked again on EID Fallback
    # try:
    #     AllowWhileUsingTheApp=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
    #     AllowWhileUsingTheApp.click()
    # except:
    #     print("Permission not shown of fallback video")

    RecordButton=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/recordButton")))
    RecordButton.click()

    sleep(2)

    StopButton=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/actionButton")))
    StopButton.click()

    sleep(1)
    
    SubmitButton=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btnSubmit")))
    SubmitButton.click()
    sleep(1)
    try:
        NextButton=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btnPositive")))
        NextButton.click()
        flag=True
    except:
        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnSubmit").click()
        flag=False

    try:
        NextButton=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btnPositive")))
        NextButton.click()
        flag=True
    except:
        print ("Uploading ID worked")

    if ReportDriver==None:
        print("No Report Driver found")
    elif Status==True:
        ReportDriver.report().step(description=TestCase4, message=TestCase4+" is Successful!!", passed=True, screenshot=False)
        ReportDriver.report().test(name=TestCase, message=TestCase+" is Successful!!", passed=True)
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)

def UploadIDusingAPI(driver,ReportDriver,Credentials):
    
    Status=True
    TestCase ="Upload IDs and Videos using API"
    
    UploadIDAPI(ReportDriver,Credentials["Email"],Credentials["Password"])
        
    driver.press_keycode(3)
    sleep(0.5)
    driver.press_keycode(187)
    sleep(0.5)
    taponcoordinates(driver,550,850)
    
    try:
        GetStartedScreen_SignIn(driver,ReportDriver)
        SignInScreen_Test(driver,ReportDriver, Credentials["Email"],Credentials["Password"])
    except:
        try:
            WebDriverWait(driver,7).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/signedUpTv")))
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/continueButton").click()
            try:
                GetStartedScreen_SignIn(driver,ReportDriver)
                SignInScreen_Test(driver,ReportDriver, Credentials["Email"],Credentials["Password"])
            except:
                SignInScreen_Test(driver,ReportDriver, Credentials["Email"],Credentials["Password"])
        except:
            SignInScreen_Test(driver,ReportDriver, Credentials["Email"],Credentials["Password"])
    
    try:
        CheckFlow_ContinueReg_Showme(driver,ReportDriver,Credentials)
    except:
        print ("Flow Not shown")

def UploadIDusingAPI_SmokeTest(driver,ReportDriver,Credentials,Authorization="N/A"):
    
    Status=True
    TestCase ="Upload IDs and Videos using API"
    
    User_ID=UploadIDAPI(ReportDriver,Credentials["Email"],Credentials["Password"],Authorization)
        
    driver.press_keycode(3)
    sleep(1)
    driver.press_keycode(187)
    sleep(1)
    taponcoordinates(driver,550,850)
    
    # try:
    #     GetStartedScreen_SignIn(driver,ReportDriver)
    #     SignInScreen_Test(driver,ReportDriver, Credentials["Email"],Credentials["Password"])
    # except:
    #     SignInScreen_Test(driver,ReportDriver, Credentials["Email"],Credentials["Password"])
    
    try:
        CheckFlow_ContinueReg_Showme(driver,ReportDriver,Credentials)
    except:
        sleep(0.01)

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["TechnicalVariables"]["User_ID"]=User_ID
    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


    return User_ID
