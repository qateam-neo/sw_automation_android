from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ManualReport import ReportResults, ReportResultsScreenNotShown


def ConfirmMobileScreen_Test(driver, ReportDriver, MobileNumber):
    
    TestCase ="Confirm Mobile Number Screen"
    Status =True
    
    #Check if we are on fingerprint screen or another screen
    try:
        ConfirmMobileNumber = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvNumber")))
        ConfirmMobileNumberText=ConfirmMobileNumber.text
        
        if ("59" == ConfirmMobileNumberText[0:2]):
            # print(ConfirmMobileNumberText[0:2])
            Verify_mobile_screen_is_shown=True

    except:
        Verify_mobile_screen_is_shown=False
        


    if Verify_mobile_screen_is_shown == True:

        if ReportDriver==None:
            print("No Report Driver found")
        elif Status == True:
            ReportResults(ReportDriver,driver,Status,TestCase,"N/A",  "N/A")
        else:
            ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)

        driver.press_keycode(4)

    else:
        ReportResultsScreenNotShown(ReportDriver,TestCase)


    return driver



def ConfirmMobileScreen_Test_Detailed(driver, ReportDriver, MobileNumber):
    
    TestCase ="Confirm Mobile Number Screen"
    Status =True
    
    #Check if we are on fingerprint screen or another screen
    try:
        ConfirmMobileNumber = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvNumber")))
        ConfirmMobileNumberText=ConfirmMobileNumber.text
        
        if ("59" == ConfirmMobileNumberText[0:2]):
            # print(ConfirmMobileNumberText[0:2])
            Verify_mobile_screen_is_shown=True

    except:
        Verify_mobile_screen_is_shown=False
        


    if Verify_mobile_screen_is_shown == True:

        Text1 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]").text
        Text1Expected = "Confirm your mobile number"

        if (( Text1Expected != Text1)):
            Status=False
            ReportResults(ReportDriver,driver,Status,TestCase, Text1,Text1Expected)
            
        Text2 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]").text
        Text2Expected ="Hello! We need you to confirm that this is still your mobile number:"
        if (( Text2Expected != Text2)):
            Status=False
            ReportResults(ReportDriver,driver,Status,TestCase,Text2,Text2Expected)

        Text3 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[3]").text
        Text3Expected = "+965"
        if (( Text3Expected != Text3)):
            Status=False
            ReportResults(ReportDriver,driver,Status,TestCase,Text3,Text3Expected)


        Text4 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[4]").text
        Text4Expected = MobileNumber
        if (( Text4Expected != Text4)):
            Status=False
            ReportResults(ReportDriver,driver,Status,TestCase,Text4,Text4Expected)

        Text5 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[5]").text
        Text5Expected = "In case this phone number is not yours or invalid, please contact support."

        if (( Text5Expected != Text5)):
            Status=False
            ReportResults(ReportDriver,driver,Status,TestCase,Text5,Text5Expected)


        Text6 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button").text
        Text6Expected = "Yes, this is my number"
        if (( Text6Expected != Text6)):
            Status=False
            ReportResults(ReportDriver,driver,Status,TestCase,Text6,Text6Expected)

        if ReportDriver==None:
            print("No Report Driver found")
        elif Status == True:
            ReportResults(ReportDriver,driver,Status,TestCase,"N/A",  "N/A")
        else:
            ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)

        driver.press_keycode(4)

    else:
        ReportResultsScreenNotShown(ReportDriver,TestCase)


    return driver

