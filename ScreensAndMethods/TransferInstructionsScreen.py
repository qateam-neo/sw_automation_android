from bdb import Breakpoint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from GesturesAndMotions import scrollDown

from ManualReport import ReportResults



def TransferInstructionsScreen(driver,ReportDriver):
    Status=True
    TestCase="Transfer Instructions Screen"
    
    try:
        A=WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/title"))).text
        if "api" in A or "depricated" in A:
            driver.press_keycode(4)
    except:
        print("API Depricated is not shown")
        APIDep=False
         
           
    # try:
    #     WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/headerTextView")))  
    #     scrollDown(driver,500, 2650, 500, 340)
    # except:
    #     try:
    #         scrollDown(driver,500, 2650, 500, 340)
    #     except:
    #        driver.press_keycode(4)
    try:
        TitleText=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle"))).text
        if "transfer" in TitleText.lower() or "instructions" in TitleText.lower():
            while True:
                try:
                    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnSubmit").click()
                    break
                except:
                    try:
                        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/doneButton").click()
                        break
                    except:
                        try:
                            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnDone").click()
                            break
                        except:
                            try:
                                # scrollDown(driver,500, 2650, 500, 340)
                                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/navigation_home").click()
                                break
                            except:
                                try:
                                    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/imgIcon")
                                    break
                                except:
                                    driver.press_keycode(4)
    except:
        print("Transfer instruction screen is not shown!!")
        Breakpoint



    
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)