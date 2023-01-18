import requests
from GetProfileAPIReturnID import GetProfileAPIReturnID
from GetTokenAPI import GetTokenAPI
from Constants_Technical_Variables import Constants


class User_Info():
    def __init__(self,Email="N/A"):
        if Email !="N/A" :
            self.Email=Email
            self.UserAuth=GetTokenAPI(Email)
            self.User_ID=GetProfileAPIReturnID(self.UserAuth)
        else:
            print ("ERROR!!!!! EMAIL IS NOT SAVED!!!")

    def KYCInfoAPI(self):
         
        API_Name="GET KYC"
        for i in range(0,2):
            r = requests.get(
                Constants.SW_UAT_URL+"profile/kyc",
            
                headers={
                    "Authorization":self.UserAuth,
                    "x-locale":"en_US",
                    "x-version":"1.8.68",
                    "x-platform":"android",
                    "Content-Type":"application/json"}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            break
        return Response
    
    def KYCInfoAPI_ReturnJSON(self):
         
        API_Name="GET KYC"
        for i in range(0,2):
            r = requests.get(
                Constants.SW_UAT_URL+"profile/kyc",
            
                headers={
                    "Authorization":self.UserAuth,
                    "x-locale":"en_US",
                    "x-version":"1.8.68",
                    "x-platform":"android",
                    "Content-Type":"application/json"}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            break
        return a

    
    
    def ProfileInfoAPI(self):
    
        API_Name="GET Profile"
        for i in range(0,2):
            r = requests.get(
                Constants.SW_UAT_URL+"profile",
            
                headers={
                    "Authorization":self.UserAuth,
                    "x-locale":"en_US",
                    "x-version":"1.8.68",
                    "x-platform":"android",
                    "Content-Type":"application/json"}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            break
        return Response  

    def ProfileInfoAPI_ReturnJSON(self):
    
        API_Name="GET Profile"
        for i in range(0,2):
            r = requests.get(
                Constants.SW_UAT_URL+"profile",
            
                headers={
                    "Authorization":self.UserAuth,
                    "x-locale":"en_US",
                    "x-version":"1.8.68",
                    "x-platform":"android",
                    "Content-Type":"application/json"}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            break
        return a  




    def StatusInfoAPI(self):
        API_Name="GET Status"
        for i in range(0,2):
            r = requests.get(
                Constants.SW_UAT_URL+"profile/status",
            
                headers={
                    "Authorization":self.UserAuth,
                    "x-locale":"en_US",
                    "x-version":"1.8.68",
                    "x-platform":"android",
                    "Content-Type":"application/json"}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            break
        return Response  
    
    def StatusInfoAPI_ReturnJSON(self):
        API_Name="GET Status"
        for i in range(0,2):
            r = requests.get(
                Constants.SW_UAT_URL+"profile/status",
            
                headers={
                    "Authorization":self.UserAuth,
                    "x-locale":"en_US",
                    "x-version":"1.8.68",
                    "x-platform":"android",
                    "Content-Type":"application/json"}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            break
        return a  
    
    

    def PortfolioInfoAPI(self):
        
        API_Name="GET Portfolio"
        for i in range(0,2):
            r = requests.get(
                Constants.SW_UAT_URL+"portfolio",
            
                headers={
                    "Authorization":self.UserAuth,
                    "x-locale":"en_US",
                    "x-version":"1.8.68",
                    "x-platform":"android",
                    "Content-Type":"application/json"}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            break
        return Response
    
    
