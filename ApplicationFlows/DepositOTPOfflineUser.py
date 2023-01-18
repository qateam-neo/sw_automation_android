from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from GesturesAndMotions import closeapp, scrollDown, taponcoordinates
from colorama import Fore

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
