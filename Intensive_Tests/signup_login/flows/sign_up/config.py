from Intensive_Tests.deposits.config import TransferRules
from Intensive_Tests.helpers import APIS
x=APIS(email="roy.braish+test@neo.ae").get_email_count()


class Credentials:
    first_name="test"
    last_name="test"
    email="roy.braish+test@neo.ae"
    password="Password123"



class Localization_SignUp:

    class SignUp:
        title="Create your account"
        
        first_name_title="First Name"
        last_name_title="Last Name"
        email_title="Email"
        pass_title="Password"
        
        first_name_entry="Enter your first name"
        last_name_entry="Enter your last name"
        email_entry="Enter your email"
        pass_entry="Enter your password"
        
        
        Policy_message='By selecting "Sign up" , I approve the Terms & Conditions and Privacy Policy.'
        
        continue_button="Sign up"
        
        
        class error_messages:
            class email_exists:
                title="Sign Up Error"
                description="An error has occurred. Please contact support team."
                
                cancel_button="Cancel"
                contact_support_button="Contact Support"