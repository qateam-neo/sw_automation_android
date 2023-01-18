import os
from re import sub
import subprocess
import sys
from time import sleep
import time
from colorama import Fore
from Constants_Technical_Variables import Constants
# Import module
if Constants.Platform == "windows":import wmi
import socket, errno



def CheckAndRunExternalPrograms():
    
    print("Launching Needed Programs to run the Test ...")
    # Initializing the wmi constructor
    f = wmi.WMI()
    
    # Check if appium server is running and run it if not
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind(("127.0.0.1", 4723))
        Appium_Running = False
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            Appium_Running = True
        else:
            Appium_Running = False
            print("something else raised the error on Port for Appium server, error exception: ")
            print(e)

    s.close()    # Iterating through all the running processes
    
    

    # Check if emulator is running and run it if not
    Emulator_Running = False
    # Iterating through all the running processes
    for process in f.Win32_Process():
        if "qemu-system-x86_64.exe" == process.Name:
            # print("Emulator is Running")
            Emulator_Running = True
            break
    
        
    # Check if Test project agent is running and run it if not
    Agent_Running = False
    # Iterating through all the running processes
    for process in f.Win32_Process():
        if "TestProjectAgent.exe" == process.Name or "testproject-agent.exe"==process.Name:
            # print("Test Project Agent is Running")
            Agent_Running = True
            break
        
    if Appium_Running == True and Agent_Running == True and Emulator_Running == True: #They are already running no need to sleep more than 10 seconds
        print (Fore.GREEN+"\tTest Project Agent, Emulator, and Appium server GUI are all Running..."+Fore.RESET)
        os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\CMD Commands\\ADBRestart.bat")
        t=8
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("The code will start in "+timer+" Seconds...", end="\r")
            time.sleep(1)
            t -= 1
    
    
    else:

                  
        if Appium_Running == False:
            print(Fore.YELLOW+"\tAppium server GUI is not Running yet..."+Fore.RESET)
            os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\CMD Commands\\OpenAppiumServer.bat")
        else:
            print(Fore.GREEN+"\tAppium server GUI is already Running... "+Fore.RESET)

        
        if Emulator_Running == False:
            print(Fore.YELLOW+"\tEmulator is not Running yet..."+Fore.RESET)
            os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\CMD Commands\\Emulator.bat")  
        else:
            print(Fore.GREEN+"\tEmulator is already Running... "+Fore.RESET)
            
        #Sleep 35 seconds until emulator is on
        t=35
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Please wait "+timer+" seconds for the emulator to run...", end="\r")
            time.sleep(1)
            
            t -= 1
            
        ERASE_LINE = '\x1b[2K' 
        sys.stdout.write(ERASE_LINE)                         

        if Agent_Running == False:
            print(Fore.YELLOW+"\tTest Project Agent is not Running yet..."+Fore.RESET)
            os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\CMD Commands\\ReportDriver.bat")
        else:
            print(Fore.GREEN+"\tTest Project Agent is already Running... "+Fore.RESET)


        t=45
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Please wait "+timer+" seconds for the Test Projoect Agenet to run...", end="\r")
            time.sleep(1)
            
            t -= 1
            
        ERASE_LINE = '\x1b[2K' 
        sys.stdout.write(ERASE_LINE)       
        
        # #Sleep 60 seconds until emulator is on
        # t=20
        # while t:
        #     mins, secs = divmod(t, 60)
        #     timer = '{:02d}:{:02d}'.format(mins, secs)
        #     print("Please wait "+timer+" seconds for the Code to run...", end="\r")
        #     time.sleep(1)
        #     t -= 1
            
        # ERASE_LINE = '\x1b[2K' 
        # sys.stdout.write(ERASE_LINE) 
        
        
        os.startfile("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\CMD Commands\\ADBRestart.bat")
        print(Fore.YELLOW+"Waiting for the programs to launch and settle..." + Fore.RESET) 


def RunProgramsonMAC():
    # os.system("start cmd /c adb devices")
    import appscript

    appscript.app('Terminal').do_script('cd / && cd Users\mobile\Library\Android\sdk\emulator && ./emulator -avd Pixel_4_XL_API_33 -no-boot-anim -gpu on')
    subprocess.run(["start", "cmd", "/K", "cd / && cd Users\mobile\Library\Android\sdk\emulator && ./emulator -avd Pixel_4_XL_API_33 -no-boot-anim -gpu on"], shell=True)    
    subprocess.run(["start",  "cmd", "/K", "appium -a 127.0.0.1 -p4723 --allow-cors --session-override --bootstrap-port 4723 --relaxed-security"], shell=True)
    # os.popen("call cd C:\Users\Roy Braish\AppData\Local\Android\Sdk\emulator && ./emulator -avd Pixel_4_XL_API_33 -no-boot-anim -gpu on")
    # os.popen("call appium -a 127.0.0.1 -p4723 --allow-cors --session-override --bootstrap-port 4723 --relaxed-security")
