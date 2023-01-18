from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def CheckIfPageLoading(driver):
    
    try:
        driver.find_element(By.ID, "neo.nbkc.smartwealth.demo:id/animationView")
        Loading=True
    except: 
        try:
            driver.find_element(By.ID, "neo.nbkc.smartwealth.demo:id/animationView")
            Loading=True
        except:
            Loading=False
            return False  
    
    while Loading:
        try:
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/animationView")
            sleep(0.1)
        except:
            Loading=False
            break