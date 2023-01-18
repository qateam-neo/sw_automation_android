import random
import string
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from GesturesAndMotions import taponcoordinates
from selenium.webdriver.common.action_chains import ActionChains

from ManualReport import ReportResults

def PersonalisePortfolio(driver,ReportDriver):
    TestCase ="Personalise Portfolio"
    Status = True
    
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/etText")))
    A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/etText")
    a=[]
    for i in range(0,5):
        a.append(random.choice(string.ascii_letters))
    A.send_keys(a)
    
    taponcoordinates(driver,500,2750)

    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/etAmount")))
    X=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/etAmount")
    X.click()
    action = ActionChains(driver)
    action.send_keys_to_element(X,5000).perform()
    taponcoordinates(driver,1200,2750)
    X=0
    
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/seekBar")))
    A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/seekBar")
    action = ActionChains(driver)
    action.click(A).perform()
    A=0
    
    # taponcoordinates(driver,1200,2750)
    X=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etAmount")
    for x in X:
        if x=="$0.00":
            x.click()
            action = ActionChains(driver)
            action.send_keys_to_element(x,5000).perform()
            taponcoordinates(driver,1200,2750)
        # driver.press_keycode(66)
    # X=0
    # taponcoordinates(driver,300,1000)

    # sleep(2)
    # taponcoordinates(driver,500,1300)
    # action = ActionChains(driver)
    # action.send_keys_to(5000).perform()
    # taponcoordinates(driver,1200,2750)

    # taponcoordinates(driver,500,2350)
    # sleep(0.5)
    
    
    # (driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/etAmount"))[1].send_keys("5000")
    
    # taponcoordinates(driver,500,2350)
    # action = ActionChains(driver)
    # action.send_keys(5000).perform()
    taponcoordinates(driver,1200,2750)
    # taponcoordinates(driver,300,1000)
    try:
        WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/button"))).click()
    except:
        try:
            taponcoordinates(driver,500,2350)
            sleep(0.5)
            WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/button"))).click()
        except:
            driver.press_keycode(4)
            WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/button"))).click()


        
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
    
    
    

