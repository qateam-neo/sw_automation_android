from ManualReport import ReportResults
from selenium.webdriver.support.ui import WebDriverWait # needs to be used when creating a function everytime
from selenium.webdriver.support import expected_conditions # needs to be used when creating a function everytime
from selenium.webdriver.common.by import By


def Showmetheappflow_ThankYouScreen(driver,ReportDriver):
    TestCase ="(Show me the app) Thank You Screen"
    Status =True

    ShowmetheappButton =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/showAppButton")
    ShowmetheappButton.click()

    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver,driver,Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)



    return driver



def Showmetheappflow_ThankYouScreen_Detailed(driver,ReportDriver):
    TestCase ="(Show me the app) Thank You Screen"
    Status =True

    Text1 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]").text
    Text1Expected = "Thank you!"

    if (( Text1Expected != Text1)):
        Status=False
        ReportResults(ReportDriver,driver,Status,TestCase, Text1,Text1Expected)
    #Total Percentage
    Text2 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]").text
    Text2Expected ="You are now signed up"
    if (( Text2Expected != Text2)):
        Status=False
        ReportResults(ReportDriver,driver,Status,TestCase,Text2,Text2Expected)
     

    #First Bond
    Text3 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[3]").text
    Text3Expected = "Get a glimpse of your new investment companion that will guide you to reach your life goals."
    if (( Text3Expected != Text3)):
        Status=False
        ReportResults(ReportDriver,driver,Status,TestCase,Text3,Text3Expected)

    ShowmetheappButton =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button")
    Text5 =ShowmetheappButton.text
    Text5Expected1 = "Continue Registrationssss"
    Text5Expected2 = "Show me the app"

    if (( Text5Expected1 != Text5)) and (( Text5Expected2 != Text5)):
        TextExpected ="Continue Registration or Show me the app"
        Status=False
        ReportResults(ReportDriver,driver,Status,TestCase,Text5,TextExpected)
    ShowmetheappButton.click()

    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver,driver,Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)



    return driver

