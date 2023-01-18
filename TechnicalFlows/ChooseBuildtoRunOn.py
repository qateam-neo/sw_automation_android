import json
import os
import natsort

def ChooseBuild():
    
    ChooseBuild=False
    Ans=input("Would you like to choose a build? (y/n): ")
    while ChooseBuild==False:
        if str(Ans).lower() == "y" or str(Ans).lower() == "yes":
            ChooseBuild=True
            break
        elif str(Ans).lower() == "n" or str(Ans).lower() == "no":
            ChooseBuild==False
            with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
                # Load its content and make a new dictionary
                JSON=json.load(file)
            BuildName=JSON["TechnicalVariables"]["BuildName"]
            break
        else:
            print("Try another Input")
    

    if ChooseBuild:
        X=os.listdir('C:\\Users\\Roy\\OneDrive\\Desktop\\Roy Personal\\SW Android Builds')
        Builds=natsort.natsorted(X)

        count =1
        for Build in Builds:
            print("\t%s- "%str(count)+Build)    
            count += 1

        BuildIndex=input("Choose Build (Ex. 1, 2, 3, ...): ")
        count =1
        for Build in Builds:
            if str(count) == BuildIndex:
                BuildName=Build
                break
            count += 1
        

    print("Build Name: "+BuildName)   
    return BuildName