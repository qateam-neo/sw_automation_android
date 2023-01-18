class Localization_withdrawal:
    class Settings_screen:

        title = "Settings"
        
        personal_info_title ="Personal Information"
        personal_info_description ="Manage your personal information"
        
        biometric_title ="Biometric Login"
        biometric_description ="Use Biometric to log in"
        
        notification_title ="Push Notifications"
        notification_description ="Enable push notifications for reminders on your investments."

        otp_title ="Manage OTP"
        otp_description ="You can now manage your OTP delivery method."

        withdrawal_title = "Withdrawals"
        withdrawal_description = "Make a withdrawal"
        
        language_title ="Language"
        language_description ="Change the language of the app"


    class Choose_portfolio:
        select_account="Select account"

        portfolio1_title="General"
        portfolio1_type="Conventional"
        islamic_portfolio_type="Islamic"

    class withdrawal_type:
        title="What type of withdrawal are you looking to make?"
        
        withdrawal_type_label="Select your withdrawal type"
        
        Full_withdrawal_title= "Full redemption"
        Full_withdrawal_description= "Withdraw all my units and holdings"
        
        Partial_withdrawal_title= "Partial redemption"
        Partial_withdrawal_description= "Withdraw a specific amount"
        
        
    class otp_screen:
        title="OTP Verification"
        description="Enter the OTP we have sent you to your email"  
        
        label="Enter your OTP code here"
        
        resend="Resend code"
        
        continue_button="Verify"

    class thank_you:
        
        title ="Thank you"
        subtitle="We have received your withdrawal request, and will process it within 7 business days."
        description="The actual withdrawal amount might be different than the amount requested due to market prices fluctuations."
        close_button="Close"

      
class IDS:    
    class Settings_screen:
        title = "neo.nbkc.smartwealth.demo:id/titleTv"
        
        home_button="neo.nbkc.smartwealth.demo:id/navigation_home"
        deposit_button="neo.nbkc.smartwealth.demo:id/navigation_transfer"
        settings_button="neo.nbkc.smartwealth.demo:id/navigation_more"
        
        personal_info_title =("neo.nbkc.smartwealth.demo:id/title",0)
        personal_info_description =("neo.nbkc.smartwealth.demo:id/description",0)
        personal_info_button=("neo.nbkc.smartwealth.demo:id/cardView",0)
        
        biometric_title =("neo.nbkc.smartwealth.demo:id/title",1)
        biometric_description =("neo.nbkc.smartwealth.demo:id/description",1)
        biometric_button=("neo.nbkc.smartwealth.demo:id/cardView",1)
        
        notification_title =("neo.nbkc.smartwealth.demo:id/title",2)
        notification_description =("neo.nbkc.smartwealth.demo:id/description",2)
        notification_button=("neo.nbkc.smartwealth.demo:id/cardView",2)

        otp_title =("neo.nbkc.smartwealth.demo:id/title",3)
        otp_description =("neo.nbkc.smartwealth.demo:id/description",3)
        otp_button=("neo.nbkc.smartwealth.demo:id/cardView",3)

        withdrawal_title =("neo.nbkc.smartwealth.demo:id/title",4)
        withdrawal_description =("neo.nbkc.smartwealth.demo:id/description",4)
        withdrawal_button=("neo.nbkc.smartwealth.demo:id/cardView",4)
        
        language_title =("neo.nbkc.smartwealth.demo:id/title",5)
        language_description =("neo.nbkc.smartwealth.demo:id/description",5)
        language_button=("neo.nbkc.smartwealth.demo:id/cardView",5)

    class Choose_portfolio:
        select_account="neo.nbkc.smartwealth.demo:id/balanceHeaderTextView"

        portfolio1_title="neo.nbkc.smartwealth.demo:id/reasonTextView"
        portfolio1_type="neo.nbkc.smartwealth.demo:id/modeTextView"
        portfolio1_option="neo.nbkc.smartwealth.demo:id/disclosureImageView"


    class withdrawal_type:
        title="neo.nbkc.smartwealth.demo:id/tvTitle"
        
        withdrawal_type_label="neo.nbkc.smartwealth.demo:id/tvSelectRedemption"
        
        Full_withdrawal_title= ("neo.nbkc.smartwealth.demo:id/labelTitle",0)
        Full_withdrawal_description=("neo.nbkc.smartwealth.demo:id/labelDesc",0)
        Full_withdrawal_button=("neo.nbkc.smartwealth.demo:id/cardView",0)
        
        Partial_withdrawal_title= ("neo.nbkc.smartwealth.demo:id/labelTitle",1)
        Partial_withdrawal_description=("neo.nbkc.smartwealth.demo:id/labelDesc",1)
        Partial_withdrawal_button=("neo.nbkc.smartwealth.demo:id/cardView",1)
        
        continue_button= "neo.nbkc.smartwealth.demo:id/btnContinue"

    class withdrawal_amount:
        title="neo.nbkc.smartwealth.demo:id/tvLblWithdrawReason"
        purpose_label="neo.nbkc.smartwealth.demo:id/tvLblPurposeOfWithdrawal"
        withdrawal_account_label="neo.nbkc.smartwealth.demo:id/tvLblWithdrawalAccount"
        
        withdrawal_amount_entry="neo.nbkc.smartwealth.demo:id/etInput"
        full_withdrawal_amount_entry="neo.nbkc.smartwealth.demo:id/tvAmount"
        withdrawal_reason_dropdown="neo.nbkc.smartwealth.demo:id/pickerWithdrawalReason"
        
        
        info_label="neo.nbkc.smartwealth.demo:id/tvLblNote"
        submit_button="neo.nbkc.smartwealth.demo:id/btnSubmit"
        
    class otp_screen:
        title="neo.nbkc.smartwealth.demo:id/tv_title"
        description="neo.nbkc.smartwealth.demo:id/tvDescription"  
        
        label="neo.nbkc.smartwealth.demo:id/tv_enter_otp"
        entries_id="neo.nbkc.smartwealth.demo:id/et_input"
        
        resend="neo.nbkc.smartwealth.demo:id/tvResendOtp"
        countdown="neo.nbkc.smartwealth.demo:id/tvCountdown"
        
        continue_button="neo.nbkc.smartwealth.demo:id/btnSubmit"


    class thank_you:
        
        title ="neo.nbkc.smartwealth.demo:id/statusTextView"
        subtitle="neo.nbkc.smartwealth.demo:id/titleTextView"
        description="neo.nbkc.smartwealth.demo:id/subTitleTextView"
        close_button="neo.nbkc.smartwealth.demo:id/closeButton"


    class book_a_call:
        
        title="neo.nbkc.smartwealth.demo:id/tv_title"
        description="neo.nbkc.smartwealth.demo:id/tv_info"
        book_a_call_button="neo.nbkc.smartwealth.demo:id/btn_book"
        continue_button="neo.nbkc.smartwealth.demo:id/btn_continue"
        













class TransferRules:
            
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
            
      