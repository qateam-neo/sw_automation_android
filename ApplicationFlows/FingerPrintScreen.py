from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ManualReport import ReportResults, ReportResultsScreenNotShown


def FingerPrintScreen_Test(driver, ReportDriver):

    TestCase ="FingerPrint Screen"
    Status =True

    #Check if we are on fingerprint screen or another
    try:
        #TODO: FIXME: Fix the xpath since the new emulator device has a new xpath for te element 
        FingerPrintScreen = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]")))
        FingerPrintScreenText=FingerPrintScreen.text
        
        if ("Fingerprint Login" == FingerPrintScreenText):
            # print(FingerPrintScreenText)
            Fingerprint_screen_is_shown=True

    except:
        # print("Fingrprint screen is not shown")
        Fingerprint_screen_is_shown=False
        


    if Fingerprint_screen_is_shown == True:


        FingerPrintScreen = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]")))

        CancelButton =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView")
        CancelButton.click()

        if ReportDriver==None:
            print("No Report Driver found")
        elif Status == True:
            ReportResults(ReportDriver,driver,Status,TestCase,"N/A",  "N/A")
        else:
            ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
            
    else:
        ReportResultsScreenNotShown(ReportDriver,TestCase)

    return driver



def FingerPrintScreen_Test_Detailed(driver, ReportDriver):
    
    TestCase ="FingerPrint Screen"
    Status =True

    #Check if we are on fingerprint screen or another
    try:
        FingerPrintScreen = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]")))
        FingerPrintScreenText=FingerPrintScreen.text
        
        if ("Fingerprint Login" == FingerPrintScreenText):
            # print(FingerPrintScreenText)
            Fingerprint_screen_is_shown=True

    except:
        # print("Fingrprint screen is not shown")
        Fingerprint_screen_is_shown=False
        


    if Fingerprint_screen_is_shown == True:


        #Text1 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]").text
        #Text1Expected = "Fingerprint Login"

        #if (( Text1Expected != Text1)):
         #   Status=False
         #   ReportResults(ReportDriver,driver,Status,TestCase, Text1,Text1Expected)

        Text2 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]").text
        Text2Expected ="Fingerprint login allows you to use your biometrics instead of entering your SmartWealth User ID and Password to log in to your NBK Capital SmartWealth online account.\n" + "\n" + "In order to use Fingerprint, you need to enable it on your device through your Android Settings under the \"Security\" section.\n" + "\n" + "By enabling Fingerprint login, you are allowing anyone who has a fingerprint stored on this device to access your account. Please review the biometrics stored on your device and make sure all should authorized to access the account information through SmartWealth.\n" + "\n" + "NBK Capital SmartWealth does not have access to your Fingerprint data.\n" + "\n" + "For information on how Google uses and stores your Fingerprint and Keychain data, please see Google's Privacy Policy and Android Security Guides."

        if (( Text2Expected != Text2)):
            Status=False
            ReportResults(ReportDriver,driver,Status,TestCase,Text2,Text2Expected)


        Text3 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button").text
        Text3Expected = "Enable Fingerprint"
        if (( Text3Expected != Text3)):
            ReportResults(ReportDriver,driver,Status,TestCase,Text3,Text3Expected)
            Status=False

        CancelButton =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView")
        Text5 =CancelButton.text
        Text5Expected = "CANCEL"

        if Text5Expected != Text5:
            Status=False
            ReportResults(ReportDriver,driver,Status,TestCase,Text5,Text5Expected)

        if ReportDriver==None:
            print("No Report Driver found")
        elif Status == True:
            ReportResults(ReportDriver,driver,Status,TestCase,"N/A",  "N/A")
        else:
            ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)

        CancelButton.click()


    else:
        ReportResultsScreenNotShown(ReportDriver,TestCase)




    return driver

