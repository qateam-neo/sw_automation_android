
import json
import SystemPathBackend
from ConfigureDevices import ConfigureDeviceEmulator
with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
# Load its content and make a new dictionary
    JSON=json.load(file)
    
##################################################################
Credentials = { 
    "FirstName":"test",
    "LastName":"test",
    "Password": "Password123",
    "MobileNumber":"5900 0098",
    "RiskScore":"5",
    "User_Type":"Islamic",
    "BuildName":JSON["TechnicalVariables"]["BuildName"]
}
##################################################################


ConfigureDeviceEmulator(None,Credentials)