from GesturesAndMotions import RefreshScreenusingswipe
from ManualReport import ReportResults
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def AddFundsScreen(driver,ReportDriver):
    Status=True
    TestCase="Add Funds Screen"
    # OnExpectedscreen = False
    # while OnExpectedscreen == False:
    #     A=driver.find_elements(By.CLASS_NAME,"android.widget.TextView")
    #     for ELEM in A:
    #         if ELEM.text=="Add Funds":
    #             # We are on Add Funds Screen.
    #             OnExpectedscreen = True
    #             break
    
    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/rvPortfolios")))

    
    while True:
        try:
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/disclosureImageView").click()
            break
        except:
            try:RefreshScreenusingswipe(driver)
            except:print("Can't Refresh Screen")
            
    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)