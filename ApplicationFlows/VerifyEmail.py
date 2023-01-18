from time import sleep
from CheckIfPageLoading import CheckIfPageLoading
from GesturesAndMotions import RefreshScreenusingswipe, closeapp, scrollDown, taponcoordinates
from GetStartedScreen import GetStartedScreen_SignIn
from ManualReport import ReportResults
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from SignInScreen import SignInScreen_Test

from VerifyEmailAPI import VerifyEmailAPI

def VerifyEmailFlow(driver, ReportDriver, Email, Password):
    
    #####################################################################
    ######################## Verify Email Screen ########################
    
    TestCase1 ="Verify Email screen"
    Status =True

    try: 
        Text7 =WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/btnOpenEmailApp")))
    except:
        print("Email is already verified ")
        return True
        
        
    # Text1 =WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvHeader"))).text
    # Text1Expected ="Verify your email"
    # if (( Text1Expected != Text1)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase1,Text1,Text1Expected)

    # Text2 =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvCheckYourInbox").text
    # Text2Expected ="Check your inbox"
    # if (( Text2Expected != Text2)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase1,Text2,Text2Expected)


    # Text3 =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvSentConfirmation").text
    # Text3Expected = "We have sent you a confirmation email to"
    # if (( Text3Expected != Text3)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase1,Text3,Text3Expected)

    # Text5 =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvEmail").text
    # Text5Expected = Email
    # if (( Text5Expected != Text5)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase1,Text5,Text5Expected)

    # Text6 =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvDescription").text
    # Text6Expected = "Please check your inbox and verify your email address."
    # if (( Text6Expected != Text6)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase1,Text6,Text6Expected)

    # Text7 =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnOpenEmailApp").text
    # Text7Expected = "Open email app"
    # if (( Text7Expected != Text7)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase1,Text7,Text7Expected)

    # Text8 =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnResendEmail").text
    # Text8Expected = "Resend Verification Email"
    # if (( Text8Expected != Text8)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase1,Text8,Text8Expected)

    # Text9 =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvChangeEmail").text
    # Text9Expected = "Change Email"
    # if (( Text9Expected != Text9)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase1,Text9,Text9Expected)

    # #Verify Email Screen Success

    if Status == True:
        ReportResults(ReportDriver, driver, "StepTrue",TestCase1,"N/A","N/A")

    
    
    #####################################################################
    ############################ Go to Email ############################
    
    EmailFound =False
    TestCase2 ="Go to Email App"
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnOpenEmailApp").click()
    try:
        GmailButton = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/com.android.internal.widget.RecyclerView[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView")))
        GmailButton.click()
        sleep(3)
    except: 
        EmailFound =False

    
    if EmailFound==False:
        try:RefreshScreenusingswipe(driver)
        except:print("Can't Refresh Screen")
        sleep(1)

    
    Elements=driver.find_elements(By.ID,"com.google.android.gm:id/subject")
    for ELEM in Elements:
        Text=ELEM.text
        # print(Text)
        if Text == "Verify your email":
            ELEM.click()
            EmailFound=True
            break
            
        

    if EmailFound == True:
        print("Verify Email found!") 
        ReportResults(ReportDriver,driver,"StepTrue",TestCase2,"N/A","N/A")
  
   
    
    
#####################################################################
############### Test the email sent and verify user #################


    Status =True
    TestCase ="Email Test and Verify User"    


    try:
        Text11 =WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,"/hierarchy/android.widget.FrameLaycom.google.android.gm:id/recipient_summary")))
    except:
        print("Email isn't open yet")        
        #taponcoordinates(driver,150,1100) #On Samsung A52
        # taponcoordinates(driver,70,720) #On Tecno Cammon

    try:
        parentElement=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.TextView")
        parentElement.click()
    except: 
        print("Show quotes text not shown")
        

        
#    Text10 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.TextView").text
#    Text10Expected = Email
#    if (( Text10Expected != Text10)):
#        Status=False
#        ReportResults(ReportDriver, driver, Status,TestCase,Text10,Text10Expected)

    # Text11 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.TextView[2]").text
    # Text11Expected = "Please verify your email address"
    # if (( Text11Expected != Text11)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase,Text11,Text11Expected)

    # Text12 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.TextView[2]").text
    # Text12Expected = "In order to transact on your behalf, we need to verify a way of communicating with you. To verify your email address with us, please click the following secure link:"
    # if (( Text12Expected != Text12)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase,Text12,Text12Expected)

    # Text13 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.TextView[1]").text
    # Text13Expected = "Thank you for investing smarter,"
    # if (( Text13Expected != Text13)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase,Text13,Text13Expected)

    # Text14 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.TextView[2]").text
    # Text14Expected = "The NBK Capital SmartWealth Team"
    # if (( Text14Expected != Text14)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase,Text14,Text14Expected)

    # Text15 =driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View").text
    # Text15Expected = "Questions? Email | FAQs"
    # if (( Text15Expected != Text15)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase,Text15,Text15Expected)


    if Status == True:
        ReportResults(ReportDriver, driver, "StepTrue",TestCase,"N/A","N/A")

        
    try: 
        ELEM=driver.find_element(By.ID,"Verify now")
    except:
        ELEM=driver.find_element(By.XPATH,'//android.view.View[@content-desc="Verify now"]/android.widget.TextView')
        

    ELEM.click()    
    sleep(6)

    driver.press_keycode(187)
    sleep(2)
    closeapp(driver,1020, 1500, 1020, 500)
    taponcoordinates(driver,550,850)
        
        
def VerifyEmailusingAPI(driver, ReportDriver, Email, Password,Authorization="N/A"):
    

    try: 
        Text7 =WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/btnOpenEmailApp")))
    except:
        print("Email is already verified ")
        return True
    
    VerifyEmailAPI(ReportDriver, Email, Password,Authorization)
    
    # driver.press_keycode(3)
    # sleep(0.5)
    # driver.press_keycode(187)
    # sleep(0.5)
    # taponcoordinates(driver,550,850)
    
    # try:
    #     GetStartedScreen_SignIn(driver,ReportDriver)
    #     SignInScreen_Test(driver,ReportDriver, Email, Password)
    # except:SignInScreen_Test(driver,ReportDriver, Email, Password)

