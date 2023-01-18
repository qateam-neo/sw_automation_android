

predefined_risk_score_boundaries = {
    1: {
        'max': {
            'risk_score': 7,
            'case_id': '6099'
            
        },
        'min': {
            'risk_score': 3,
            'case_id': '6100'
        }
    },
    2: {
        'max': {
            'risk_score': 1,
            'case_id': '6119'

        },
        'min': {
            'risk_score': 1,
            'case_id': '6120'
        }
    }
}

predefined_config = {
    1: {
        1: {
            'risk_score': 3,
            'title': 'You have selected a conservative investment plan'
        },
        2: {
            'risk_score': 5,
            'title': 'You have selected a balanced investment plan'
        },
        3: {
            'risk_score': 7,
            'title': 'You have selected a growth investment plan'
        }
    },
    2: {
        3: {
            'risk_score': 1,
            'title': 'You have selected a growth investment plan'
        }
    }
}



class IDS:
    
    class Loading:
        Dots="neo.nbkc.smartwealth.demo:id/animationView"
    
    class GetStartedScreen:
        title="neo.nbkc.smartwealth.demo:id/titleLabel"
        description="neo.nbkc.smartwealth.demo:id/descriptionLabel"
        
        get_started_button= "neo.nbkc.smartwealth.demo:id/skipButton"
        login_button="neo.nbkc.smartwealth.demo:id/loginButton"
        change_language_button= "neo.nbkc.smartwealth.demo:id/btnChangeLanguage"
                
    
    class how_would_you_like_to_get_started_screen:
        title="neo.nbkc.smartwealth.demo:id/questionTextView"
        description=("neo.nbkc.smartwealth.demo:id/descriptionTextView",0)

        customized_title=("neo.nbkc.smartwealth.demo:id/titleTextView",0)
        customized_description=("neo.nbkc.smartwealth.demo:id/descriptionTextView",1)
        customized_button=("neo.nbkc.smartwealth.demo:id/recyclerCardView",0)

        predefined_title=("neo.nbkc.smartwealth.demo:id/titleTextView",1)
        predefined_description=("neo.nbkc.smartwealth.demo:id/descriptionTextView",2)
        predefined_button=("neo.nbkc.smartwealth.demo:id/recyclerCardView",1)

        continue_button="neo.nbkc.smartwealth.demo:id/continueButton"
    
    class predefined_options_screen:
        title="neo.nbkc.smartwealth.demo:id/questionTextView"
        
        conservative_title=("neo.nbkc.smartwealth.demo:id/titleTextView",0)
        conservative_description=("neo.nbkc.smartwealth.demo:id/descriptionTextView",0)
        conservative_button=("neo.nbkc.smartwealth.demo:id/recyclerCardView",0)

        balanced_title=("neo.nbkc.smartwealth.demo:id/titleTextView",1)
        balanced_description=("neo.nbkc.smartwealth.demo:id/descriptionTextView",1)
        balanced_button=("neo.nbkc.smartwealth.demo:id/recyclerCardView",1) 

        growth_title=("neo.nbkc.smartwealth.demo:id/titleTextView",2)
        growth_description=("neo.nbkc.smartwealth.demo:id/descriptionTextView",2)
        growth_button=("neo.nbkc.smartwealth.demo:id/recyclerCardView",2)
    
        not_sure_button="neo.nbkc.smartwealth.demo:id/tvLink"
        continue_button="neo.nbkc.smartwealth.demo:id/continueButton"
        
        
    class questionnaire:
        select_option="neo.nbkc.smartwealth.demo:id/optionTextView"
        question="neo.nbkc.smartwealth.demo:id/questionTextView"
    
    class investment_type_screen:
        title="neo.nbkc.smartwealth.demo:id/labelTitle"
        description="neo.nbkc.smartwealth.demo:id/tvSubTitle"

        etf_title=("neo.nbkc.smartwealth.demo:id/tvTitle",0)
        etf_description=("neo.nbkc.smartwealth.demo:id/tvDesc",0)
        etf_tag=("neo.nbkc.smartwealth.demo:id/tvTag",0)
        etf_option=("neo.nbkc.smartwealth.demo:id/layoutInfo",0)

        islamic_title=("neo.nbkc.smartwealth.demo:id/tvTitle",1)
        islamic_description=("neo.nbkc.smartwealth.demo:id/tvDesc",1)
        islamic_tag=("neo.nbkc.smartwealth.demo:id/tvTag",1)
        islamic_option=("neo.nbkc.smartwealth.demo:id/layoutInfo",1)

        Continue="neo.nbkc.smartwealth.demo:id/btnContinue"
    
    class islamic_popup:
        description="neo.nbkc.smartwealth.demo:id/tvMessage"
        
        continue_button="neo.nbkc.smartwealth.demo:id/btnContinue"
        select_another_plan_button="neo.nbkc.smartwealth.demo:id/tvSelectPlan"
        
        

    class investment_proposal_screen:
        
        title="neo.nbkc.smartwealth.demo:id/titleTextView"
        expand_description_button="neo.nbkc.smartwealth.demo:id/expandButton"
        description="neo.nbkc.smartwealth.demo:id/descriptionTextView"

        risk_score_text="neo.nbkc.smartwealth.demo:id/textViewHeader"
        risk_score_increase="neo.nbkc.smartwealth.demo:id/increaseButton"
        risk_score_decrease="neo.nbkc.smartwealth.demo:id/decreaseButton"

        percentages_texts="neo.nbkc.smartwealth.demo:id/holdingTextView"
        percentages="neo.nbkc.smartwealth.demo:id/percentageTextView"
        
        expand_historical_button="neo.nbkc.smartwealth.demo:id/historicalChartButton"
        growth_per_annual="neo.nbkc.smartwealth.demo:id/chartDescriptionTextView"
        
        start_investing_button="neo.nbkc.smartwealth.demo:id/accountButton"
        
    class KYC:
        class Personal_Info:
            Fields="neo.nbkc.smartwealth.demo:id/tvTitle"
            Inputs="neo.nbkc.smartwealth.demo:id/etValue"

class Localization_Onboarding:
    
    class GetStartedScreen:
        title="Smart Investing, Simplified"
        description="SmartWealth by NBK Capital is an online financial advisor built for people who are seeking financial freedom."
        
        get_started_button= "Get Started"
        login_button="Login"
        change_language_button= "ع"
                
    
    class how_would_you_like_to_get_started_screen:
        title="How would you like to get started?"
        description="Start your SmartWealth account opening by selecting one of the options below"

        customized_title="Build an investment plan customized to you"
        customized_description="Answer 10 questions that will help us learn more about who you are. Based on that, we will build you a personalized investment plan."

        predefined_title="Select a ready-built investment plan"
        predefined_description="Choose an investment plan in line with your risk tolerance preferences: Conservative, Balanced, Growth."

        continue_button="Continue"

    
    class investment_type_screen:
        title="What type of investment do you want to start with?"
        description="Choose an investment plan. You can add more later."

        etf_title="Global Investment"
        etf_description="Start with $5000"
        etf_tag="Popular"

        islamic_title="Islamic Focused"
        islamic_description="Start with $5000"
        islamic_tag="New"

        not_eligible_tag="Not eligible"
        Continue="Continue"
    class islamic_popup:
        description="Our Islamic investment plans are heavily exposed to stocks and thus may experience more volatility than our other plans. This may not be suitable for all investors."
        
        continue_button="Continue"
        select_another_plan_button="Select a different plan"


class Investment_Proposal_Info:
    class Predefined:
        class ETF:
            def get_title(risk_score):
                risk_score=int(risk_score)
                if risk_score <=3 : return 'You have selected a conservative investment plan'
                elif risk_score>=4 and risk_score<=7: return 'You have selected a balanced investment plan'
                elif risk_score>=8 and risk_score<=10: return 'You have selected a growth investment plan'
                else: print("ERROR Wrong riskscore was sent to Investment_Proposal_Info")
                
            def get_description(risk_score):
                risk_score=int(risk_score)
                if risk_score <=3 : return 'This means your asset mix will have greater exposure to more stable and income focused instruments while your returns will be just above inflation.'
                elif risk_score>=4 and risk_score<=7: return 'This means your asset mix will focus on income and growth instruments to achieve greater returns. You can expect to see some downturns to achieve such returns.'
                elif risk_score>=8 and risk_score<=10: return 'This means your asset mix will focus on growth instruments to achieve the highest returns. We recommend a long-term investment horizon as markets run through their cycles.'
                else: print("ERROR Wrong riskscore was sent to Investment_Proposal_Info")

            def get_risk_score_text(risk_score):
                risk_score=int(risk_score)
                if risk_score<=10: return 'Your Risk Tolerance: '+str(risk_score)
                else: print("ERROR Wrong riskscore was sent to Investment_Proposal_Info")
                
        class ISLAMIC:
            def get_title(risk_score):
                return 'We recommend a Growth portfolio'
                
            def get_description(risk_score):
                return 'This means your asset mix will focus on growth instruments to achieve the highest returns. We recommend a long-term investment horizon as markets run through their cycles.'

            def get_risk_score_text(risk_score):
                return 'Your Risk Tolerance: '+str(1)
            
    class Customized:
        class ETF:
            def get_title(risk_score):
                
                if risk_score <=3 : return 'We recommend a Conservative portfolio'
                elif risk_score>=4 and risk_score<=7: return 'We recommend a Balanced portfolio'
                elif risk_score>=8 and risk_score<=10: return 'We recommend a Growth portfolio'
                else: print("ERROR Wrong riskscore was sent to Investment_Proposal_Info")
                
            def get_description(risk_score):
                
                if risk_score <=3 : return 'This means your asset mix will have greater exposure to more stable and income focused instruments while your returns will be just above inflation.'
                elif risk_score>=4 and risk_score<=7: return 'This means your asset mix will focus on income and growth instruments to achieve greater returns. You can expect to see some downturns to achieve such returns.'
                elif risk_score>=8 and risk_score<=10: return 'This means your asset mix will focus on growth instruments to achieve the highest returns. We recommend a long-term investment horizon as markets run through their cycles.'
                else: print("ERROR Wrong riskscore was sent to Investment_Proposal_Info")

            def get_risk_score_text(risk_score):
                
                if risk_score<=10: return 'Your Risk Tolerance: '+str(risk_score)
                else: print("ERROR Wrong riskscore was sent to Investment_Proposal_Info")

        class ISLAMIC:
            def get_title(risk_score):
                
                if risk_score ==1 : return 'We recommend a Conservative portfolio'
                elif risk_score==2: return 'We recommend a Balanced portfolio'
                elif risk_score==3: return 'We recommend a Growth portfolio'
                else: print("ERROR Wrong riskscore was sent to Investment_Proposal_Info")
                
            def get_description(risk_score):
                
                if risk_score ==1 : return 'This means your asset mix will have greater exposure to more stable and income focused instruments while your returns will be just above inflation.'
                elif risk_score==2: return 'This means your asset mix will focus on income and growth instruments to achieve greater returns. You can expect to see some downturns to achieve such returns.'
                elif risk_score==3: return 'This means your asset mix will focus on growth instruments to achieve the highest returns. We recommend a long-term investment horizon as markets run through their cycles.'
                else: print("ERROR Wrong riskscore was sent to Investment_Proposal_Info")

            def get_risk_score_text(risk_score):
                
                if risk_score<=3: return 'Your Risk Tolerance: '+str(risk_score)
                else: print("ERROR Wrong riskscore was sent to Investment_Proposal_Info")

    class Historical_Performance:
        class ETF:
            titles=["Developed Market Stocks","Emerging Market Stocks","Real Estate","Fixed Income","Cash"]
            percentages = {
                                            1: ["14%", "0%", "0%", "84%", "2%"],
                                            2: ["29%", "0%", "0%", "69%", "2%"],
                                            3: ["39%", "0%", "0%", "59%", "2%"],


                                            4: ["49%", "0%", "0%", "49%", "2%"],
                                            5: ["52%", "7%", "0%", "39%", "2%"],
                                            6: ["53%", "7%", "0%", "38%", "2%"],
                                            7: ["56%", "10%", "0%", "32%", "2%"],
                                            
                                            
                                            8: ["69%", "10%", "0%", "19%", "2%"],
                                            9: ["71%", "14%", "8%", "5%", "2%"],
                                            10: ["74%", "14%", "10%", "0%", "2%"]
                                        }
        class ISLAMIC:
            titles=["Developed Market Stocks","Emerging Market Stocks","Commodities","Money Market","Cash"]
            percentages = {
                                            1: ["68%", "5%", "25%", "0%", "2%"],
                                            2: ["78.1%", "5%", "14.9%", "69%", "2%"],
                                            3: ["88%", "5%", "5%", "0%", "2%"]
                                        }





