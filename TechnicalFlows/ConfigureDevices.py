import os
import subprocess
import sys
from appium import webdriver
from colorama import Fore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import wmi

import time
from Intensive_Tests.helpers import Reporting
from ManualReport import ReportResults


def ConfigureDevice(ReportDriver,Credentials):
    
    # desired_caps = {
    #     "deviceName": "Galaxy A52",
    #     "platformName": "Android",
    #     "UDID":"R58R33D0FQL",
    #     "version" : "11",
    #     "appPackage": "neo.nbkc.smartwealth.demo",
    #     "appActivity":"com.nbkcapitalsmartwealth.app.splash.SplashActivity",
    #     #"app": "",
    #     "realDevice": True
    # }
    
    desired_caps = {
        "deviceName": "TECNO CAMON 16",
        "platformName": "Android",
        "UDID":"0602125126011433",
        "version" : "11",
        "appPackage": "neo.nbkc.smartwealth.demo",
        "appActivity":"com.nbkcapitalsmartwealth.app.splash.SplashActivity",
        "realDevice": True
    }
    count=0
    while True:
        try:
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            break
        except:
            print("Couldn't connect to Device\nMake sure you have Appium Server up and running...")
        if count==0:
            os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\CMD Commands\\ADBRestart.bat")
            count=count+1
    TestCase="Configure Device and Open Application"
    ActualText="N/A"
    ExpectedText="N/A"
    
    Status=True
    
    ReportResults(ReportDriver,driver,Status,TestCase,ActualText,ExpectedText)

    print("App Started")
    return driver


def ConfigureDeviceNoApp(ReportDriver,Credentials):
    
    desired_caps = {
        "deviceName": "Galaxy A52",
        "platformName": "Android",
        "UDID":"R58R33D0FQL",
        "version" : "11",
        "realDevice": True
    }
    
    # desired_caps = {
    #     "deviceName": "TECNO CAMON 16",
    #     "platformName": "Android",
    #     "UDID":"0602125126011433",
    #     "version" : "11",
    #     "realDevice": True
    # }
        
    count=0
    while True:
        try:
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            break
        except:
            print("Couldn't connect to Device\nMake sure you have Appium Server up and running...")
        if count==0:
            os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\CMD Commands\\ADBRestart.bat")
            count=count+1
        
    TestCase="Configure Device and Connect Session"
    ActualText="N/A"
    ExpectedText="N/A"
    
    Status=True
    
    ReportResults(ReportDriver,driver,Status,TestCase,ActualText,ExpectedText)

    print("Session Connected")
    return driver


def ConfigureDeviceEmulatorNoApp(ReportDriver,Credentials):
     
    TestCase="Configure Device and Connect Session"
    ActualText="N/A"
    ExpectedText="N/A"
    Status=True
    count=0
    UDID="emulator-5556"
        
    while count<22:
        
        
        desired_caps = {
            "deviceName": "Android Emulator",
            "platformName": "Android",
            "udid":UDID,
            "version" : "12",
            "newCommandTimeout":120	
        }
        try:
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            count=1000
            Failed = False
            break
        except:
            print("Couldn't connect to Device\nMake sure you have Appium Server up and running...")
            Failed=True
            count=count+1


        if count==1 and Failed:
            returned_text = subprocess.check_output("adb devices", shell=True, universal_newlines=True)
            a=[]
            for e in returned_text.split("\n"):
                if "emulator" in e:
                    UDIDSection=e.split("\t")
                    break
            for s in UDIDSection:
                if "emulator" in s:
                    UDID=s[0:13]
            print(UDID)
            os.popen("adb -s %s shell am start -n io.appium.settings/io.appium.settings.Settings"%UDID)

        

    ReportResults(ReportDriver,driver,Status,TestCase,ActualText,ExpectedText)
    print("Session Connected")
    
    # try:
    #     WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/skipButton")))
    # except:
    #     print("Can't find Get Started Screen (Slow Emulator)")
    return driver



def ConfigureDeviceEmulator(ReportDriver,Credentials):
    
    TestCase="Configure Device and Connect Session"
    ActualText="N/A"
    ExpectedText="N/A"
    Status=True
    count=0
    UDID="emulator-5554"
        
    while count<22:
        
        
        desired_caps = {
            "deviceName": "Android Emulator",
            "platformName": "Android",
            "udid":UDID,
            "version" : "13",
            # "app": "C:\\Users\\Roy Braish\\Roy Personal\\SW Android Builds\\"+Credentials["BuildName"],
            "appPackage": "neo.nbkc.smartwealth.demo",
            "appActivity":"com.nbkcapitalsmartwealth.app.splash.SplashActivity",
            "newCommandTimeout":120	
        }
        if count !=0 and count %2 == 0 and Failed:
        
            desired_caps = {
                "deviceName": "Android Emulator",
                "platformName": "Android",
                "udid":UDID,
                "version" : "13",
                # "app": "C:\\Users\\Roy Braish\\Roy Personal\\SW Android Builds\\"+Credentials["BuildName"],
                "appPackage": "neo.nbkc.smartwealth.demo",
                "appActivity":"com.nbkcapitalsmartwealth.app.splash.SplashActivity",
                "newCommandTimeout":120	
            }
        try:
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            count=1000
            Failed = False
            break
        except:
            print("Couldn't connect to Device\nMake sure you have Appium Server up and running...")
            Failed=True
            count=count+1


        if count==1 and Failed:
            returned_text = subprocess.check_output("adb devices", shell=True, universal_newlines=True)
            a=[]
            for e in returned_text.split("\n"):
                if "emulator" in e and "device" in e:
                    UDIDSection=e.split("\t")
                    break
            for s in UDIDSection:
                if "emulator" in s:
                    UDID=s[0:13]
            print(UDID)
            os.popen("adb -s %s shell am start -n io.appium.settings/io.appium.settings.Settings"%UDID)


        if count==10 and Failed:
            returned_text = subprocess.check_output("adb devices", shell=True, universal_newlines=True)
            if "offline" in returned_text:
                subprocess.check_output("adb kill-server", shell=True, universal_newlines=True)
                subprocess.check_output("adb start-server", shell=True, universal_newlines=True)
                subprocess.check_output("adb devices", shell=True, universal_newlines=True)


        if count==16 and Failed:
            f = wmi.WMI()
            for process in f.Win32_Process():
                if "qemu-system" in process.Name:
                    # print("Emulator is Running")
                    process.Terminate()
                    break
            t=10
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer+" Seconds till the emulator is shut down...", end="\r")
                time.sleep(1)
                t -= 1            
            os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\CMD Commands\\Emulator.bat")  
            
            ERASE_LINE = '\x1b[2K' 
            sys.stdout.write(ERASE_LINE)             
            
            t=70
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print("The code will start in "+timer+" Seconds...", end="\r")
                time.sleep(1)
                t -= 1   
                            
            ERASE_LINE = '\x1b[2K' 
            sys.stdout.write(ERASE_LINE)             

        
    ReportResults(ReportDriver,driver,Status,TestCase,ActualText,ExpectedText)
    print("Session Connected")
    try: WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "com.android.permissioncontroller:id/permission_allow_button"))).click()
    except: print("Notification pop up is not shown")
    try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/skipButton")))
    except:
        print("Can't find Get Started Screen (Slow Emulator)")

    return driver

class Appiumdriver:
    def __init__(self):
        self.UDID="emulator-5554"
        self.remote_url="http://127.0.0.1:4724/wd/hub"
        self.desired_caps = {
            "deviceName": "Android Emulator",
            "platformName": "Android",
            "udid":self.UDID,
            "version" : "13",
            # "app": "C:\\Users\\Roy Braish\\Roy Personal\\SW Android Builds\\"+Credentials["BuildName"],
            "appPackage": "neo.nbkc.smartwealth.demo",
            "appActivity":"com.nbkcapitalsmartwealth.app.splash.SplashActivity",
            "newCommandTimeout":120	
        }
        self.desired_caps_no_app = {
            "deviceName": "Android Emulator",
            "platformName": "Android",
            "udid":self.UDID,
            "version" : "13",
            "newCommandTimeout":120	
        }

        self.Report=Reporting(None,"Configure Device and Connect Session")


    def _check_udid_force_start_appium(self):
        returned_text = subprocess.check_output("adb devices", shell=True, universal_newlines=True)
        a=[]
        for e in returned_text.split("\n"):
            if "emulator" in e and "device" in e:
                UDIDSection=e.split("\t")
                for s in UDIDSection:
                    if "emulator" in s:
                        UDID=s[0:13]
                        break
        print(UDID)
        self.UDID=UDID
        os.popen("adb -s %s shell am start -n io.appium.settings/io.appium.settings.Settings"%UDID)

    def _restart_adb(self):
        returned_text = subprocess.check_output("adb devices", shell=True, universal_newlines=True)
        if "offline" in returned_text:
            subprocess.check_output("adb kill-server", shell=True, universal_newlines=True)
            subprocess.check_output("adb start-server", shell=True, universal_newlines=True)
            subprocess.check_output("adb devices", shell=True, universal_newlines=True)

    def _restart_emulator(self):
        f = wmi.WMI()
        for process in f.Win32_Process():
            if "qemu-system" in process.Name:
                # print("Emulator is Running")
                process.Terminate()
                break
        t=10
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer+" Seconds till the emulator is shut down...", end="\r")
            time.sleep(1)
            t -= 1            
        os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\CMD Commands\\Emulator.bat")  
        
        ERASE_LINE = '\x1b[2K' 
        sys.stdout.write(ERASE_LINE)             
        
        t=70
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("The code will start in "+timer+" Seconds...", end="\r")
            time.sleep(1)
            t -= 1   
                        
        ERASE_LINE = '\x1b[2K' 
        sys.stdout.write(ERASE_LINE)             

    def _analyze_screen_errors(self):
        try: WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "com.android.permissioncontroller:id/permission_allow_button"))).click()
        except: print("Notification pop up is not shown")
        
        try:WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/skipButton")))
        except:print("Can't find Get Started Screen (Slow Emulator)")

    def create_driver_open_app(self):
        
        self.testcase="Configure Device and Connect Session"
        count=0
        while count<22:
            try:
                self.driver = webdriver.Remote(self.remote_url, self.desired_caps)
                count=1000
                Failed = False
                break
            except:
                print("Couldn't connect to Device\nMake sure you have Appium Server up and running...")
                Failed=True
                count=count+1


            if count==1 and Failed:self._check_udid_force_start_appium()

            if count==10 and Failed:self._restart_adb()


            if count==16 and Failed:self._restart_emulator()
        self.Report.report_testcase(True,self.testcase,"N/A")   
        print("Session Connected")
        self._analyze_screen_errors()
        

        return self.driver
    
    def create_driver_no_app(self):
        
        self.testcase="Connect Session"
        count=0
        while count<22:
            try:
                self.driver = webdriver.Remote(self.remote_url, self.desired_caps_no_app)
                count=1000
                Failed = False
                break
            except:
                print("Couldn't connect to Device\nMake sure you have Appium Server up and running...")
                Failed=True
                count=count+1


            if count==1 and Failed:self._check_udid_force_start_appium()

            if count==10 and Failed:self._restart_adb()


            if count==16 and Failed:self._restart_emulator()
        self.Report.report_testcase(True,self.testcase,"N/A")   
        print("Session Connected")        

        return self.driver