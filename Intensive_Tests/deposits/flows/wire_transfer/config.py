from Intensive_Tests.deposits.config import TransferRules


class Localization_BT:
    
    class IBAN:
        title="Complete Banking Details"
        description="Your IBAN is needed so we can process your deposits in a timely manner and so we know where to send your withdrawals to. This does not mean nor authorize SmartWealth to debit money from your bank account directly."
         
        iban_limit_message="IBAN must be between 14 and 34 characters."


    class Enter_Amount:
        title="Bank Transfer"
        description="You will see instructions to manually transfer the funds from your bank app on the next page"
        enter_amount="Enter Amount"
        
        class error_messages:
            def minimum_deposit_error(depositflow):
                minimum_deposit="Minimum deposit amount is $%s."%TransferRules.BKTransferBoundaries.initial_deposit.MIN
                        
            
    class TransferInstructions:
        title="Transfer Instructions"
        description="You're almost done! You still need to transfer the below amount from your NBK app to complete your deposit:"
        
        dropdown_description="I will wire funds from this bank account:"
        continue_button="Done"
        
