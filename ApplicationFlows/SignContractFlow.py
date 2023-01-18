from time import sleep
from colorama import Fore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from BlueScreens import Signyourcontract_Blue
from GesturesAndMotions import scrollDown, taponcoordinates



def SignContract(driver,ReportDriver):
    
    ContractSigned=False
    while ContractSigned==False:
        try:
            Signyourcontract_Blue(driver, ReportDriver)
            print("Attempting to sign contract:")
            sleep(2)
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")))
            WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View")))
            
            OKClicked=False
            while OKClicked==False:
                WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.widget.Button")))
                Elements=driver.find_elements(By.CLASS_NAME,"android.widget.Button")
                for ELEM in Elements:
                    if ELEM.text=="OK":
                        try: 
                            ELEM.click()
                            print(Fore.GREEN+"\tOK Clicked"+Fore.RESET)
                            OKClicked = True
                            break
                        except:
                            print(Fore.YELLOW+"\t"+ELEM.text +" is still not clickable"+Fore.RESET,end="\r")
                        
                
            sleep(2)
            GetStartedClicked=False
            while GetStartedClicked==False:
                WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.widget.Button")))
                Elements=driver.find_elements(By.CLASS_NAME,"android.widget.Button")
                for ELEM in Elements:
                    if ELEM.text=="Get Started":
                        try: 
                            ELEM.click()
                            print(Fore.GREEN+"\tGet Started Clicked"+Fore.RESET)
                            GetStartedClicked = True
                            break
                        except:
                            print(Fore.YELLOW+"\t"+ELEM.text +" is still not clickable"+Fore.RESET,end="\r")
                        

            sleep(2)
            PageLoaded=False
            while PageLoaded==False:
                WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.view.View")))
                Elements=driver.find_elements(By.CLASS_NAME,"android.view.View")
                for ELEM in Elements:
                    if ELEM.text=="Click to sign":
                        try:
                            print(Fore.GREEN+"\tClick to sign tab is shown")
                            PageLoaded = True
                            sleep(2)
                            break
                        except:
                            print(Fore.YELLOW+"\t"+ELEM.text +" is still not clickable"+Fore.RESET,end="\r")

            taponcoordinates(driver,147,1910)
            sleep(0.5)
            
            Signature=False
            while Signature==False:
                WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.view.View")))
                Elements=driver.find_elements(By.CLASS_NAME,"android.view.View")
                for ELEM in Elements:
                    if ELEM.text=="Click to sign":
                        try: 
                            ELEM.click()
                            print(Fore.GREEN+"\tClick to sign tab is clicked"+Fore.RESET)
                            Signature = True
                            sleep(0.5)
                            break
                        except:
                            print(Fore.YELLOW+"\t"+ELEM.text +" is still not clickable"+Fore.RESET,end="\r")
                            
            #Signature
            scrollDown(driver,300, 1200,1100, 1600)
            sleep(0.1)
            scrollDown(driver,1100, 1600,1100, 1200)
            sleep(0.5) 
            # scrollDown(driver,890, 872,193, 1316)
            
            InsertEverywhere=False
            while InsertEverywhere==False:
                WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.widget.Button")))
                Elements=driver.find_elements(By.CLASS_NAME,"android.widget.Button")
                for ELEM in Elements:
                    if ELEM.text=="Insert everywhere":
                        try: 
                            ELEM.click()
                            print(Fore.GREEN+"\tInsert everywhere button is shown"+Fore.RESET)
                            InsertEverywhere = True
                            sleep(0.5)
                            break
                        except:
                            print(Fore.YELLOW+"\t"+ELEM.text +" is still not clickable"+Fore.RESET,end="\r")
                        
            sleep(3)
            ContinueShown=False
            while ContinueShown==False:
                WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.widget.Button")))
                Elements=driver.find_elements(By.CLASS_NAME,"android.widget.Button")
                for ELEM in Elements:
                    if ELEM.text=="Continue":
                        try: 
                            ELEM.click()
                            print(Fore.GREEN+"\tContinue button is shown"+Fore.RESET)
                            ContinueShown = True
                            sleep(0.5)
                            break
                        except:
                            print(Fore.YELLOW+"\t"+ELEM.text +" is still not clickable"+Fore.RESET,end="\r")
                        
            
            IAgreeShown=False
            while IAgreeShown==False:
                WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.widget.Button")))
                Elements=driver.find_elements(By.CLASS_NAME,"android.widget.Button")
                for ELEM in Elements:
                    if ELEM.text=="I agree":
                        try:
                            ELEM.click()
                            print(Fore.GREEN+"\tI agree button is shown"+Fore.RESET)
                            IAgreeShown = True
                            sleep(0.5)
                            break
                        except:
                            print(Fore.YELLOW+"\t"+ELEM.text +" is still not clickable"+Fore.RESET,end="\r")
            

            try:
                WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvBannerDesc")))
                ContractSigned = True
                break
            except:
                ContractSigned = False
                
                
            if ContractSigned == False:
                    # WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"android.view.View"))) 
                    # A=driver.find_elements(By.CLASS_NAME,"android.view.View")
                    # for ELEM in A:
                    #     if ELEM.text=="index":
                    driver.press_keycode(4)
                    try:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))
                        ApproxTime=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTime")
                        if len(ApproxTime) == 2: 
                            Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
                            Titles[1].click()
                            ContractSigned=False
                            
                        elif len(ApproxTime) == 1:
                            Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle") # User is approved, skip 
                            ContractSigned=True
                            break
                        
                    except:
                        print("Another Error is occuring on contract, contract signed but Pending dashboard is not shown yet.")
            
        except:
            driver.press_keycode(4)
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))
                ApproxTime=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTime")
                if len(ApproxTime) == 2: 
                    Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
                    Titles[1].click()
                    ContractSigned=False
                    
                elif len(ApproxTime) == 1:
                    Titles=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle") # User is approved, skip 
                    ContractSigned=True
                    break
                
            except:
                print(" (Except) Error on signature,Pending dashboard is most probably not shown.")
                        
                
                
            