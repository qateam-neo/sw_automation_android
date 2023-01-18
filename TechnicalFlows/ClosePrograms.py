import os
import signal
import subprocess
from colorama import Fore
import wmi
import socket, errno


def ClosePrograms():
    f = wmi.WMI()
    
    print("Test is Done, Closing Programs...")

    # Iterating through all the running processes
    for process in f.Win32_Process():
        if "TestProjectAgent.exe" == process.Name or "testproject-agent.exe"==process.Name:
            process.Terminate()
            print(Fore.GREEN+"\tTest Project Agent terminated successfully!"+Fore.RESET)
            
    
        if "qemu-system-x86_64.exe" == process.Name:
            process.Terminate()
            print(Fore.GREEN+"\tEmulator terminated successfully!"+Fore.RESET)
            
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
    
    
    if Appium_Running:
        command = "netstat -ano | findstr 4723"
        c = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        stdout, stderr = c.communicate()
        try: 
            pid = int(stdout.decode().strip().split(' ')[-1])
            os.kill(pid, signal.SIGTERM)
            print(Fore.GREEN+"\tAppiumm Server terminated successfully!"+Fore.RESET)
        except:
            print(Fore.RED+"Couldn't close Appium Server"+Fore.RESET)