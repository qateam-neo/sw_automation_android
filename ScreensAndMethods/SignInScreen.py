from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ManualReport import ReportResults
from selenium.webdriver.common.action_chains import ActionChains


def SignInScreen_Test(driver,ReportDriver, Email, Password):

    TestCase = "Sign In Flow"
    Status = True
    
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/inputEt")))
    inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/inputEt")
        
    if inputs[0].text != Email:   
        inputs[0].click()
        inputs[0].clear()
        action = ActionChains(driver)
        action.send_keys(Email).perform()
        if driver.is_keyboard_shown():
            driver.press_keycode(4) 
        sleep(2)
        
    inputs=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/inputEt")
    if inputs[1].text=="•••••••••••":
        print("We Can skip password")
        # print(driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/inputEt").text)
    else:
        inputs[1].click()
        
        action = ActionChains(driver)
        action.send_keys("Password123").perform()
        if driver.is_keyboard_shown():
            driver.press_keycode(4) 


    sleep(1)
    
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/chk_rememberme").click()
    try:
        SignIn_Button =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/loginButton")
        SignIn_Button.click()
    except:
        driver.press_keycode(4)
        sleep(1)
        SignIn_Button =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/loginButton")
        SignIn_Button.click()
    
    try:driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/intercom_close").click()
    except: sleep(0.01)
    sleep(4)
    ReportResults(ReportDriver,driver,Status,TestCase,"N/A",  "N/A")



