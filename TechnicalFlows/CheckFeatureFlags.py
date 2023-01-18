from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from colorama import Fore

def FeatureFlag(driver,Feature):
    FeatureAvailable = False
    Feature=Feature.lower()
    if "bank" in Feature or "transfer" in Feature or "bt" in Feature:
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/md_text_message")))
            if "maintenance" in driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_text_message").text :
                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_button_positive").click()
                print(Fore.RED+"Bank Transfer Deposits are disabled from FireBase"+Fore.RESET)
                print("Bank Transfer Deposits are disabled from FireBase",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
                FeatureAvailable=False
        except:
                print("Bank Transfer Deposit is enabled from FireBase")
                FeatureAvailable=True
    elif Feature=="Deposit":
        try: 
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/md_text_message")))
            if "maintenance" in driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_text_message").text :
                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_button_positive").click()
                print(Fore.RED+"All Deposit are disabled from FireBase"+Fore.RESET)
                print("All Deposit are disabled from FireBase",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
                FeatureAvailable=False
        except:
                print("Deposit is enabled from FireBase")
                FeatureAvailable=True

    if Feature=="withdrawal":
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/md_text_message")))
            if "maintenance" in driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_text_message").text :
                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_button_positive").click()
                print(Fore.RED+"All Withdrawals are disabled from FireBase"+Fore.RESET)
                print("All Withdrawals are disabled from FireBase",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
                FeatureAvailable=False
        except:
                print("Withdrawals are enabled from FireBase")
                FeatureAvailable=True

    if "full" in Feature:
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/md_text_message")))
            if "maintenance" in driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_text_message").text :
                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_button_positive").click()
                print(Fore.RED+"Full Withdrawals are disabled from FireBase"+Fore.RESET)
                print("Full Withdrawals are disabled from FireBase",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
                FeatureAvailable=False
        except:
                print("Full Withdrawals are enabled from FireBase")
                FeatureAvailable=True

    if "partial" in Feature:
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/md_text_message")))
            if "maintenance" in driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_text_message").text :
                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_button_positive").click()
                print(Fore.RED+"Partial Withdrawals are disabled from FireBase"+Fore.RESET)
                print("Partial Withdrawals are disabled from FireBase",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
                FeatureAvailable=False
        except:
                print("Partial Withdrawals are enabled from FireBase")
                FeatureAvailable=True

    if "onboarding" in Feature and ("callback" in Feature or "cb" in Feature):
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/md_text_message")))
            if "maintenance" in driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_text_message").text :
                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_button_positive").click()
                print(Fore.RED+"Onboarding CallBack is disabled from FireBase"+Fore.RESET)
                print("Onboarding CallBack is disabled from FireBase",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
                FeatureAvailable=False
        except:
                print("Onboarding CallBack is enabled from FireBase")
                FeatureAvailable=True

    if ("withdraw" in Feature or "withdrawal" in Feature) and ("callback" in Feature or "cb" in Feature):
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/md_text_message")))
            if "maintenance" in driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_text_message").text :
                driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/md_button_positive").click()
                print(Fore.RED+"Withdrawal CallBack is disabled from FireBase"+Fore.RESET)
                print("Withdrawal CallBack is disabled from FireBase",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
                FeatureAvailable=False
        except:
                print("Withdrawal CallBack is enabled from FireBase")
                FeatureAvailable=True

    else:
        print("Wrong Input for Feature")
    return FeatureAvailable