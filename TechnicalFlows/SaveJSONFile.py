import json


def SaveJSONFile(JSONFileVariable,NewValue):
    JSONFileVariable=JSONFileVariable.split(",")
    #JSONFileVariable=["x"]["y"]
    # print(JSONFileVariable)
    # print(JSONFileVariable[0])
    # print(JSONFileVariable[1])

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    # print(json_object)
    
    json_object[JSONFileVariable[0]][JSONFileVariable[1]] = NewValue

    a_file = open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
    