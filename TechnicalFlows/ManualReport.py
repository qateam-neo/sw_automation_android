import os
from time import sleep

from colorama import Back, Fore

from HTMLFunctions import AddHTMLResults


def ReportResults(ReportDriver,driver,Status,TestCase,ActualText="N/A", ExpectedText="N/A",suggested_solution="N/A"):
    #ReportDriver.report().disable_auto_test_reports(disabled=True)

    ExpectedText=str(ExpectedText)
    ActualText=str(ActualText)
    if ReportDriver == None:
        if Status ==True:
            print(Fore.GREEN+"NEW test Case reported(TEST success)  "+TestCase+Fore.RESET)
            print("NEW test Case reported(TEST success)  "+TestCase,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            AddHTMLResults(TestCase, TestCase+" is Successful!!", "pass")
            
            
        if Status == False and ExpectedText!="N/A" and ActualText!="N/A" and suggested_solution!="N/A":
            print(Fore.RED+"new test Case reported(STEP Fail) "  +TestCase)
            print("\tExpected:\t"+ExpectedText)
            print("\tActual:\t"+ActualText )
            print("\tSuggested Solution:\t"+suggested_solution +Fore.RESET)
            
            
            print("new test Case reported(STEP Fail) "  +TestCase,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            sleep(1)
            print("\tExpected:\t"+ExpectedText ,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            sleep(1)
            print("\tActual:\t"+ActualText ,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            sleep(1)
            print("\tSuggested Solution:\t"+suggested_solution ,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            AddHTMLResults(TestCase, TestCase+" has Failed!!", "fail")
        
        elif Status == False and ExpectedText!="N/A" and ActualText!="N/A":
            print(Fore.RED+"new test Case reported(STEP Fail) "  +TestCase)
            print("\tExpected:\t"+ExpectedText)
            print("\tActual:\t"+ActualText )
            print("\tSuggested Solution:\t"+suggested_solution +Fore.RESET)
            
            print("new test Case reported(STEP Fail) "  +TestCase,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            sleep(1)
            print("\tExpected:\t"+ExpectedText ,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            sleep(1)
            print("\tActual:\t"+ActualText ,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            AddHTMLResults(TestCase, TestCase+" has Failed!!", "fail")

        elif Status == False:
            print(Fore.RED+"new test Case reported(STEP Fail) "  +TestCase + Fore.RESET)
            print("new test Case reported(STEP Fail) "  +TestCase,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            AddHTMLResults(TestCase, TestCase+" has Failed!!", "fail")

    else:    
    #Your test code goes here
        if Status ==True:
            ReportDriver.report().step(description=TestCase, message=TestCase+" is Successful!!", passed=True,screenshot=False)
            ReportDriver.report().test(name=TestCase, message=TestCase+" is Successful!!", passed=True)
            print(Fore.GREEN+"NEW test Case reported(TEST success)  "+TestCase+Fore.RESET)
            print("NEW test Case reported(TEST success)  "+TestCase,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
        
        if Status == False:
            ReportDriver.report().step(description=TestCase, message="Issue in "+ TestCase, passed=False, screenshot=False,inputs={"ExectedResults":ExpectedText,"ActualResults": ActualText} )
            driver.save_screenshot(os.getcwd()+"\FailedScreenshots\%s.png"%TestCase)
            print(Fore.RED+"new test Case reported(STEP Fail)"  +TestCase + Fore.RESET)
            print("new test Case reported(STEP Fail)"  +TestCase,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

        if Status=="StepTrue":
            ReportDriver.report().step(description=TestCase, message="Issue in "+ TestCase, passed=True, screenshot=False)

        
    #ReportDriver.quit()
    
def ReportResultsUserSmokeTest(ReportDriver,Status,User_Type,RiskScore,OnboardingFlow):
    #ReportDriver.report().disable_auto_test_reports(disabled=True)

    if ReportDriver == None:
        if Status ==True:
            print("\n\n"+Fore.BLUE+"Test Started for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow)+Fore.RESET+"\n\n")
            print("Test Started for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow),file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            AddHTMLResults("User Test Started", "User Test Started: "+User_Type+" "+RiskScore+" "+OnboardingFlow, "pass")

        if Status == False:
            print("\n\n"+Fore.YELLOW+"Test Retrying for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow)+Fore.RESET+"\n\n")
            print("Test Retrying for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow),file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            AddHTMLResults("Retring User", "Retrying User: "+User_Type+" "+RiskScore+" "+OnboardingFlow, "Fail")

    else:  
    
        #Your test code goes here 
        if Status ==True:
            ReportDriver.report().step(description="User Test Started", message="Test Started for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow), passed=True,screenshot=False)
            ReportDriver.report().test(name="User Test Started", message="User Test Started", passed=True)
            print("\n\n"+Fore.BLUE+"Test Started for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow)+Fore.RESET+"\n\n")
        
        
        if Status == False:
            ReportDriver.report().step(description="User Test Retrying", message="Test Retrying for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow), passed=False,screenshot=False)
            ReportDriver.report().test(name="User Test Retrying", message="User Test Retrying", passed=False)
            print("\n\n"+Fore.YELLOW+"Test Retrying for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow)+Fore.RESET+"\n\n")

def ReportUserFinalResults(ReportDriver,Status,User_Type,RiskScore,OnboardingFlow):
    #ReportDriver.report().disable_auto_test_reports(disabled=True)

    if ReportDriver == None:
        if Status ==True:
            print(Fore.GREEN+Back.GREEN+"Test is Successful for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow)+Fore.RESET+Back.RESET)
            print("Test is Successful for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow),file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            AddHTMLResults("User Test Done", "User Passed: "+User_Type+" "+RiskScore+" "+OnboardingFlow, "pass")

        if Status == False:
            print(Fore.RED+"Test has Failed for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow)+Fore.RESET)
            print("Test has Failed for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow),file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            AddHTMLResults("User Test Done", "User Failed: "+User_Type+" "+RiskScore+" "+OnboardingFlow, "fail")

    else:    
    #Your test code goes here 
        if Status ==True:
            ReportDriver.report().step(description="%s %s user test is Successful"%(OnboardingFlow,User_Type), message="Test is Successful for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow), passed=True,screenshot=False)
            ReportDriver.report().test(name="%s %s user test is Successful"%(OnboardingFlow,User_Type), message="Test is Successful for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow), passed=True)
            print(Fore.GREEN+Back.GREEN+"Test is Successful for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow)+Fore.RESET+Back.RESET)

        elif Status == False:
            ReportDriver.report().step(description="%s %s user test has Failed"%(OnboardingFlow,User_Type), message="Test has Failed for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow), passed=False,screenshot=False)
            ReportDriver.report().test(name="%s %s user test has Failed"%(OnboardingFlow,User_Type), message="Test has Failed for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow), passed=False)
            print(Fore.RED+"Test has Failed for %s user with Risk Score %s and going through %s Flow" %(User_Type, RiskScore,OnboardingFlow)+Fore.RESET)
    
        
    
def ReportResultsA(ReportDriver,driver,Status,TestCase,ActualText,ExpectedText):
    if Status==False:
        print(TestCase+" has Failed!!!")
    else:
        print(TestCase+" is Successfull!!")
        
def ReportResultsScreenNotShown(ReportDriver,TestCase):

    if ReportDriver == None:
        print(Fore.YELLOW+"%s is not shown"%TestCase+Fore.RESET)
        print("%s is not shown"%TestCase,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
        AddHTMLResults(TestCase, "%s is not shown"%TestCase, "not shown")

    else:    
        ReportDriver.report().step(description=TestCase, message=TestCase+" is not shown.", passed=False, screenshot=False)
        ReportDriver.report().test(name=TestCase, message=TestCase+" is Successful!!", passed=True)
        print(Fore.YELLOW+"%s is not shown"%TestCase+Fore.RESET)
        print("%s is not shown"%TestCase,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))



def ReportResultsAPICollection(ReportDriver,API_Name,StatusCode,Response):

    if ReportDriver == None:
        if StatusCode==200 or StatusCode=="200" or StatusCode=="201" or StatusCode==201:
            print("\t"+Fore.GREEN+API_Name +": "+str(StatusCode)+"\t is successful!"+Fore.RESET)
            print("\t"+API_Name +": "+str(StatusCode)+"\t is successful!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            AddHTMLResults(API_Name, API_Name +": "+str(StatusCode)+"\t is successful!", "passed")

        else:
            print("\t"+Fore.RED+API_Name +": "+str(StatusCode)+"\t Failed!")
            print("\t"+Fore.RED+Response+Fore.RESET)
            print("\t"+Fore.RED+API_Name +": "+str(StatusCode)+"\t Failed!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            AddHTMLResults(API_Name, API_Name +": "+str(StatusCode)+"\t has failed!", "fail")

    else:    

        if StatusCode==200 or StatusCode=="200" or StatusCode=="201" or StatusCode==201:
            print("\t"+Fore.GREEN+API_Name +": "+str(StatusCode)+"\t is successful!"+Fore.RESET)
            ReportDriver.report().step(description=API_Name, message=API_Name+" is Successful!!", passed=True,screenshot=False,inputs={"Status Code":StatusCode,"Response": Response})
            print("\t"+API_Name +": "+str(StatusCode)+"\t is successful!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

        else:
            ReportDriver.report().step(description=API_Name, message=API_Name+" Failed!!", passed=False,screenshot=False,inputs={"Status Code":StatusCode,"Response": Response})
            print("\t"+Fore.RED+API_Name +": "+str(StatusCode)+"\t Failed!")
            print("\t"+Fore.RED+Response+Fore.RESET)
            print("\t"+Fore.RED+API_Name +": "+str(StatusCode)+"\t Failed!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
