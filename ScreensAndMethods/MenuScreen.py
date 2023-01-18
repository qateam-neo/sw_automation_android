from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def MenuScreen(driver,ReportDriver,MethodToClick):
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/title")))
    Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/title")
    for ELEM in Titles:
        if ELEM.text==MethodToClick:
            ELEM.click()
            break
        