from GetStartedScreen import GetStartedScreen_SignUp
from HowWouldYouLikeToGetStarted import HowWouldYouLikeToGetStartedText
from InvestmentProposal import InvestmentProposal
from InvestmentType import InvestmentType
from PredefinedScreen import PredefinedScreen
from Questionnaire import Questionnaire
from SignUpScreen import SignUpScreenTest


def SignUpFlow(driver,ReportDriver,Credentials,JSON,User_Type="etf",RiskScore="5",OnboardingFlow= "predefined"):
    GetStartedScreen_SignUp(driver,ReportDriver)
    HowWouldYouLikeToGetStartedText(driver,ReportDriver,OnboardingFlow)
    if OnboardingFlow=="Predefined" or OnboardingFlow== "predefined" :
        PredefinedScreen(driver,ReportDriver,RiskScore)
    elif OnboardingFlow=="Customized" or OnboardingFlow=="customized" :
        Questionnaire(driver,ReportDriver,RiskScore,JSON)
    try:InvestmentType(driver,ReportDriver,User_Type)
    except:print("Investment type screen is not shown...")
    InvestmentProposal(driver,ReportDriver,User_Type)
    Credentials=SignUpScreenTest(driver,ReportDriver,Credentials)
    
    return Credentials