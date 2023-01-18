from ast import Not
from time import sleep
from colorama import Fore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CheckIfPageLoading import CheckIfPageLoading

from GesturesAndMotions import closeapp, scrollDown, taponcoordinates
from ManualReport import ReportResults
from WithdrawalOTP_API import WithdrawalOTP_API

def WithdrawalOTPScreen(driver,ReportDriver):
    
    Status=True
    TestCase="OTP Screen"
    
    flag=True
    driver.open_notifications()
    while flag==True:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "android:id/text")))
        Notifications=driver.find_elements(By.ID,"android:id/text")
        for ELEM in Notifications:
            if "GET" in ELEM.text or "POST" in ELEM.text or "PUT" in ELEM.text:
                ELEM.click()
                flag=False
                break
        
        if flag==True:
            scrollDown(driver,500, 2400, 500, 1650)
        
    
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/path")))
    Logs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/path")
    for ELEM in Logs:
        if "withdraw" in ELEM.text:
            ELEM.click()
            break
    
    sleep(1)
    taponcoordinates(driver,1300,400)
    sleep(0.5)

    ResponseShown=False
    while ResponseShown==False:
        Elements=driver.find_elements(By.CLASS_NAME,"android.widget.TextView")
        for ELEM in Elements:
            if ELEM.text=="RESPONSE":
                ELEM.click()
                print("Response button is shown")
                ResponseShown = True
                sleep(0.5)
                break
            
            
    scrollDown(driver,500, 1500, 500, 700)
    scrollDown(driver,500, 1500, 500, 700)

    X=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/bodyLine")
    for ELEM in X:
        if "otp_code" in ELEM.text:      
            OTP=X[4].text
            # print(OTP)
            OTPCode =OTP[17:23]
            print(Fore.GREEN+"The OTP Code for this withdarawal is: "+OTPCode+Fore.RESET)
            break


    
    driver.press_keycode(187)
    sleep(0.5)
    closeapp(driver,1020, 1500, 1020, 500)
    taponcoordinates(driver,550,850)
    
    while True:
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/codeEditText")))
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/codeEditText").send_keys(OTPCode)
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton").click()
            break
        except:
            try:
                WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/bodyLine")))
                driver.press_keycode(187)
                sleep(0.5)
                closeapp(driver,1020, 1500, 1020, 400)
                taponcoordinates(driver,550,850)
            except:
                WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "android:id/text")))
                driver.press_keycode(4)

            
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
    
def WithdrawalOTPScreen_API(driver,ReportDriver,User_ID):

    Status=True
    TestCase="OTP Screen"
    sleep(4)
    WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/otp_view")))
    OTPCode=WithdrawalOTP_API(User_ID)
    sleep(3)
    CheckIfPageLoading(driver)
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/otp_view")))
    otpbox=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/et_input")
    otpbox=otpbox[0]
    otpbox.send_keys(OTPCode)
    # driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnSubmit").click()


    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
    
    
def DepositOTPOfflineUser(driver,ReportDriver):
    WebDriverWait(driver,6).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/codeEditText")))
    flag=True
    driver.open_notifications()
    while flag==True:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "android:id/text")))
        Notifications=driver.find_elements(By.ID,"android:id/text")
        for ELEM in Notifications:
            if "GET" in ELEM.text or "POST" in ELEM.text or "PUT" in ELEM.text:
                ELEM.click()
                flag=False
                break
        
        if flag==True:
            scrollDown(driver,500, 2400, 500, 1650)
        
    
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/path")))
    Logs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/path")
    for ELEM in Logs:
        if "deposit" in ELEM.text:
            ELEM.click()
            break
    
    sleep(1)
    taponcoordinates(driver,1300,400)
    sleep(0.5)

    ResponseShown=False
    while ResponseShown==False:
        Elements=driver.find_elements(By.CLASS_NAME,"android.widget.TextView")
        for ELEM in Elements:
            if ELEM.text=="RESPONSE":
                ELEM.click()
                print("Response button is shown")
                ResponseShown = True
                sleep(0.5)
                break
            
            
    scrollDown(driver,500, 1500, 500, 700)
    scrollDown(driver,500, 1500, 500, 700)

    X=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/bodyLine")
    for ELEM in X:
        if "otp_code" in ELEM.text:      
            OTP=ELEM.text
            # print(OTP)
            OTPCode =OTP[17:23]
            print(Fore.GREEN+"The OTP Code for this withdarawal is: "+OTPCode+Fore.RESET)
            break


    
    driver.press_keycode(187)
    sleep(0.5)
    speed=400
    closeapp(driver,1020, 1600, 1020, 500,speed)
    while True:
        try:
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/bodyLine")
            speed=speed+100
            closeapp(driver,1020, 1600, 1020, 500,speed)
        except:
            try:
                if len(driver.find_elements(By.ID,"com.google.android.apps.nexuslauncher:id/snapshot"))==0:
                    breakpoint
                elif len(driver.find_elements(By.ID,"com.google.android.apps.nexuslauncher:id/snapshot"))==1:
                    print("Back on OTP Screen")
                    break
                elif len(driver.find_elements(By.ID,"com.google.android.apps.nexuslauncher:id/snapshot"))>1:
                    print("API Logger still open")
            
            except:
                print("We are not in multiple application view")
        
    try: driver.find_element(By.ID,"com.google.android.apps.nexuslauncher:id/snapshot").click()
    except:taponcoordinates(driver,550,850)
    
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/codeEditText")))
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/codeEditText").send_keys(OTPCode)
    sleep(1.3)
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/submitButton").click()
