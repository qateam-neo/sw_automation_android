from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ManualReport import ReportResults



def EnterDepositAmountScreen(driver,ReportDriver):
    Status=True
    TestCase="Enter Deposit Amount"
    WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/lblEnterAmount")))
    AmountOption1=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvOption1").click()
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnSubmit").click()
    sleep(1)
    SamePage=True
    while SamePage==True:
        try:
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnBack")
            raise ValueError("KNET is not available")
        except:
            sleep(0.1)
            
        try:
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvOption1").click()
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnSubmit").click()
            SamePage=True
        except:
            try:
                aa=driver.find_elements(By.CLASS_NAME,"android.webkit.WebView")
                for a in aa:
                    if a.text=="KNET Payments":
                        SamePage=False
                        break
                if SamePage:raise ValueError('A very specific bad thing happened.')

                
            except:
                try:
                    if driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle").text =="Transfer Instructions":
                        SamePage=False
                        break
                    if SamePage:raise ValueError('A very specific bad thing happened.')
                except:
                    try:
                        if driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/titleTextView").text =="Verification Needed":
                            SamePage=False
                            break
                        if SamePage:raise ValueError('A very specific bad thing happened.')
                    except:
                        try:
                            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/transferDetailsRecycler")
                            SamePage=False
                            break
                        except:
                            try:
                                A=WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/title"))).text
                                if "api" in A or "depricated" in A:
                                    driver.press_keycode(4)
                            except:
                                print("Can't find Transfer instructions and amount button or KNET")
    
    
    
    
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)