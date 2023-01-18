import json
from time import sleep
from colorama import Fore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CheckIfPageLoading import CheckIfPageLoading


from ManualReport import ReportResults


def SignUpScreenTest(driver,ReportDriver ,Credentials):

    TestCase ="'Sign Up' Screen"

    Status =True


    

    Firstname_Fieldbox = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/firstNameEditText")))
    Lastname_Fieldbox = driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/lastNameEditText")
    Email_Fieldbox = driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/emailEditText")
    Password_Fieldbox = driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/inputEt")
    Signup_Button= driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnSignup")

    Email=Credentials["Email"]
    Firstname_Fieldbox.send_keys(Credentials["FirstName"])
    Lastname_Fieldbox.send_keys(Credentials["LastName"])
    Email_Fieldbox.send_keys(Credentials["Email"])
    print(Credentials["Email"])
    print(Email)
    Password_Fieldbox.click()
    
    Password_Fieldbox.send_keys(Credentials["Password"])

    while driver.is_keyboard_shown():
        driver.press_keycode(4)
        sleep(1)
    Signup_Button.click()
    

    sleep(1)
    
    
    CheckIfPageLoading(driver)
    StillonPage=True
    while StillonPage==True:
        sleep(0.5)
        try:
            a=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/labelTitle")
            StillonPage=True
            print ("\t"+ Fore.RED+"Issue in Email: %s, trying another..."%Email+Fore.RESET)
            print ("\tIssue in Email: %s, trying another..."%Email,file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnCancel").click()

            if (Email[(len(Email)-8)]).isdigit() ==True and (Email[(len(Email)-9)]).isdigit() == False and (Email[(len(Email)-10)]).isdigit() ==False:
                EmailCount=int(Email[(len(Email)-8)])+1
                Email=Email.replace(Email[(len(Email)-8)],  (str(EmailCount)))
                # print(Email)
                
            elif (Email[(len(Email)-8)]).isdigit() ==True and (Email[(len(Email)-9)]).isdigit() == True and (Email[(len(Email)-10)]).isdigit() ==False:
                
                EmailCount=int(Email[(len(Email)-9):(len(Email)-7)])+1
                Email=Email.replace((Email[(len(Email)-9):(len(Email)-7)]), (str(EmailCount)))
                # print(Email)
            
            # print([ Email[(len(Email)-10)].isdigit(),Email[(len(Email)-9)].
            #        isdigit(),Email[(len(Email)-8)].isdigit()])
            # print([ Email[(len(Email)-10)],Email[(len(Email)-9)],Email[(len(Email)-8)]])
           
            Email_Fieldbox.send_keys(Email)
            sleep(2)
            try:Signup_Button.click()
            except:
                driver.press_keycode(4)
                Signup_Button.click()
            
        except:
            try:
                a=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnOpenEmailApp")
                Credentials["Email"]=Email
                print(Fore.GREEN+"\tUser Signed Up Succesfully using: "+Credentials["Email"]+Fore.RESET)
                print("\tUser Signed Up Succesfully using: "+Credentials["Email"],file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

                StillonPage=False
                break
            except:
                try:
                    driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/btnSignup").click()
                    StillonPage=True
                except:
                    StillonPage=True

    
    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    # print(json_object)

    json_object["SingleUserDetails"]["Email"] = Email

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
    
    
    
    return Credentials

