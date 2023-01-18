from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from CheckIfPageLoading import CheckIfPageLoading
from GesturesAndMotions import scrollDown


def PopUp(driver):
    CheckIfPageLoading(driver)
    Continue=WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/btnContinue")))
    SelectAnotherPlan=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvSelectPlan")
    Continue.click()
    

def InvestmentType(driver,ReportDriver ,User_Type="N/A"):
    
    # APIDep=True
    # while APIDep==True:
        
    #     try:
    #         A=WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/title"))).text
    #         if "api" in A or "depricated" in A:
    #             driver.press_keycode(4)
    #     except:
    #         print("API Depricated is not shown")
    #         APIDep=False
    #         break

    WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/layoutInfo")))
    Buttons=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/layoutInfo")
    
    if User_Type != "N/A":
        if User_Type.lower()=="etf" or "etf" in User_Type.lower():
            Buttons[0].click()
        elif User_Type.lower()=="islamic" or User_Type.lower()=="is":
            try:Buttons[1].click()
            except:print("Islamic is not eligible for this user")
        else:
            Buttons[0].click()

                
    else:Buttons[0].click()

    while True:
                
        try:
            Continue=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnContinue").click()
            break
        except:scrollDown(driver,500, 2200, 500, 700)

    try:PopUp(driver)
    except:
        print("Islamic pop up is not shown!!")