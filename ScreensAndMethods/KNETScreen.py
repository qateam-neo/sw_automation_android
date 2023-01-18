from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import appium
from ConfirmMobileScreen import ConfirmMobileScreen_Test

from ManualReport import ReportResults
def KNETScreen(driver,ReportDriver):
    TestCase ="KNET Screen"
    Status = True
    try:
        WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.view.View")))
        SelectBank=driver.find_elements(By.CLASS_NAME,"android.view.View")
        for ELEM in SelectBank:
            # print(ELEM.text)
            if ELEM.text == "Select Your Bank":
                ELEM.click()
                break
        # sleep(0.4)
            
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"android:id/text1")))
        KNETTestCard=driver.find_elements(By.ID,"android:id/text1")
        for ELEM in KNETTestCard:
            if ELEM.text == "Knet Test Card [KNET1]":
                ELEM.click()
                break
        
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.view.View")))
        SelectBank=driver.find_elements(By.CLASS_NAME,"android.view.View")
        for ELEM in SelectBank:
            if ELEM.text == "MM":
                ELEM.click()  
                break
                
        # sleep(0.4)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"android:id/text1")))
        KNETTestCard=driver.find_elements(By.ID,"android:id/text1")
        for ELEM in KNETTestCard:
            if ELEM.text == "09":
                ELEM.click()  
                break    
                
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.view.View")))
        SelectBank=driver.find_elements(By.CLASS_NAME,"android.view.View")
        for ELEM in SelectBank:
            if ELEM.text == "YYYY":
                ELEM.click()  
                break
                
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"android:id/text1")))
        KNETTestCard=driver.find_elements(By.ID,"android:id/text1")
        for ELEM in KNETTestCard:
            if ELEM.text == "2025":
                ELEM.click()  
                break      
                    
        
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.widget.EditText"))).click()
        InputFields=driver.find_elements(By.CLASS_NAME,"android.widget.EditText")
        InputFields[0].send_keys("0000000001")
        InputFields[1].send_keys("1234")
        driver.press_keycode(4)

        AA=driver.find_elements(By.CLASS_NAME,"android.widget.Button")
        for ELEM in AA:
            if ELEM.text == "Submit":
                ELEM.click()
                break            
        
        sleep(3)
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"neo.nbkc.smartwealth.demo:id/btnBack")))
            return False
        except:
            sleep(0.1)
        

        ConfirmShown=False
        while ConfirmShown==False:
            SubmitShown=False
            try: 
                AA=driver.find_elements(By.CLASS_NAME,"android.widget.Button")
                for ELEM in AA:
                    if ELEM.text == "Submit":
                        ELEM.click()
                        SubmitShown=True
                if SubmitShown==False: raise ValueError("Submit is already clicked")
            except:
                AA=driver.find_elements(By.CLASS_NAME,"android.widget.Button")
                for ELEM in AA:
                    if ELEM.text == "Confirm":
                        ELEM.click()
                        ConfirmShown=True
                        break    
            
            try:
                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnBack")
            except:
                sleep(0.1)
            else:
                raise ValueError("KNET is not available")
            try:WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/btnDone"))).click()
            except:driver.press_keycode(4)

        
        if ReportDriver==None:
            print("No Report Driver found")
        elif Status:
            ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
        else:
            ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
        
        return True
    except:
        retry=True
        return False