from Intensive_Tests.deposits.config import TransferRules


class Localization_KNET:

    class KNETPopup:
        title="KNET Terms of Use"
        description="""The amount will be deducted in KD. A convenience fee of KD 0.150 will be added on top of your deposit amount.

I understand and declare that I am about to credit my SmartWealth account with NBK Capital with funds debited from a bank account opened in my name using the KNET payment service. I further declare that I am the sole owner and beneficiary of the registered and used bank accounts and I did not violate any relevant laws or regulations including but not limited to the CMA Law No. 7 of 2010 and its Executive Regulations without any responsibility on the part of NBK Capital in this regard."""
        
        continue_button="Continue"
        


    class Enter_Amount:
        title="KNET"
        description="You will be directed to KNET to complete your payment"
        enter_amount="Enter Amount"
        
        class error_messages:
            def minimum_deposit_error(depositflow):
                minimum_deposit="Minimum deposit amount is $%s."%TransferRules.KNETBoundaries.initial_deposit.MIN
        continue_button="Continue to KNET"
        
                        
            
    class TransferInstructions:
        title="Transfer Instructions"
        description="You're almost done! You still need to transfer the below amount from your NBK app to complete your deposit:"
        
        dropdown_description="I will wire funds from this bank account:"
        continue_button="Done"
        
