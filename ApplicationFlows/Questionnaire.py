import json
from time import sleep
from colorama import Fore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from GesturesAndMotions import taponcoordinates
from investment_proposal.flows.customized.main import InvestmentProposalCustomizedFlow
from ManualReport import ReportResults
import pytest


def Questionnaire(driver,ReportDriver,RiskScore,JSON):
    Customized=InvestmentProposalCustomizedFlow(driver,RiskScore)
    Customized.start()
    
def Questionnaire_old(driver,ReportDriver, RiskScore,JSON):
    Status = True
    TestCase="Risk Questionnaire"
    
    print("Starting Questionnaire Flow... ")
    print("Starting Questionnaire Flow... ",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))

    SamePage=True
    while SamePage==True:
        if SamePage==True:
            Title=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")))
            Options= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/optionTextView")
            if Title.text ==  "What is your primary reason for investing?":
                for Option in Options:
                    if Option.text == "Aggressive growth and return":
                        Option.click()
                        sleep(1)
                        break
        A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")
        if A.text=="What is your current age?":
            sleep(0.2)
            SamePage=False
            print(Fore.GREEN+"\t"+Option.text +" is Successfull!!!"+Fore.RESET)
            print("\t"+Option.text +" is Successfull!!!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            break
        elif A.text=="What is your primary reason for investing?":
            SamePage=True
        
        
        
    SamePage=True
    while SamePage==True:
        if SamePage==True:
            Title=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")))
            try:AgeField= driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/textInput")
            except:sleep(0.1)
            if Title.text ==  "What is your current age?":
                AgeField.click()
                sleep(2)
                AgeField.send_keys("55")
                sleep(1)
                Keyboardshown=driver.is_keyboard_shown()
                if Keyboardshown==True:                
                    taponcoordinates(driver,1262,2737)
                else:
                    AgeField.click()
                
                
        A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")
        if A.text=="What is your monthly income (in USD)?":
            sleep(0.2)
            SamePage=False
            print(Fore.GREEN+"\t"+Title.text +" is Successfull!!!"+Fore.RESET)
            print("\t"+Title.text +" is Successfull!!!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            break
        elif A.text=="What is your current age?":
            SamePage=True


    SamePage=True
    while SamePage==True:
        if SamePage==True:
            Title=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")))
            Options= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/optionTextView")
            if Title.text ==  "What is your monthly income (in USD)?":
                for Option in Options:
                    if Option.text == "Greater than $15,001":
                        Option.click()
                        sleep(1)
                        break
                
    
        A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")
        if A.text=="What best describes your household?":
            sleep(0.2)
            SamePage=False
            print(Fore.GREEN+"\t"+Option.text +" is Successfull!!!"+Fore.RESET)
            print("\t"+Option.text +" is Successfull!!!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            break
        elif A.text=="What is your monthly income (in USD)?":
            SamePage=True

                
                    
    SamePage=True
    while SamePage==True:
        if SamePage==True:
            Title=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")))
            Options= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/optionTextView")
            if Title.text ==  "What best describes your household?":
                for Option in Options:
                    if Option.text == "Dual income, no dependents":
                        Option.click()
                        sleep(1)
                        break
            
        A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")
        if A.text=="What is the total value of your cash and liquid investments (in USD)?":
            sleep(0.2)
            SamePage=False
            print(Fore.GREEN+"\t"+Option.text +" is Successfull!!!"+Fore.RESET)
            print("\t"+Option.text +" is Successfull!!!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            break
        elif A.text=="What best describes your household?":
            SamePage=True

    
    SamePage=True
    while SamePage==True:
        if SamePage==True:
            Title=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")))
            Options= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/optionTextView")
            if Title.text ==  "What is the total value of your cash and liquid investments (in USD)?":
                for Option in Options:
                    if Option.text == "Greater than $5,000,000":
                        Option.click()
                        sleep(1)
                        break
        
        A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")
        if A.text=="I would rather have lower and predictable investment returns than ones which may be higher, but less predictable.":
            sleep(0.2)
            SamePage=False
            print(Fore.GREEN+"\t"+Option.text +" is Successfull!!!"+Fore.RESET)
            print("\t"+Option.text +" is Successfull!!!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            break
        elif A.text=="What is the total value of your cash and liquid investments (in USD)?":
            SamePage=True
    
    
    SamePage=True
    while SamePage==True:
        if SamePage==True:
            Title=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")))
            Options= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/optionTextView")
            if Title.text ==  "I would rather have lower and predictable investment returns than ones which may be higher, but less predictable.":
                for Option in Options:
                    if Option.text == "Strongly disagree":
                        Option.click()
                        sleep(1)
                        break
                    
        A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")
        if A.text=="I believe that I generally take bigger investment risks with my money than other people.":
            sleep(0.2)
            SamePage=False
            print(Fore.GREEN+"\t"+Option.text +" is Successfull!!!"+Fore.RESET)
            print("\t"+Option.text +" is Successfull!!!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            break
        elif A.text=="I would rather have lower and predictable investment returns than ones which may be higher, but less predictable.":
            SamePage=True
                
                
    SamePage=True
    while SamePage==True:
        if SamePage==True:
            Title=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")))
            Options= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/optionTextView")
            if Title.text ==  "I believe that I generally take bigger investment risks with my money than other people.":
                for Option in Options:
                    if Option.text == "Strongly agree":
                        Option.click()
                        sleep(1)
                        break
                    
        A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")
        if A.text=="I worry about losing money in the stock market.":
            sleep(0.2)
            SamePage=False
            print(Fore.GREEN+"\t"+Option.text +" is Successfull!!!"+Fore.RESET)
            print("\t"+Option.text +" is Successfull!!!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            break
        elif A.text=="I believe that I generally take bigger investment risks with my money than other people.":
            SamePage=True

                
    SamePage=True
    while SamePage==True:
        if SamePage==True:
            Title=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")))
            Options= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/optionTextView")
            if Title.text ==  "I worry about losing money in the stock market.":
                for Option in Options:
                    if Option.text == "Strongly disagree":
                        Option.click()
                        sleep(1)
                        break
             
        A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")
        if A.text=="If there’s a chance of making better long-term returns, I am willing to take an investment risk.":
            sleep(0.2)
            SamePage=False
            print(Fore.GREEN+"\t"+Option.text +" is Successfull!!!"+Fore.RESET)
            print("\t"+Option.text +" is Successfull!!!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            break
        elif A.text=="I worry about losing money in the stock market.":
            SamePage=True

                        
    SamePage=True
    while SamePage==True:
        if SamePage==True:
            Title=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")))
            Options= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/optionTextView")
            if Title.text ==  "If there’s a chance of making better long-term returns, I am willing to take an investment risk.":
                for Option in Options:
                    if Option.text == "Strongly agree":
                        Option.click()
                        sleep(1)
                        break
                        
        A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")
        if A.text=="I would be worried if I saw my investments had gone down in value.":
            sleep(0.2)
            SamePage=False
            print(Fore.GREEN+"\t"+Option.text +" is Successfull!!!"+Fore.RESET)
            print("\t"+Option.text +" is Successfull!!!",file = open('C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\Results.txt', 'a'))
            break
        elif A.text=="If there’s a chance of making better long-term returns, I am willing to take an investment risk.":
            SamePage=True

                        
    SamePage=True
    while SamePage==True:
        if SamePage==True:
            Title=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")))
            Options= driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/optionTextView")
            if Title.text ==  "I would be worried if I saw my investments had gone down in value.":
                for Option in Options:
                    if Option.text ==  "Strongly disagree":
                        Option.click()
                        sleep(1)
                        break
                
        try:
            A=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/questionTextView")
            if A.text=="I would be worried if I saw my investments had gone down in value.":
                SamePage=True
        except:
            SamePage=False

    if ReportDriver==None:
        print("No Report Driver found")
    elif Status == True:
        ReportResults(ReportDriver, driver, Status,TestCase,"N/A",  "N/A")
    else:
        ReportDriver.report().test(name=TestCase, message=TestCase+" has Failed!!", passed=False)
    
