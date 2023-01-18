import json
import requests
from GetProfileAPIReturnID import GetProfileAPIReturnID
from GetTokenAPI import GetTokenAPI
from ManualReport import ReportResultsAPICollection

class Admin_APIs:
    
    
    
    def __init__(self,AdminAuthorization="N/A",User_ID="N/A",Email="N/A") :
        if User_ID == "N/A" and Email=="N/A" :
            with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BaseClasses\\KYC_3.0_JSON_File.json") as file:
                JSON=json.load(file)
            self.User_ID =JSON["TechnicalVariables"]["User_ID"]
        elif User_ID == "N/A" and Email !="N/A":
            Auth=GetTokenAPI(Email)
            self.User_ID=GetProfileAPIReturnID(Auth,None,Email,"Password123")
        elif User_ID != "N/A" and Email =="N/A":
            self.User_ID=User_ID
        if AdminAuthorization != "N/A":
            self.AdminAuthorization = str(AdminAuthorization)
        
        
        
    def ValidateAdminAuth(self,AdminAuthorization):

        API_Name="Validate Admin Authorization Bearer API"
        for i in range(0,2):
    
            r = requests.get(
                "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile?user_filter_type=auto_approved&offset=0&limit=5&investment_type=all&q=",
            
                headers ={
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Authorization': AdminAuthorization,
                    'Connection': 'keep-alive',
                    'ContentType': 'application/json',
                    'Origin': 'https://admin.nbkcapital-smartwealth.com',
                    'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                    'X-Locale': 'en_US',
                    'X-Platform': 'web',
                    'X-Version': '2.0',
                    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"'
                    }
            )
            
            #Script
            
            # a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            if StatusCode=="200" or StatusCode=="201" or StatusCode==201 or StatusCode==200:
                self.AdminAuthorization=AdminAuthorization.strip()
                return True
            
            elif "authorization" in Response.lower():
                return False
            
            else : return "Not Authorization"
        
    
    def Info_API (self):

        print("User Admin Info API:")

        
        API_Name="GET User Admin Info"
        r = requests.get(
            "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/info" % str(self.User_ID),
        
        
            headers ={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
                }
        )
        
        #Script
        
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text
        return Response
        

    def Address_API(self):
        print("User Admin Address API:")

        
        API_Name="GET User Admin Address"
        r = requests.get(
            "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/address" % self.User_ID,
        
            headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
        )
        
        #Script
        
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text
        return Response


    def Summary_API (self):
        
            print("User Admin Summary API:")

            
            API_Name="GET User Admin Summary"
            r = requests.get(
                "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/summary" % self.User_ID,
            
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            return Response


    def Bank_API (self):
        
            print("User Admin Bank API:")

            
            API_Name="GET User Admin Bank"
            r = requests.get(
                "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/bank" % self.User_ID,
            
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            return Response

    
    def KYC_CID_Status_API (self):
        
            print("User Admin KYC CID Status API:")

            
            API_Name="GET User Admin KYC CID Status"
            r = requests.get(
                "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/project-connect/%s/kyc-cid-status" % str(self.User_ID),
            
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            return Response


    def Steps_API (self):
        
            print("User Admin Steps API:")

            
            API_Name="GET User Admin Steps"
            r = requests.get(
                "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/steps" % self.User_ID,
            
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            return Response


    def ETF_Portfolio_API (self):
        
            print("User Admin ETF Portfolio API:")

            
            API_Name="GET User Admin ETF Portfolio"
            r = requests.get(
                "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/portfolios?investment_type=etf" % self.User_ID,
            
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            return Response


    def MMF_Portfolio_API (self):
        
            print("User Admin MMF Portfolio API:")

            
            API_Name="GET User Admin MMF Portfolio"
            r = requests.get(
                "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/portfolios?investment_type=mmf" % self.User_ID,
            
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            return Response

    
    def Funds_API (self):
        
            print("User Admin Funds API:")

            
            API_Name="GET User Admin Funds"
            r = requests.get(
                "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/funds" % self.User_ID,
            
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            return Response


    def Deposits_API (self):
        
            print("User Admin Deposits API:")

            
            API_Name="GET User Admin Deposits"
            r = requests.get(
                "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/deposits" % self.User_ID,
            
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            return Response

    
    def Withdrawals_API (self):
        
            print("User Admin Withdrawals API:")

            
            API_Name="GET User Admin Withdrawals"
            r = requests.get(
                "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/withdrawals" % self.User_ID,
            
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            return Response

    
    def CivilIDs_API(self):
        
        print("Get User Civil IDs API:")
        
        
        API_Name="GET Front Civil IDs API"
        r = requests.get(
            "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/document?document_name=civil_id_first" % self.User_ID,
        
            headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
        )
        
        #Script
        
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text
            
        
        API_Name="GET Second Civil IDs API"
        r = requests.get(
            "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/document?document_name=civil_id_second" % self.User_ID,
        
            headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
        )
        
        #Script
        
        a=r.json()
        StatusCode=str(r.status_code)
        Response=r.text


    def Contract_API (self):
        
            print("User Admin Contract API:")

            
            API_Name="GET User Admin Contract"
            r = requests.get(
                "https://sw-internal-uat.nbkcapital-smartwealth.com/api/v2/admin/profile/%s/document?document_name=signed_contract" % self.User_ID,
            
                headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': self.AdminAuthorization,
                'Connection': 'keep-alive',
                'ContentType': 'application/json',
                'Origin': 'https://admin.nbkcapital-smartwealth.com',
                'Referer': 'https://admin.nbkcapital-smartwealth.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'X-Locale': 'en_US',
                'X-Platform': 'web',
                'X-Version': '2.0',
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
}
            )
            
            #Script
            
            a=r.json()
            StatusCode=str(r.status_code)
            Response=r.text
            return Response


