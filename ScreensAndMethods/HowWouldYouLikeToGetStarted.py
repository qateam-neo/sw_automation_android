from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CheckIfPageLoading import CheckIfPageLoading
from ManualReport import ReportResults
import pytest


def HowWouldYouLikeToGetStartedText(driver,ReportDriver,Flow):
    TestCase ="'How Would You Like To Get Started' Screen"
    Status =True
    # ActualText = []
    # ExpectedText = []
    CheckIfPageLoading(driver)

    XX = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]")))
    # ActualText.append(XX.text)
    
    # ExpectedText.append("How would you like to get started?")
    # if (( ExpectedText[0] != ActualText[0])):
    #     Status=False
    #     ReportResults(ReportDriver,driver,Status,TestCase,ActualText[0],ExpectedText[0])
    Option=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/recyclerCardView")
    if Flow=="Predefined" or Flow== "predefined" :
        Option[1].click()
    elif Flow=="Customized" or Flow=="customized" :
        Option[0].click()
    driver.find_element(By.XPATH,"//*[@text='Continue']").click()

    # ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]").text)
    # ExpectedText.append("Start your SmartWealth account opening by selecting one of the options below")
    # if (( ExpectedText[1] != ActualText[1])):
    #     Status=False
    #     ReportResults(ReportDriver,driver,Status,TestCase,ActualText[1],ExpectedText[1])


    # ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/android.view.ViewGroup/android.widget.TextView[1]").text)
    # ExpectedText.append( "Build an investment plan customized to you")
    # if (( ExpectedText[2] != ActualText[2])):
    #     Status=False
    #     ReportResults(ReportDriver,driver,Status,TestCase,ActualText[2],ExpectedText[2])

    # ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/android.view.ViewGroup/android.widget.TextView[2]").text)
    # ExpectedText.append( "Answer 10 questions that will help us learn more about who you are. Based on that, we will build you a personalized investment plan.")
    # if (( ExpectedText[3] != ActualText[3])):
    #     Status=False
    #     ReportResults(ReportDriver,driver,Status,TestCase,ActualText[3],ExpectedText[3])

    # ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[2]/android.view.ViewGroup/android.widget.TextView[1]").text)
    # ExpectedText.append("Select a ready-built investment plan")
    # if (( ExpectedText[4] != ActualText[4])):
    #     Status=False
    #     ReportResults(ReportDriver,driver,Status,TestCase,ActualText[4],ExpectedText[4])

    # ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[2]/android.view.ViewGroup/android.widget.TextView[2]").text)
    # ExpectedText.append("Choose an investment plan in line with your risk tolerance preferences: Conservative, Balanced, Growth.")
    # if (( ExpectedText[5] != ActualText[5])):
    #     Status=False
    #     ReportResults(ReportDriver,driver,Status,TestCase,ActualText[5],ExpectedText[5])


    if ReportDriver==None:
        print("No Report Driver found")
        ReportResults(ReportDriver, driver, True,TestCase,"N/A",  "N/A")

    elif Status == True:
        ReportResults(ReportDriver,driver,Status,TestCase,"N/A","N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
        


def HowWouldYouLikeToGetStartedText_Detailed(driver,ReportDriver):
    TestCase ="'How Would You Like To Get Started' Screen"
    Status =True
    ActualText = []
    ExpectedText = []
    
    XX = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]")))
    ActualText.append(XX.text)
    
    ExpectedText.append("How would you like to get started?")
    if (( ExpectedText[0] != ActualText[0])):
        Status=False
        ReportResults(ReportDriver,driver,Status,TestCase,ActualText[0],ExpectedText[0])


    ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]").text)
    ExpectedText.append("Start your SmartWealth account opening by selecting one of the options below")
    if (( ExpectedText[1] != ActualText[1])):
        Status=False
        ReportResults(ReportDriver,driver,Status,TestCase,ActualText[1],ExpectedText[1])


    ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/android.view.ViewGroup/android.widget.TextView[1]").text)
    ExpectedText.append( "Build an investment plan customized to you")
    if (( ExpectedText[2] != ActualText[2])):
        Status=False
        ReportResults(ReportDriver,driver,Status,TestCase,ActualText[2],ExpectedText[2])

    ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/android.view.ViewGroup/android.widget.TextView[2]").text)
    ExpectedText.append( "Answer 10 questions that will help us learn more about who you are. Based on that, we will build you a personalized investment plan.")
    if (( ExpectedText[3] != ActualText[3])):
        Status=False
        ReportResults(ReportDriver,driver,Status,TestCase,ActualText[3],ExpectedText[3])

    ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[2]/android.view.ViewGroup/android.widget.TextView[1]").text)
    ExpectedText.append("Select a ready-built investment plan")
    if (( ExpectedText[4] != ActualText[4])):
        Status=False
        ReportResults(ReportDriver,driver,Status,TestCase,ActualText[4],ExpectedText[4])

    ActualText.append(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[2]/android.view.ViewGroup/android.widget.TextView[2]").text)
    ExpectedText.append("Choose an investment plan in line with your risk tolerance preferences: Conservative, Balanced, Growth.")
    if (( ExpectedText[5] != ActualText[5])):
        Status=False
        ReportResults(ReportDriver,driver,Status,TestCase,ActualText[5],ExpectedText[5])


    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver,driver,Status,TestCase,"N/A","N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
        
    
    driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[2]").click()
    driver.find_element(By.XPATH,"//*[@text='Continue']").click()
    sleep(3)
    
    return driver





