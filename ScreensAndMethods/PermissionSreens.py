from time import sleep
from ManualReport import ReportResults
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def PermissionScreensText(driver,ReportDriver):
    
    Status=True
    TestCase="Permission Screens"
    
    Title =WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tv_title")))
    Info=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tv_info")
    Camera=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tv_camera")
    Microphone=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tv_microphone")
    Button=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btn")
    
    if Title.text != "Prepare your documents":
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Title.text ,"Prepare your documents")
                
    infotextExpected="Smartwealth will scan your Civil ID to verify your identity in the next steps. Please allow camera and microphone access to continue. learn more"  
    if Info.text != infotextExpected:
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Info.text,infotextExpected)


    if Camera.text !="Enable Camera":
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Camera.text ,"Enable Camera")
        

    if Microphone.text != "Enable Microphone":
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Microphone.text,"Enable Microphone")
        
            
    if Button.text != "Allow access" and Button.text != "Open Settings":
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Button.text,"Open Settings or Allow access")
        
    elif Button.text == "Open Settings":
        OpenSettings=True
        
    else: 
        OpenSettings=False
        
        
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status== True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
        
        ##### TEXT IN SCREEN IS TESTED Above / Now allowing access #####
        
    
    
    if OpenSettings==False:
        
        Button.click()
        sleep(2)
        AllowWhileUsingTheApp=driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        AllowWhileUsingTheApp.click()
        sleep(2)
        AllowWhileUsingTheApp=driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        AllowWhileUsingTheApp.click()
        sleep(1)
        Button=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btn")
        Button.click()
        
    if OpenSettings==True:
        print("Open Settings flow")