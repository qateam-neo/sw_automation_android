

    
        
        

class Deposit:
    risk_score_target = 1
    driver = None
    
    def __init__(self,driver,email):
        self.driver = driver
        self.email=email
        self.ReportDriver=None 


    def outer(self, driver,email):
        self.driver = driver
        self.email=email
        self.ReportDriver=None
        
    class Wire:  
        
        def __init__(self,driver,email):
            self.driver = driver
            self.email=email
            self.ReportDriver=None 
        
        def test_inner(self):
            innervar="innnerrrrr"
            print(self.email)
            
            
        
        

Deposit("N/A","rrrrrrrrrrrrrr").test_outer("dsdds")
