from Intensive_Tests.deposits.config import TransferRules


class Localization_Mobile_number:
    
    class Verify_Mobile_number:
        title="Confirm your mobile number"
        description="Hello! We need you to confirm that this is still your mobile number:"
        
        support_message="In case this phone number is not yours or invalid, please contact support."
        continue_button="Yes, this is my number"

    class thank_you:
        
        title="Success! We've confirmed your number"
        description="Amazing! We've verified your number. This helps keep your account secure and a lot more."
        
        method_text="Would you like to set SMS as your preferred method for transaction OTPs? You can always change this within your settings."
        
        email_option="No, I prefer email"
        sms_option="Yes, set SMS for OTPs"
        
        