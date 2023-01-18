xpath = {
    'conservative_option_pointer': '/html/body/div[1]/div/div[1]/div/div/div[2]/div/div[1]/div[1]',
    'balanced_option_pointer': '/html/body/div[1]/div/div[1]/div/div/div[2]/div/div[1]/div[2]',
    'growth_option_pointer': '/html/body/div[1]/div/div[1]/div/div/div[2]/div/div[1]/div[3]',
    'predefined_continue_pointer': '/html/body/div[1]/div/div[1]/div/div/div[2]/div/div[2]/button'
}

class Localization_Predefined:
    
    class predefined_options_screen:
        title="What level of risk do you feel comfortable with?"
        
        balanced_title="Balanced"
        balanced_description="This means your asset mix will focus on income and growth instruments to achieve greater returns. You can expect to see some downturns to achieve such returns."
    
        conservative_title="Conservative"
        conservative_description="This means your asset mix will have greater exposure to more stable and income focused instruments while your returns will be just above inflation."    

        growth_title="Growth"
        growth_description="This means your asset mix will focus on growth instruments to achieve the highest returns. We recommend a long-term investment horizon as markets run through their cycles."
    
        not_sure_button="Not sure? Help me decide"
        continue_button="Continue"
        