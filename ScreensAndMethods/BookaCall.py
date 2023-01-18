from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CheckFeatureFlags import FeatureFlag
from CheckIfPageLoading import CheckIfPageLoading

from ManualReport import ReportResults


def BookaCall(driver,ReportDriver,BookaCall=False,NotInterested=False):
    #Feature can be either onboarding or withdrawal

    CheckIfPageLoading(driver)
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btn_book")))
        FeatureAvailable=True
    except:FeatureAvailable=FeatureFlag(driver,"onboarding callback")
    if FeatureAvailable:
        Book=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btn_book")
        NotInterestedButton=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btn_not_interested")
        
        if BookaCall==True:
            Book.click()
            sleep(2)
        else:
            NotInterestedButton.click()
            
            
        try:
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btn_not_interested").click()
            sleep(2)
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btn_not_interested").click()
        except:
            sleep(0.5)
        ReportResults(ReportDriver, driver, True,"Book a Call Screen","N/A",  "N/A")
    
        
def BookaCall_Withdrawal(driver,ReportDriver,BookaCall=False,ContinueWithdrawal=False):
    try:
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/btn_book")))
        FeatureAvailable=True
    except:FeatureAvailable=FeatureFlag(driver,"withdrawal callback")
    if FeatureAvailable: 

        Book=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btn_book")
        ContinueButton=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btn_continue")
        
        if BookaCall==True:
            Book.click()
        else:
            ContinueButton.click()
        sleep(2)

        
        
        try:
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btn_continue").click()
            sleep(2)
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btn_continue").click()
        except:
            sleep(0.5)
        ReportResults(ReportDriver, driver, True,"Book a Call Withdrawal Screen","N/A",  "N/A")
