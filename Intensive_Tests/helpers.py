import json
import os

from Intensive_Tests.kyc.flows.personal_info.config import Field_types
print(os.getcwd())

import requests
from Intensive_Tests.investment_proposal.config import IDS
from Intensive_Tests.deposits.config import IDS as Deposit_IDS

from Intensive_Tests.signup_login.flows.sign_in.config import Credentials
import SystemPath
from time import sleep
from colorama import Fore
import psycopg2
from Intensive_Tests.enums import AndroidEnums
from selenium.webdriver.support.ui import WebDriverWait # needs to be used when creating a function everytime
from selenium.webdriver.support import expected_conditions # needs to be used when creating a function everytime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import string
from appium.webdriver.common.touch_action import TouchAction

from ManualReport import ReportResults

from appium.webdriver.common.mobileby import MobileBy

class AndroidGestures():
    
    def __init__(self,driver):
        self.driver = driver
    
    def BACK(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_BACK))
        
    def HOME(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_HOME))
    
    def APP_SWITCH(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_APP_SWITCH))

    def BACKSLASH(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_BACKSLASH))

    def VOLUME_UP(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_VOLUME_UP))
        
    def VOLUME_DOWN(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_VOLUME_DOWN))
        
    def VOLUME_MUTE(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_VOLUME_MUTE))
        
    def CLEAR(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_CLEAR))
    
    def COPY(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_COPY))

    def CUT(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_CUT))
        
    def PASTE(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_PASTE))
        
    def DELETE(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_DEL))
        
    def ENTER(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_ENTER))
        
    def ESCAPE(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_ESCAPE))
        
    def REFRESH(self):
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_HOME))
        WebDriverWait(self.driver,6).until(expected_conditions.visibility_of_element_located((By.XPATH,'//android.view.View[@content-desc="Home"]')))
        sleep(0.75)
        self.driver.press_keycode(int(AndroidEnums.KEYCODE_APP_SWITCH))
        sleep(1.5)
        self.driver.find_element(By.XPATH,'//android.widget.FrameLayout[@content-desc="SmartWealth-uat"]').click()
        
        
        
class AppiumActions:
    
    def __init__(self,driver):
        self.driver = driver
        self.action_chains=ActionChains(self.driver)
        self.Android=AndroidGestures(self.driver)
        self.action = TouchAction(self.driver)

    
    def scroll_down(self):
        self.action.press(x=500, y=1500).move_to(x=500, y=500).release().perform()

    def scroll_up_date(self):
        self.action.press(x=500, y=1100).move_to(x=500, y=2000).release().perform()
        
    def scroll_down_expiry_date(self):
        self.action.press(x=500, y=2000).move_to(x=500, y=1100).release().perform()

    def return_to_pending_dashboard(self):
        while not self._check_if_visible("neo.nbkc.smartwealth.demo:id/tvTime",1):
            self.Android.BACK()

    def return_to_active_dashboard(self):
        while not self._check_if_visible("neo.nbkc.smartwealth.demo:id/earningsCard",5) or not self._check_if_visible("neo.nbkc.smartwealth.demo:id/balanceCard",5):
            self.Android.BACK()


    def return_to_payment_method(self):
        while not self._check_if_visible(Deposit_IDS.SelectPaymentMethod.description,3):
            self.Android.BACK()
    
    
    def get_element(self,ID):
        if len(ID)==2:
            return (self.driver.find_elements(By.ID,ID[0]))[ID[1]]
        else: return self.driver.find_element(By.ID,ID)
    
    def get_elements(self,ID):
        elements=self.driver.find_elements(By.ID,ID)
        return elements
    
    def wait_for_element(self,ID,timeout=5):        
        if len(ID)==2:
            WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located((By.ID,ID[0])))
            return (self.driver.find_elements(By.ID,ID[0]))[ID[1]]
        else: return WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located((By.ID,ID)))

    def wait_for_elements(self,ID,timeout=5):
        WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located((By.ID,ID)))        
        elements=self.driver.find_elements(By.ID,ID)
        return elements
    
    def _check_if_visible(self,ID,timeout=4):
        try:
            element=self.wait_for_element(ID,timeout)
            return element
        except:
            return False
        
    def click_element(self,ID,timeout=None):
        if timeout is not None :    self.wait_for_element(ID,timeout).click()
        else:   self.get_element(ID).click()

    def send_otp_text(self,ID,otp,skip=False,timeout=4):
        self.wait_for_element(ID,timeout).send_keys(str(otp))

    
    def scrollDown_refresh(self,x_initial=452, y_initial=544, x_final=416, y_final= 1694):
        self.driver.swipe(x_initial,y_initial,x_final,y_final,626)

    def send_keys_to_element(self,message,ID=None,element=None,skip=False,timeout=4):
        if element is None:
            self.wait_for_element(ID,timeout).send_keys(message)
            shown_message=self.get_element(ID).text
            if shown_message != message and not skip:
                try: 
                    message="$"+format(int(message), ',d')
                    if shown_message ==message:
                        return True
                    else:raise ValueError("Intended.")
                except:
                    self.click_element(ID)
                    sleep(1)
                    self.action_chains.send_keys(message).perform()
                    if self.driver.is_keyboard_shown():
                        self.driver.press_keycode(4) 
        else:
            element.click()
            sleep(1)
            self.action_chains.send_keys(message).perform()
            if self.driver.is_keyboard_shown():
                self.driver.press_keycode(4) 

            
        
        
    def wait_for_element_class(self,CLASS,timeout=5):     

        if len(CLASS) ==2:
            try:
                WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,CLASS[0])))
                temp=self.driver.find_elements(By.CLASS_NAME,CLASS[0])
                for ELEM in temp:
                    # print(ELEM.text)
                    if ELEM.text == CLASS[1]:
                        return ELEM
                return False
            except:return False
            
        else: return self.driver.find_elements(By.CLASS_NAME,CLASS[0])

    def wait_for_elements_class(self,CLASS,timeout=5):
            WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,CLASS)))
            return self.driver.find_elements(By.CLASS_NAME,CLASS)
        
        
    def search_element_by_id_text(self,ID,trigger_text=None,timeout=5):        
        if len(ID)==2 and trigger_text is None:
            WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located((By.ID,ID[0])))
            x=self.driver.find_elements(By.ID,ID[0])
            for ELEM in x: 
                if (ELEM.text==ID[1]):return ELEM
            return False
        elif len(ID)==2 and trigger_text is not None:
            WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located((By.ID,ID[0])))
            x=self.driver.find_elements(By.ID,ID[0])
            for ELEM in x: 
                if (ELEM.text==trigger_text):return ELEM
            return False
        elif len(ID)==1 and trigger_text is not None:
            WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located((By.ID,ID)))
            x=self.driver.find_elements(By.ID,ID)
            for ELEM in x: 
                if (ELEM.text==trigger_text):return ELEM
            return False
        
    def find_element_by_text(self,text):
        return self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'%s')]"%text)

        
    def find_element_parent_by_text(self,Field):
        # locator="//*[contains(@class, '%s')]"%Field.parent_class
        locator=Field.parent_id
        print(locator)
        print(Field.parent_class)
        element = self.wait_for_elements(locator,1)
        for i in range(0,1):
            for elem in element:
                try:
                    elem.find_element(MobileBy.XPATH,"//*[contains(@text,'%s')]"%Field.trigger_Title)
                    return elem
                except:
                    pass 
        return False
    
    def choose_option(self,parent,Field):
        if not Field.mapped_by_index:
            #Get values inside parent            
            options=parent.find_elements(By.ID,Field.id)
            for option in options:
                if Field.choice in option.text:
                    option.click()
                    break
            print("ISSUE IN CHOOSING OPTION, Can't find choice. Field: "+Field.trigger_Title)
        else:
            options=parent.find_elements(By.ID,Field.id)
            options[Field.choice].click()
            
    def fill_input(self,parent,Field):
        if not Field.mapped_by_index:
            input=parent.find_element(By.ID,Field.id)
            self.send_keys_to_element(Field.choice,element=input)
        else:
            input=parent.find_elements(By.ID,Field.id)[Field.index]
            self.send_keys_to_element(Field.choice,element=input)

    def forward_orientation(self,single_element_id):
        elements=self.get_elements(single_element_id)
        old_element=elements[1]
        self.scroll_up_date()
        elements=self.get_elements(single_element_id)
        if old_element==elements[1]:
            return False
        else:
            return True
        
    def _fill_year(self,Field):
        self.click_element(Field_types.date_picker.year.id,6)
        old_element="N/A"
        Forward=True
        Forward=self.forward_orientation(Field_types.date_picker.year.single_year_id)

        while True:
            elements=self.get_elements(Field_types.date_picker.year.single_year_id)
            for elem in elements:
                if elem.text == Field.choice_year:
                    elem.click()
                    return True
            if Forward:     self.scroll_up_date()
            else:   self.scroll_down_expiry_date()
            sleep(0.3)
    
    def _fill_month(self,Field):
        months=["January", "February", "March", "April", "May", "June","July","August","September","October","November","December"]
        if Field.choice_month.isdigit(): 
            choice=months[int(Field.choice_month)-1]
        else:
            choice=Field.choice_month
        while True:
            parent= self.wait_for_element(Field_types.date_picker.month.parent_id)
            element=parent.find_element(By.CLASS_NAME,Field_types.date_picker.month.class_name)
            full_date=element.get_attribute("content-desc")
            month=""
            for char in full_date: 
                if char.isalpha():  month=month+char
                
            if month == choice: return True
            elif months.index(month) > months.index(choice): 
                self.click_element(Field_types.date_picker.month.back_button_id)
            elif months.index(month) < months.index(choice): 
                self.click_element(Field_types.date_picker.month.next_button_id)

    def _fill_day(self,Field):
        self.find_element_by_text(Field.choice_day).click()
            
        
    def fill_date_picker(self,parent,Field):
        parent.find_element(By.ID,Field.id).click()
        sleep(1.5)
        self._fill_year(Field)
        self._fill_month(Field)
        self._fill_day(Field)
        self.click_element(Field_types.date_picker.ok_button_id)
    
    def fill_list_picker(self,parent,Field):
        parent.find_element(By.ID,Field.id).click()
        elements=self.get_elements(Field_types.list_picker.single_country_id)
        for elem in elements:
            if elem.text == Field.choice:
                elem.click()
                return True
        sleep(1)
        scroller=self.get_element(Field_types.list_picker.scroller.parent_id)
        scroller_letters=scroller.find_elements(By.CLASS_NAME,Field_types.list_picker.scroller.values_class_name)
        for letter in scroller_letters:
            if letter.text == Field.choice[0]:
                letter.click()
                break
        sleep(1)
        elements=self.get_elements(Field_types.list_picker.single_country_id)
        for elem in elements:
            if elem.text == Field.choice:
                elem.click()
                return True
        return False

class Reporting():
    def __init__(self,driver,flow) :
        self.ReportDriver=None
        self.driver=driver
        self.flow=flow
    
    def change_flow(self,flow):
        self.flow=flow
    
    def report_testcase(self,status,screen,risk_score,expected="N/A",actual="N/A",solution="N/A"):
        # message="\t%s %s flow on risk score %s"%(screen,self.flow,str(risk_score))

        risk_score=str(risk_score)
        if status:
            print(Fore.GREEN+"TEST success:  %s on %s with risk score %s"%(screen,self.flow,risk_score)+Fore.RESET)
            print("TEST success:  "+screen,file = open(os.getcwd()+'/BaseClasses/Results.txt', 'a'))
            
            
        if status == False and expected!="N/A" and actual!="N/A" and solution!="N/A":
            print(Fore.RED+"TEST Fail: %s on %s with risk score %s"%(screen,self.flow,risk_score))
            print("\tExpected:\t\t"+expected)
            print("\tActual:\t\t"+actual )
            print("\tSuggested Solution:\t\t"+solution +Fore.RESET)
            
            
            print("TEST Fail: "  +screen,file = open(os.getcwd()+'/BaseClasses/Results.txt', 'a'))
            sleep(1)
            print("\tExpected:\t\t"+expected ,file = open(os.getcwd()+'/BaseClasses/Results.txt', 'a'))
            sleep(1)
            print("\tActual:\t\t"+actual ,file = open(os.getcwd()+'/BaseClasses/Results.txt', 'a'))
            sleep(1)
            print("\tSuggested Solution:\t\t"+solution ,file = open(os.getcwd()+'/BaseClasses/Results.txt', 'a'))
        
        elif status == False and expected!="N/A" and actual!="N/A":
            print(Fore.RED+"TEST Fail: %s on %s with risk score %s"%(screen,self.flow,risk_score))
            print("\tExpected:\t\t"+str(expected))
            print("\tActual:\t\t"+str(actual) )
            print("\tSuggested Solution:\t\t"+str(solution) +Fore.RESET)
            
            print("TEST Fail: "  +screen,file = open(os.getcwd()+'/BaseClasses/Results.txt', 'a'))
            sleep(1)
            print("\tExpected:\t\t"+expected ,file = open(os.getcwd()+'/BaseClasses/Results.txt', 'a'))
            sleep(1)
            print("\tActual:\t\t"+actual ,file = open(os.getcwd()+'/BaseClasses/Results.txt', 'a'))

        elif status == False:
            print(Fore.RED+"TEST Fail: %s on %s with risk score %s"%(screen,self.flow,risk_score)+Fore.RESET)
            print("TEST Fail: "  +screen,file = open(os.getcwd()+'/BaseClasses/Results.txt', 'a'))

    def report_testcase_not_shown(self,screen):
            print(Fore.YELLOW+"TEST Skip: %s is not shown"%screen+Fore.RESET)
            print("%s is not shown"%screen,file = open(os.getcwd()+'/BaseClasses/Results.txt', 'a'))


class Random_values:
    
    # def __init__(self) :
    #     pass
    
    class generate_alphanumeric_value:
        
        def in_range( min, max):
            characters = string.ascii_lowercase + string.digits
            return (''.join(random.choice(characters) for i in range(random.randint(min,max))))

        def with_length( length):
            characters = string.ascii_lowercase + string.digits
            return (''.join(random.choice(characters) for i in range(length)))

    class generate_numeric_value:
        
        def between_2_numbers(min_number, max_number):
            return random.randint(min_number, int(max_number))
        
        def in_range(min, max):
            return (''.join(random.choice(string.digits) for i in range(random.randint(min,max))))

        def with_length(length):
            return (''.join(random.choice(string.digits) for i in range(length)))
        

    class generate_alphabetical_value:
        
        def in_range( min, max):
            return (''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(min,max))))

        def with_length( length):
            return (''.join(random.choice(string.ascii_lowercase) for i in range(length)))


class DataBase:
        
    def __init__(self):  
        self.postgres=psycopg2.connect(database="postgres", user="ro_user", password="55bA7$SG8M1a", host="nbkcsw-live-2.cpr22mx3duxb.eu-central-1.rds.amazonaws.com", port="5432").cursor("postgres")
    
    def get_emails(self,email_prefix='roy.braish',investment_type='%%',
                   etf_risk_score='*',islamic_risk_score='*',
                   classification_type='%%'):
        if islamic_risk_score == '*':
            islamic_risk_score_minimum=0
            islamic_risk_score=11
        else:
            islamic_risk_score_minimum=int(islamic_risk_score)-1
            islamic_risk_score=int(islamic_risk_score)+1
            
        if etf_risk_score == '*':
            etf_risk_score_minimum=0
            etf_risk_score=10
        else:
            etf_risk_score_minimum=int(etf_risk_score)-1
            etf_risk_score=int(etf_risk_score)+1

        email_prefix='%'+email_prefix+'%'

        query=  """
                    SELECT email FROM user_profile
                    WHERE investment_type LIKE '%s'
                    AND original_risk_score > %i
                    AND original_risk_score < %i        
                    AND modified_risk_score > %i
                    AND modified_risk_score < %i        
                    AND classification_type LIKE '%s'
                    AND email LIKE '%s'
                """     %(  investment_type,
                            etf_risk_score_minimum,
                            etf_risk_score,
                            islamic_risk_score_minimum,
                            islamic_risk_score,
                            classification_type,
                            email_prefix)
        print(query)
        self.postgres.execute(query=query)


        rows = self.postgres.fetchall()
        Emails=[]
        for row in rows:
            row=str(row)
            row=row.strip("(")
            row=row.strip(")")
            row=row.strip(",")
            row=row.strip("'")
            
            Emails.append(row)
            # print(row)
        # print(Emails)
        if Emails == [] :
            return "No Results Found"
        return Emails 
    
    def get_latest_email(self,emailprefix):
        emailprefix=emailprefix.lower()
        query=  """
                    SELECT email FROM user_profile
                    WHERE email LIKE '%""" +str(emailprefix)+"%'"+"""
                    ORDER BY created_at DESC; """
                    
        self.postgres.execute(query=query)
        rows = self.postgres.fetchall()
        
        # print(rows[0])
        row=str(rows[0])
        row=row.strip("(")
        row=row.strip(")")
        row=row.strip(",")
        row=row.strip("'")

        return row

class APIS:
    def __init__(self,driver="N/A",email="default"):  
        self.driver = driver
        self.SW_UAT_URL="https://api.nbkcapital-smartwealth.com/api/v2/"
        if email!="default":self.email=email
        else:self.email=Credentials.email
        self.password=Credentials.password
        self.AndroidGestures=AndroidGestures(self.driver)
        try:self._get_user_profile()
        except:
            try:self._get_user_profile()
            except:
                print("Get user API is showing error")
        
        # self.Authorization=self._get_user_token()
        
    def _get_header(self):
        self.headers={
            "Authorization":self.Authorization,
            "x-locale":"en_US",
            "x-version":"1.8.68",
            "x-platform":"android",
            "Content-Type":"application/json"}
        return self.headers
    
    def _get_user_profile(self,flag="N/A"):
        """
        :flag: { "id",  "auth0_id",  "first_name",  "last_name",  "date_of_birth",  "account_manager_id",  "email",  "phone_number",  "original_risk_score",  "modified_risk_score",  "base_risk_score",  
        "finished_kyc",  "uploaded_civilID",  "is_finished_risk_funnel",  "finished_questionnaire_a",  "finished_questionnaire_b",  "signed_contract",  "is_contract_confirmed",  "is_pipeline",  "wired_funds",  
        "bank_name",  "bank_description",  "beneficiary_name",  "iban_number": "8236316311",  "account_number": null,  "email_is_verified",  "nationality": "KW",  "has_transaction",  "has_verified_transaction",  
        "latest_transfer_method",  "has_saxo_account",  "has_mmf_account",  "net_deposits",  "nav_value",  "investment_type",  "is_notify_user",  "is_approved",  "primary_id_front_scanned",  "primary_id_back_scanned", 
        "secondary_id_scanned",  "uploaded_video_status",  "id_manually_uploaded",  "is_onboarded_through_rm",  "is_onboarded_offline,"is_welcome_closed", "is_international", "classification_type", 
        "is_classification_confirmed", "is_premium", "is_black", "is_black_interested", "is_eid_verified", "language", "locale", "currency", "transfer_methods", "total_deposits_requests", "total_net_deposits",
        "total_withdrawals", "total_nav", "total_net_daily_earning", "total_earnings", "latest_earnings_date", "total", "otp_preferred_method", "otp_sms_status", "is_otp_preferred_method_selected", 
        "is_predefined_risk_score_selected", "missing_info", "calendly_url" }
        """
        
        
            
        try:r = requests.get(self.SW_UAT_URL+"profile", headers= self._get_header())
        except:
            self._get_user_token()
            r=requests.get(self.SW_UAT_URL+"profile",headers=self._get_header())
        a=r.json()
        self.user_id=a["meta"]["id"]
        try:self.iban=a["meta"]["iban"]
        except:sleep(0.01)
        try:self.iban=a["meta"]["civil"]
        except:sleep(0.01)
        
        if flag=="N/A": return a
        elif len ((flag.replace(" ","")).split(","))>1:
            list=[]
            for i in ((flag.replace(" ","")).split(",")):
                try:
                    if a["meta"][i]!="":
                        list.append(a["meta"][i])
                    else: list.append (False)
                except:
                    list.append(False)
            return list
        else:
            try:
                if a["meta"][flag]!="":
                    return a["meta"][flag]
                else: return False
            except:
                return False

    
    def _get_user_token(self,email="default"):
        if email!="default": self.email=email

        r = requests.request("GET",
                             self.SW_UAT_URL+"development/get-token?email="+self.email,
                             headers={"Authorization": "#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#"})
        #Script
        a=r.json()
        self.Authorization="Bearer " + a["access_token"]
        if r.status_code==200 or r.status_code==201: return self.Authorization
        else:   return False


    def _get_mobile_number(self,email="default",format="numeric"):
        """
        :format: 'numeric': xxxxxxxx |'text': xxxx xxxx
        """

        if email!="default": self.email=email
        self.Authorization=self._get_user_token(email)
        r = requests.get(self.SW_UAT_URL+"profile", headers= self._get_header())
        a=r.json()
        self.user_id=a["meta"]["id"]
        number= str(a["meta"]["phone_number"]).replace("+965","")
        if format == "text": number=number[0:4] +" "+number[4:len(number)]
        return number
    
    def _get_mobile_number_otp(self):
    
        response = requests.request("GET", 
                                    url = self.SW_UAT_URL+"development/otp/"+str(self.user_id),
                                    headers = {'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'})
        
        print(response.json())
        return (response.json())["otp"]
        
    def _activate_user(self,amount=10000):
        self._get_user_profile()
        r = requests.post(self.SW_UAT_URL+"development/activate/"+self.user_id,
        data=json.dumps({"initial_investment":int(amount)}),
        headers={	
                "Authorization": "#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#",  "Content-Type": "application/json",     "x-locale": "en_US",	"x-version": "1.0", 	"x-platform": "web"})
        print(r.status_code)
        print(r.json())

    def get_email_count(self):
        self.prefix= self.email.replace("@neo.ae","")
        while True:
            if self.prefix[len(self.prefix)-1].isdigit(): self.prefix=self.prefix[:-1]
            else: break
        response = requests.request("GET", 
                            "https://api.nbkcapital-smartwealth.com/api/v2/development/email-count?prefix="+self.prefix, 
                            headers={'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'})
        self.email=self.prefix+ str(int(response.json()["count"]) +1) + "@neo.ae"

        return self.email
    
    def verify_email(self):
        self.auth0_userid=self._get_user_profile("auth0_id")
        response=requests.patch( "https://staging-nbksmartwealth.eu.auth0.com/api/v2/users/"+self.auth0_userid,
                        data={  "email":self.email,
                                "email_verified": "true",
                                "verify_email":"true"},
                        headers={"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1xcHNlck9mQzJyT0l6ZjhxMWdUTyJ9.eyJpc3MiOiJodHRwczovL3N0YWdpbmctbmJrc21hcnR3ZWFsdGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImdhbEtZWlJKbzZ1eUFsZ2ZYZEFZazdvVWRUMmk1cllGQGNsaWVudHMiLCJhdWQiOiJodHRwczovL3N0YWdpbmctbmJrc21hcnR3ZWFsdGguZXUuYXV0aDAuY29tL2FwaS92Mi8iLCJpYXQiOjE2NzYwMTk3NTEsImV4cCI6MTY3ODYxMTc1MSwiYXpwIjoiZ2FsS1laUkpvNnV5QWxnZlhkQVlrN29VZFQyaTVyWUYiLCJzY29wZSI6InJlYWQ6Y2xpZW50X2dyYW50cyBjcmVhdGU6Y2xpZW50X2dyYW50cyBkZWxldGU6Y2xpZW50X2dyYW50cyB1cGRhdGU6Y2xpZW50X2dyYW50cyByZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgY3JlYXRlOnVzZXJzIHJlYWQ6dXNlcnNfYXBwX21ldGFkYXRhIHVwZGF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgZGVsZXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBjcmVhdGU6dXNlcnNfYXBwX21ldGFkYXRhIGNyZWF0ZTp1c2VyX3RpY2tldHMgcmVhZDpjbGllbnRzIHVwZGF0ZTpjbGllbnRzIGRlbGV0ZTpjbGllbnRzIGNyZWF0ZTpjbGllbnRzIHJlYWQ6Y2xpZW50X2tleXMgdXBkYXRlOmNsaWVudF9rZXlzIGRlbGV0ZTpjbGllbnRfa2V5cyBjcmVhdGU6Y2xpZW50X2tleXMgcmVhZDpjb25uZWN0aW9ucyB1cGRhdGU6Y29ubmVjdGlvbnMgZGVsZXRlOmNvbm5lY3Rpb25zIGNyZWF0ZTpjb25uZWN0aW9ucyByZWFkOnJlc291cmNlX3NlcnZlcnMgdXBkYXRlOnJlc291cmNlX3NlcnZlcnMgZGVsZXRlOnJlc291cmNlX3NlcnZlcnMgY3JlYXRlOnJlc291cmNlX3NlcnZlcnMgcmVhZDpkZXZpY2VfY3JlZGVudGlhbHMgdXBkYXRlOmRldmljZV9jcmVkZW50aWFscyBkZWxldGU6ZGV2aWNlX2NyZWRlbnRpYWxzIGNyZWF0ZTpkZXZpY2VfY3JlZGVudGlhbHMgcmVhZDpydWxlcyB1cGRhdGU6cnVsZXMgZGVsZXRlOnJ1bGVzIGNyZWF0ZTpydWxlcyByZWFkOnJ1bGVzX2NvbmZpZ3MgdXBkYXRlOnJ1bGVzX2NvbmZpZ3MgZGVsZXRlOnJ1bGVzX2NvbmZpZ3MgcmVhZDplbWFpbF9wcm92aWRlciB1cGRhdGU6ZW1haWxfcHJvdmlkZXIgZGVsZXRlOmVtYWlsX3Byb3ZpZGVyIGNyZWF0ZTplbWFpbF9wcm92aWRlciBibGFja2xpc3Q6dG9rZW5zIHJlYWQ6c3RhdHMgcmVhZDp0ZW5hbnRfc2V0dGluZ3MgdXBkYXRlOnRlbmFudF9zZXR0aW5ncyByZWFkOmxvZ3MgcmVhZDpzaGllbGRzIGNyZWF0ZTpzaGllbGRzIGRlbGV0ZTpzaGllbGRzIHVwZGF0ZTp0cmlnZ2VycyByZWFkOnRyaWdnZXJzIHJlYWQ6Z3JhbnRzIGRlbGV0ZTpncmFudHMgcmVhZDpndWFyZGlhbl9mYWN0b3JzIHVwZGF0ZTpndWFyZGlhbl9mYWN0b3JzIHJlYWQ6Z3VhcmRpYW5fZW5yb2xsbWVudHMgZGVsZXRlOmd1YXJkaWFuX2Vucm9sbG1lbnRzIGNyZWF0ZTpndWFyZGlhbl9lbnJvbGxtZW50X3RpY2tldHMgcmVhZDp1c2VyX2lkcF90b2tlbnMgY3JlYXRlOnBhc3N3b3Jkc19jaGVja2luZ19qb2IgZGVsZXRlOnBhc3N3b3Jkc19jaGVja2luZ19qb2IgcmVhZDpjdXN0b21fZG9tYWlucyBkZWxldGU6Y3VzdG9tX2RvbWFpbnMgY3JlYXRlOmN1c3RvbV9kb21haW5zIHJlYWQ6ZW1haWxfdGVtcGxhdGVzIGNyZWF0ZTplbWFpbF90ZW1wbGF0ZXMgdXBkYXRlOmVtYWlsX3RlbXBsYXRlcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.whCTVURvdgz7GiwdSXk5OASy8sxDasLv5ukgP46DDsd_EFmsOAMEMujGyl-XsMciQ3NmufpwWdVnETMAcVjfyMYWi7IWi1pPk3SzE-oJzVZC8ZhewcT4FuQzJVzeyKg6AC1gvbACS4h2igN_nAbEkltetorqOSWnK6BQL49kE5NTVGEonaaRIofP-i9qig0bG1xKO3epbKFSRsH5ujtScTnsr8-wonWaZriMsnapVCR0rwjmzFzekRf5pLqgh433-dof5eaOdpTEF4iAEHqrdxxUBZ7nz3pfU9pjUbSnnFnhJflSz5mjWh1gsRlHZxkSe_TIwXqADdVyJRnGobzGBw"})
        print(response.json())
        print(response.status_code)

        if response.status_code!=200 and response.status_code!=201 and response.status_code!=202 and response.status_code!="200": return False
        else: return True

    def upload_ids(self):
        
        header={
                "Authorization":self.Authorization,
                "x-locale":"en_US",
                "x-version":"1.8.68",
                "x-platform":"android"
                        
            }

                
        response=requests.post(
            self.SW_UAT_URL+"profile/primary-id",
            files={'file': open(os.getcwd()+'/BaseClasses/TEST.pdf', 'rb')},
            headers=header)
        print(response.json())
        
        # if response.status_code!=200 and response.status_code!=201 and response.status_code!=202: return False
        
        response=requests.post(
            self.SW_UAT_URL+"profile/primary-id-other-side",
            files={'file': open(os.getcwd()+'/BaseClasses/TEST.pdf', 'rb')},
            headers=header)
        print(response.json())
        # if response.status_code!=200 and response.status_code!=201 and response.status_code!=202: return False

        response=requests.get(self.SW_UAT_URL+"profile/video-id/signed-url?file_name=%s.mp4"%self.user_id,    headers=header)
        print(response.json())
        # if response.status_code!=200 and response.status_code!=201 and response.status_code!=202: return False

        # response=requests.post(
        #     self.SW_UAT_URL+"profile/video-id",
        #     data=json.dumps({'file_name':'%s.mp4'%(self.user_id)}),
        #     headers=header)
        # print(response.json())


        
     
    def withdrawal_otp(self):
        self._get_user_profile()
        url = self.SW_UAT_URL+"development/withdrawal/token/"+self.user_id
        headers = {'Authorization': '#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#'}
        response = requests.request("GET", url, headers=headers)

        b = response.json()
        withdrawal_otp = b['otp']
        print(withdrawal_otp)
        
        return withdrawal_otp

        
        
    def verify_email_and_upload_ids(self):
        if not self.verify_email(): return False
        self.upload_ids()
        self.AndroidGestures.REFRESH()
        return True



    def sign_contract(self):
        r = requests.put(
            self.SW_UAT_URL+"development/"+self.user_id+"/set-contract-signed",
            headers={
                "Authorization":"#76&&&,vSV[@djE&G~rz|]yD.g55432343##^%&%*23&(*&)7sdgdg#%SDFE3545@#3@##%#^#",
                "Content-Type":"application/json",
                "x-locale":"en_US",
                "x-version":"1.0",
                "x-platform":"web"      
            })
    
    
    def get_user_kyc(self,flag="N/A"):
        """
        :flag:
        {
            "sex","first_name","middle_name","family_name","birth_country","nationality","birth_date", "civil_id_number","civil_id_serial","civil_id_expiry_date","passport_number","passport_country",
            "passport_expiry_date","is_customer_same_as_beneficiary","beneficiary_power_of_attorney_enabled","address_country","address_city","address_area","address_street","address_block","address_house",
            "contact_mobile_number","employment_status","employer_type","private_sector_industry","employment_sector","employment_company","employment_department","employment_place","auth_sign_process_financial_transactions",
            "board_membership_existing","investment_reason","trading_experience","income_source","income_annual","liquid_investments_kd","assets_value","transactions_value_past_two_years",
            "financial_sector_years_experience","bank_name","political_position_existing","political_position_is_me","political_position_role","political_position_relationship","political_position_name",
            "us_citizen","tax_payer_identification","us_address_1","us_address_2","pays_taxes_in_other_country","tax_country_1","tax_country_2","tax_country_3","tax_payer_id_1","tax_payer_id_2","tax_payer_id_3"
        } 
        """
        self._get_user_token()
        r = requests.get(self.SW_UAT_URL+"profile/kyc", headers= self._get_header())
        a=r.json()
        self.civil_id_number=a["meta"]["kyc"]["civil_id_number"]
        if flag=="N/A": return a
        else: 
            try:
                return a["meta"]["kyc"][flag]
            except:
                return False

    def approve_by_civil_id(self):
        self.civil_id_number=self.get_user_kyc("civil_id_number")
                    
        response = requests.post(self.SW_UAT_URL+"external/project-connect/dev/profile/approve",
        data=json.dumps({"civil_id_number": self.civil_id_number}),
        headers={"Content-Type":"application/json"}
        )
        if response.status_code!=200 and response.status_code!=201 and response.status_code!=202: return False

        
class ApplicationHelpers:
    def __init__(self,driver):
        self.driver = driver
        self.AppiumGestures=AppiumActions(self.driver)
        

        self.Report=Reporting(self.driver,"Application Helpers")


    def loading_stuck(self):
        count=0
        while True:
            try:
                self.AppiumGestures.get_element(IDS.Loading.Dots)
                count=count+1
            except: return False
            if count==100:
                return True
    
    def map_elements(self,class1, class2):
        mapped_elements = {}
        for element in dir(class1):
            if not element.startswith("__"):
                class1_attr = getattr(class1, element)
                class2_attr = getattr(class2, element, None)
                if class2_attr:
                    mapped_elements[class1_attr] = class2_attr
        return mapped_elements
    
    def map_attributes(self,class1, class2):
        mapped_elements = {}
        for class1_attr in dir(class1):
            if not class1_attr.startswith('__'):
                class1_attr_val = getattr(class1, class1_attr)
                if class1_attr_val in dir(class2):
                    class2_attr = getattr(class2, class1_attr_val)
                    mapped_elements[class1_attr_val] = class2_attr
                elif class1_attr in dir(class2):
                    class2_attr = getattr(class2, class1_attr)    
                    mapped_elements[class1_attr_val] = class2_attr
        return mapped_elements

    
    def test_screen_localization(self,screen):
        ids,localization=screen
        element_map=self.map_attributes(ids,localization)
        # Loop through element_map and compare corresponding element texts
        for ids_element, localization_element in element_map.items():
            try:
                element=self.AppiumGestures.wait_for_element(ids_element,2)
                if element.text != localization_element:
                    self.Report.report_testcase(False,"N/A","N/A",element.text,localization_element)
            except:
                pass
# A=APIS(Credentials.email)
# A._get_mobile_number()
# A._get_mobile_number_otp()