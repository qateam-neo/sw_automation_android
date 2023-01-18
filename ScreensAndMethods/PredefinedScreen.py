from time import sleep

from CheckIfPageLoading import CheckIfPageLoading
from ManualReport import ReportResults
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


def PredefinedScreen(driver, ReportDriver,RiskScore):
    TestCase = "'Predefined Plans' Screen"
    Status = True
    
    CheckIfPageLoading(driver)
    WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/recyclerCardView")))
    Options=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/recyclerCardView")
    
    if (RiskScore=="3"):
        Options[0].click()        
    if (RiskScore=="5"):
        Options[1].click()
    if (RiskScore=="7"):
        Options[2].click()
    else:
        Options[1].click() #Default case
        
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/continueButton").click()

    if ReportDriver==None:
        print("No Report Driver found")
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    elif Status is True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)

    
    return driver


def PredefinedScreenTestingText_Detailed(driver, ReportDriver,RiskScore):
    TestCase = "'Predefined Plans' Screen"
    Status = True
    
    ActualText=[]
    ExpectedText=[]
    
    Text1 =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]"))).text
    ActualText.append (Text1)
    ExpectedText.append("What level of risk do you feel comfortable with?")
    if (( ExpectedText[0] !=ActualText[0])):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,ActualText[0],  ExpectedText[0])

    ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/android.view.ViewGroup/android.widget.TextView[1]").text)
    ExpectedText.append("Conservativ")
    if ((ActualText[1]  != ExpectedText[1])):
        Status = False        
        ReportResults(ReportDriver, driver, Status,TestCase,ActualText[1],  ExpectedText[1])

    ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/android.view.ViewGroup/android.widget.TextView[2]").text)
    ExpectedText.append("This means your asset mix will have greater exposure to more stable and income focused instruments while your returns will be just above inflation.")
    if ((ActualText[2]  != ExpectedText[2])):
        Status = False
        ReportResults(ReportDriver, driver, Status,TestCase,ActualText[2],  ExpectedText[2])

    ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[2]/android.view.ViewGroup/android.widget.TextView[1]").text)
    ExpectedText.append("Balance")
    if ((ActualText[3]  != ExpectedText[3])):
        Status = False
        ReportResults(ReportDriver, driver, Status,TestCase,ActualText[3],  ExpectedText[3])

    ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[2]/android.view.ViewGroup/android.widget.TextView[2]").text)
    ExpectedText.append("This means your asset mix will focus on income and growth instruments to achieve greater returns. You can expect to see some downturns to achieve such returns.")
    if ((ActualText[4]  != ExpectedText[4])):
        Status = False
        ReportResults(ReportDriver, driver, Status,TestCase,ActualText[4],  ExpectedText[4])


    ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[3]/android.view.ViewGroup/android.widget.TextView[1]").text)
    ExpectedText.append("Growt")
    if ((ActualText[5]  != ExpectedText[5])):
        Status = False
        ReportResults(ReportDriver, driver, Status,TestCase,ActualText[5],  ExpectedText[5])

    ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[3]/android.view.ViewGroup/android.widget.TextView[2]").text)
    ExpectedText.append("This means your asset mix will focus on growth instruments to achieve the highest returns. We recommend a long-term investment horizon as markets run through their cycles.")
    if ((ActualText[6]  != ExpectedText[6])):#Can't find_element_by_xpath
        Status = False
        ReportResults(ReportDriver, driver, Status,TestCase,ActualText[6],  ExpectedText[6])

    ActualText.append(driver.find_element(By.XPATH,"//*[@text='Not sure? Help me decide']").text)
    ExpectedText.append( "Not sure? Help me decide")
    if ((ActualText[7]  != ExpectedText[7])):
        Status = False
        ReportResults(ReportDriver, driver, Status,TestCase,ActualText[7],  ExpectedText[7])

    if ReportDriver==None:
        print("No Report Driver found")
    elif Status is True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
                
    if (RiskScore=="3"):
        driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]").click()
        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/continueButton").click()
        
    if (RiskScore=="5"):
        driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[2]").click()
        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/continueButton").click()

    if (RiskScore=="7"):
        driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[3]").click()
        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/continueButton").click()

    return driver