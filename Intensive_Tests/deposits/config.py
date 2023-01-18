class KNET_Credentials:
    bank="Knet Test Card [KNET1]"
    card_number="0000000001"
    month="09"
    year="2025"
    pin="1234"


class Localization_deposits:
    
    class SelectPaymentMethod:
        title = "Deposit"
        description="Select Payment Method"
        
        knet_title = "KNET"
        knet_time= "5-7 days processing time"
        knet_description="Deposit quickly with your local debit card through KNET."
        
        bt_title = "Bank Transfer"
        bt_time= "5-7 days processing time"
        bt_description="Manually transfer money from your bank account based on these details."

        dd_title = "NBK Easy Transfer"
        dd_time= "Invested within 48 hours"
        dd_description="Link your NBK account with SmartWealth for automatic transfers."

        continue_button = "Continue"
        
    

    class PendingDashboard:
        title="Thank you"
        description="You will get full access as soon as your funds are received and invested."
        
        eid_title="Verify your ID"
        eid_description="Your ID was successfully scanned"
        
        kyc_title="Complete your information"
        kyc_description="Profile created and agreements duly signed"
        
        initial_deposit_title="Fund your account"
        initial_deposit_time="Approximately 2mins"
        initial_deposit_description="Deposit funds into your account to start your smart investment journey."
    
        

    class active_select_portfolio:
        
        select_account_label="Select account"
        
        portfolio_title="General"
        portfolio_type="Conventional"
        islamic_portfolio_type="Islamic"

        





      
class IDS:    
    class PendingDashboard:
        title="neo.nbkc.smartwealth.demo:id/tvBannerTitle"
        description="neo.nbkc.smartwealth.demo:id/tvBannerDesc"
        
        eid_image_button=("neo.nbkc.smartwealth.demo:id/imgIcon",0)
        eid_title=("neo.nbkc.smartwealth.demo:id/tvTitle",0)
        eid_description=("neo.nbkc.smartwealth.demo:id/tvDescription",0)
        
        kyc_image_button=("neo.nbkc.smartwealth.demo:id/imgIcon",1)
        kyc_title=("neo.nbkc.smartwealth.demo:id/tvTitle",1)
        kyc_description=("neo.nbkc.smartwealth.demo:id/tvDescription",1)

        initial_deposit_image_button=("neo.nbkc.smartwealth.demo:id/imgIcon",2)
        initial_deposit_title=("neo.nbkc.smartwealth.demo:id/tvTitle",2)
        initial_deposit_time="neo.nbkc.smartwealth.demo:id/tvTime"
        initial_deposit_description=("neo.nbkc.smartwealth.demo:id/tvDescription",2)
        
        do_it_later_button="neo.nbkc.smartwealth.demo:id/tvLater"
        
        
    class ActiveDashboard:
                
        home_button="neo.nbkc.smartwealth.demo:id/navigation_home"
        deposit_button="neo.nbkc.smartwealth.demo:id/navigation_transfer"
        settings_button="neo.nbkc.smartwealth.demo:id/navigation_more"

    class active_select_portfolio:
        
        select_account_label="neo.nbkc.smartwealth.demo:id/balanceHeaderTextView"
        
        portfolio_title="neo.nbkc.smartwealth.demo:id/reasonTextView"
        portfolio_type="neo.nbkc.smartwealth.demo:id/modeTextView"
        
        portfolio_amount="neo.nbkc.smartwealth.demo:id/valueTextView"
        portfolio1_option="neo.nbkc.smartwealth.demo:id/disclosureImageView"

    class SelectPaymentMethod:
        title = "neo.nbkc.smartwealth.demo:id/tvDeposit"
        description="neo.nbkc.smartwealth.demo:id/tvSelectPayment"
        
        
        knet_title = ("neo.nbkc.smartwealth.demo:id/labelTitle",0)
        knet_time= ("neo.nbkc.smartwealth.demo:id/tvSubtitle",0)
        knet_description=("neo.nbkc.smartwealth.demo:id/tvDescription",0)
        knet_option_button=("neo.nbkc.smartwealth.demo:id/card",0)

        bt_title = ("neo.nbkc.smartwealth.demo:id/labelTitle",1)
        bt_time= ("neo.nbkc.smartwealth.demo:id/tvSubtitle",1)
        bt_description=("neo.nbkc.smartwealth.demo:id/tvDescription",1)
        bt_option_button=("neo.nbkc.smartwealth.demo:id/card",1)
        
        # dd_title = ("neo.nbkc.smartwealth.demo:id/labelTitle",2)
        # dd_time=  ("neo.nbkc.smartwealth.demo:id/tvSubtitle",2)
        # dd_description=("neo.nbkc.smartwealth.demo:id/tvDescription",2)
        # dd_option_button=("neo.nbkc.smartwealth.demo:id/card",2)


        continue_button = "neo.nbkc.smartwealth.demo:id/btnContinue"

    class IBAN:
        title = "neo.nbkc.smartwealth.demo:id/labelTitle"
        description="neo.nbkc.smartwealth.demo:id/labelDesc"

        iban_entry="neo.nbkc.smartwealth.demo:id/etIBAN"
        iban_limit_message="neo.nbkc.smartwealth.demo:id/tvError"
        
        bank_name=("neo.nbkc.smartwealth.demo:id/tvName",0)
        user_name=("neo.nbkc.smartwealth.demo:id/tvName",1)
        
        continue_button="neo.nbkc.smartwealth.demo:id/btnContinueFunding"
    
    class Enter_Amount:
        title="neo.nbkc.smartwealth.demo:id/tvTitle"
        description="neo.nbkc.smartwealth.demo:id/tvInstructions"
        
        name="neo.nbkc.smartwealth.demo:id/tvName"
        bank="neo.nbkc.smartwealth.demo:id/tvBank"
        iban="neo.nbkc.smartwealth.demo:id/tvIban"
        
        amount_entry="neo.nbkc.smartwealth.demo:id/fieldEditText"
        error_message="neo.nbkc.smartwealth.demo:id/errorTextView"
        
        predefined_amount1="neo.nbkc.smartwealth.demo:id/tvOption1"
        predefined_amount2="neo.nbkc.smartwealth.demo:id/tvOption2"
        predefined_amount3="neo.nbkc.smartwealth.demo:id/tvOption3"

        continue_button="neo.nbkc.smartwealth.demo:id/btnSubmit"
        
    class TransferInstructions:
        title="neo.nbkc.smartwealth.demo:id/tvTitle"
        description="neo.nbkc.smartwealth.demo:id/tvDescription"
        
        continue_button="neo.nbkc.smartwealth.demo:id/btnDone"

    class KNETPopup:
        title="neo.nbkc.smartwealth.demo:id/labelTitle"
        description="neo.nbkc.smartwealth.demo:id/tvDescription"
        
        continue_button="neo.nbkc.smartwealth.demo:id/btnContinue"
        close_button="neo.nbkc.smartwealth.demo:id/ivClose"
        
    class KNET_class_locators:
        bank_button=("android.view.View","Select Your Bank")
        knet_testcard_button=("android:id/text1",KNET_Credentials.bank)
        
        month_dropdown=("android.view.View","MM")
        month_button=("android:id/text1",KNET_Credentials.month)

        year_dropdown=("android.view.View","YYYY")
        year_button=("android:id/text1",KNET_Credentials.year)

        cardnumber_pin_entry="android.widget.EditText"
        cancel_button=("android.widget.Button","Cancel")
        submit_button=("android.widget.Button","Submit")
        
        class second_screen:
            
            confirm=("android.widget.Button","Confirm")

        class error_screen_IDS:
            title="neo.nbkc.smartwealth.demo:id/tvErrorTitle"
            description="neo.nbkc.smartwealth.demo:id/tvErrorDesc"
            
            back_button="neo.nbkc.smartwealth.demo:id/btnBack"

        
class TransferRules:
    
    class BKTransferBoundaries:
        class initial_deposit:
            MIN= 5000
            MAX= 10000000
            INCREMENT=None
            
        class additional_deposit:
            MIN= 500
            MAX= 10000000
            INCREMENT=None
            
        class predefined_option:
            class balance_below_20000_not_black:
                INITIAL_DEPOSIT=[10000,20000,40000]
                ADDITIONAL_DEPOSIT=[3000,5000,10000]
                ADDITIONAL_PORTFOLIO=[1000,3000,10000]
                
            class balance_above_20000_below_100000_not_black:
                ADDITIONAL_DEPOSIT=[10000,20000,40000]
                ADDITIONAL_PORTFOLIO=[3000,5000,10000]

            class above_100000_black:
                INITIAL_DEPOSIT=[100000,150000,250000]
                ADDITIONAL_DEPOSIT=[10000,25000,50000]
                ADDITIONAL_PORTFOLIO=[5000,10000,20000]


    class KNETBoundaries:
        class initial_deposit:
            MIN= 5000
            MAX= 10000000
            INCREMENT=None
            
        class additional_deposit:
            MIN= 500
            MAX= 10000000
            INCREMENT=None
            
        class predefined_option:
            class balance_below_20000_not_black:
                INITIAL_DEPOSIT=[10000,20000,40000]
                ADDITIONAL_DEPOSIT=[3000,5000,10000]
                ADDITIONAL_PORTFOLIO=[1000,3000,10000]
                
            class balance_above_20000_below_100000_not_black:
                ADDITIONAL_DEPOSIT=[10000,20000,40000]
                ADDITIONAL_PORTFOLIO=[3000,5000,10000]

            class above_100000_black:
                INITIAL_DEPOSIT=[100000,150000,250000]
                ADDITIONAL_DEPOSIT=[10000,25000,50000]
                ADDITIONAL_PORTFOLIO=[5000,10000,20000]


    class DDBoundaries:
        class initial_deposit:
            MIN= 5000
            MAX= 160000
            INCREMENT=None
            
        class additional_deposit:
            MIN= 500
            MAX= 160000
            INCREMENT=None

        class recurrent_payments:
            MAX=160000
            MAX_DAILY=160000
            
            
    class Withdrawal:   
        
        class single_portolio:
            def getMaximumWithdrawalamount(Balance):
                minimum_withdrawal_amount=1         
                _Minimum_allowed_portfolio_balance=5000

                if Balance >_Minimum_allowed_portfolio_balance:    return Balance-_Minimum_allowed_portfolio_balance
                else:   return False
                
        class multiple_portfolio:
            def getMaximumWithdrawalamount(list_other_potfolio_balances,target_portfolio_balance):
                minimum_withdrawal_amount=1         
                _Minimum_allowed_portfolio_balance=5000
                _minimum_balance_other_portfolio_valid=500
                _minimum_balance_other_portfolio_not_valid=5000
                
                for PortfolioBalance in list_other_potfolio_balances:    
                    if PortfolioBalance >= _Minimum_allowed_portfolio_balance:    return target_portfolio_balance-_minimum_balance_other_portfolio_valid
                    
                return target_portfolio_balance-_minimum_balance_other_portfolio_not_valid
            
      