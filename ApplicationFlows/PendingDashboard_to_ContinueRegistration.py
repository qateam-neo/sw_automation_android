from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def PendingDashboard_to_ContinueRegistration(driver, ReportDriver):
    try:
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/bannerTitleTv")))
        ContinueRegistration = driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/bannerTitleTv")
    
        for ELEM in ContinueRegistration:
            if ELEM.text == "Continue registration":
                
                ContinueRegistrationButton =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/updateButton")
                ContinueRegistrationButton.click()
            else:
                print("Couldn't find Banner! ")
    
    except:
        ContinueRegistrationButton=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/updateButton")[0]
        ContinueRegistrationButton.click()

    return driver