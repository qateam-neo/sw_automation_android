from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import pytest
from CheckIfPageLoading import CheckIfPageLoading
from ManualReport import ReportResults

 
def InvestmentProposal(driver,ReportDriver ,User_Type="N/A"):

    TestCase ="'Investment Proposal' Screen"
    sleep(5)
    Status=True
    count=0    
    SamePage=True
    while SamePage==True:
        CheckIfPageLoading(driver)

        try:
            A=WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/title"))).text
            if "api" in A or "depricated" in A:
                driver.press_keycode(4)
            else: raise ValueError("API Depricated is not shown")

        except:
            try:
                if User_Type != "N/A":
                    if (User_Type=="Islamic" or User_Type=="islamic" or User_Type=="Is") and count==0:
                        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/islamic").click()
                        count=1
                    else: raise ValueError('Islamic button not shown in investment proposal.')
            except:
                try:
                    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/holdingTextView")
                    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "neo.nbkc.smartwealth.demo:id/accountButton"))).click()
                                
                except:
                    try:
                        driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/lastNameEditText")
                        SamePage=False
                    except:
                        print("Investment proposal, API depricated not shown, investment proposal page not loaded yet...")
             
    # Status=True
    # APIDep=True
    # while APIDep==True:
        
    #     try:
    #         A=WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/title"))).text
    #         if "api" in A or "depricated" in A:
    #             driver.press_keycode(4)
    #             CheckIfPageLoading(driver)
    #     except:
    #         print("API Depricated is not shown")
    #         APIDep=False
    #         break
        
    # WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/accountButton")))
    # try:
    #     if User_Type != "N/A":
    #         if User_Type=="Islamic" or User_Type=="islamic" or User_Type=="Is":
    #             driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/islamic").click()
    #             CheckIfPageLoading(driver)
    #             try:
    #                 A=WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/title"))).text
    #                 if "api" in A or "depricated" in A:
    #                     driver.press_keycode(4)
    #                     CheckIfPageLoading(driver)
    #             except:
    #                 sleep(1)
    #                 print("API Depricated is not shown")
    #                 APIDep=False
                    

    # except:
    #     print("Investment Type chosen in the screen before (Investment Type)")            
    # WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/accountButton"))).click()

        
    if ReportDriver==None:
        print("No Report Driver found")
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
     



def InvestmentProposal_ETFTest_Detailed(driver,ReportDriver ,riskscore):
    
    TestCase ="'Investment Proposal' Screen"

    Text1Expected = None
    Text3Expected = None
    i =int(riskscore)-1
    Status =True
    Text = []

    # Percentages Array is in the following Format: Fixed Income, Developed Market Stocks, Emerging Market Stocks, Real Estate, Cash.
    Percentages = [["84", "14", "0", "0", "2"], 
                   ["69", "29", "0", "0", "2"], 
                   ["59", "39", "0", "0", "2"], 
                   ["49", "49", "0", "0", "2"], 
                   ["39", "52", "7", "0", "2"], 
                   ["38", "53", "7", "0", "2"], 
                   ["32", "56", "10", "0", "2"], 
                   ["19", "69", "10", "0", "2"], 
                   ["5", "71", "14", "8", "2"], 
                   ["0", "74", "14", "10", "2"]
                   ]
    
    Percentagegrowthpa = ["5.1", "5.6", "6.1", "6.2", "6.5", "7.4", "7.4", "7.6", "7.1", "7.1"]


    if riskscore=="3":
        Text1Expected = "You have selected a conservative investment plan"
        Text3Expected = "This means your asset mix will have greater exposure to more stable and income focused instruments while your returns will be just above inflation."

    elif riskscore=="5":

        Text1Expected = "You have selected a balanced investment plan"
        Text3Expected = "This means your asset mix will focus on income and growth instruments to achieve greater returns. You can expect to see some downturns to achieve such returns."

    else:

        Text1Expected = "You have selected a growth investment plan"
        Text3Expected = "This means your asset mix will focus on growth instruments to achieve the highest returns. We recommend a long-term investment horizon as markets run through their cycles."


    Element1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView")))
    Text1=Element1.text

    if (( Text1Expected != Text1)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase, Text1,Text1Expected)

    Text2 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.Button").text
    Text2Expected = "What does this mean?"
    if (( Text2Expected != Text2)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text2,Text2Expected)


    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/expandButton").click()


    X3 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView[2]")))
    Text3=X3.text
    
    if (( Text3Expected != Text3)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text3,Text3Expected)

    Text4 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView").text
    Text4Expected = "Risk Tolerance: "+str(riskscore)
    if (( Text4Expected != Text4)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text4,Text4Expected)

    Text5 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RadioGroup/android.widget.RadioButton[1]").text
    Text5Expected = "Global Multi-Asset"
    if (( Text5Expected != Text5)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text5,Text5Expected)

    Text6 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.TextView[1]").text
    Text6Expected = "ASSET CLASS"
    if (( Text6Expected != Text6)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text6,Text6Expected)

    Text7 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.TextView[2]").text
    Text7Expected = "ALLOCATION"
    if (( Text7Expected != Text7)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text7,Text7Expected)

    Text8 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]").text
    Text8Expected = "Fixed Income"
    if (( Text8Expected != Text8)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text8,Text8Expected)

    Text9 =driver.find_element_by_xpath("hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]").text
    Text9Expected = Percentages[i][0] +"%"
    if (( Text9Expected != Text9)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text9,Text9Expected)

    Text10 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]").text
    Text10Expected = "Developed Market Stocks"
    if (( Text10Expected != Text10)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text10,Text10Expected)

    Text11 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]").text
    Text11Expected = Percentages[i][1] +"%"
    if (( Text11Expected != Text11)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text11,Text11Expected)

    Text12 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[4]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]").text
    Text12Expected = "Emerging Market Stocks"
    if (( Text12Expected != Text12)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text12,Text12Expected)

    Text13 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[4]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]").text
    Text13Expected = Percentages[i][2] +"%"
    if (( Text13Expected != Text13)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text13,Text13Expected)

    Text14 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[5]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]").text
    Text14Expected = "Real Estate"
    if (( Text14Expected != Text14)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text14,Text14Expected)

    Text15 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[5]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]").text
    Text15Expected = Percentages[i][3] +"%"
    if (( Text15Expected != Text15)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text15,Text15Expected)

    Text16 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[6]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]").text
    Text16Expected = "Cash"
    if (( Text16Expected != Text16)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text16,Text16Expected)

    Text17 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[6]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]").text
    Text17Expected = Percentages[i][4] +"%"
    if (( Text17Expected != Text17)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text17,Text17Expected)

    Text18 =driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.Button").text
    Text18Expected = "View Historical Performance"
    if (( Text18Expected != Text18)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text18,Text18Expected)

    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/historicalChartButton").click()
    sleep(1)


# ###############################SWIPEEEE
#     action = TouchActions(driver)
#     action.scroll(500,3000)


    Text19 =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/historicalChartButton").text
    Text19Expected = "Hide Historical Performance"
    if (( Text19Expected != Text19)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text19,Text19Expected)

    Text20 =driver.find_element_by_xpath("//*[@text='Based on a $10,000 investment']").text
    Text20Expected = "Based on a $10,000 investment"
    if (( Text20Expected != Text20)):
        Status=False
        ReportResults(ReportDriver, driver, Status,TestCase,Text20,Text20Expected)

    # Text21 =driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/chartDescriptionTextView").text
    # # Text21Expected = "(+Percentagegrowthpa[i]+"% growth p.a.)"
    # if (( Text21Expected != Text21)):
    #     Status=False
    #     ReportResults(ReportDriver, driver, Status,TestCase,Text21,Text21Expected)


    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
        
    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/historicalChartButton").click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/accountButton"))).click()

    
