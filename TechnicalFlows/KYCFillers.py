from doctest import OPTIONFLAGS_BY_NAME
from time import sleep
from CheckIfPageLoading import CheckIfPageLoading
from GesturesAndMotions import scrollDown
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def SelectLocation(driver,Field, ChosenLocation):
    
    # StringasList = ["%s"%ChosenLocation]
    # ExpectedFirstLetter=StringasList[0][0]
    LetterSelected=False
    LocationFound=False
    ExpectedFirstLetter=ChosenLocation[0]
    # print(ExpectedFirstLetter)

    
    try:
        WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/fastScrollerView")))
        parentElement=driver.find_element(By.ID,"neo.nbkc.smartwealth.demo:id/fastScrollerView")
        elementList = parentElement.find_elements(By.CLASS_NAME,"android.widget.TextView")
        ScrollerExists=True
        Maximum=2
    except: 
        ScrollerExists=False
        Maximum=10
        
    if ScrollerExists:
        count=0
        while (LetterSelected == False) and (count < 25):
            for ELEM in elementList:
                if ELEM.text==ExpectedFirstLetter:
                    LetterSelected=True
                    ELEM.click()
                    sleep(0.5)
                    break
                count=count+1
        
        if LetterSelected == False:
            print ("Error in KYC JSON File in field: "+Field)
    
    Count_Location=0
    while LocationFound==False and Count_Location< Maximum:
        Locations=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        for ELEM in Locations:
            Text=ELEM.text
            if Text == ChosenLocation:
                ELEM.click()
                LocationFound=True
                break
        if LocationFound==False:
            scrollDown(driver,500, 1000, 500, 600)
        Count_Location=Count_Location+1
    CheckIfPageLoading(driver)

    if LocationFound==False:
        print ("Error in KYC JSON File in field: "+Field)
    else:
        WebDriverWait(driver,7).until(EC.visibility_of_element_located((By.ID, "neo.nbkc.smartwealth.demo:id/tvTitle")))
        
    return LocationFound
        

# def ClickofMutiSelectionCheckboxes(driver, location, )

def ClickonCheckbox(driver,Field,Option,AvailableOptions):
    if Field == "Gender":
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")))
        CheckboxOptions=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
        OptionFound=False
        for ELEM in CheckboxOptions:
            if ELEM.text==Option:
                OptionFound=True
                ELEM.click()
                sleep(0.5)
                break
        if OptionFound==False:
            print("Issue in JSON file in Field: "+Field)
        return OptionFound
    
    if Field=="Source_Of_Income":
        OptionFound=False
        parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
        Title= parentElement[2].find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        
        ReasonForInvesting= parentElement[0].find_element(By.ID,"neo.nbkc.smartwealth.demo:id/tvTitle")
        # print(ReasonForInvesting.text)

        if ReasonForInvesting.text=="Trading experience": #We are on customized flow.
            Inputs3=parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
            AvailableOptions=Inputs3
            X=AvailableOptions[0].text
            Y=AvailableOptions[1].text
            Z=AvailableOptions[2].text
            B=AvailableOptions[3].text
            R=AvailableOptions[4].text
            M=AvailableOptions[5].text
            # print([X,Y,Z,B,R,M])
            
            for ELEM in Option:
                if ELEM==X: 
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[0].click()
                    OptionFound=True
                    sleep(2)
                elif ELEM==Y :
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[1].click()
                    OptionFound=True
                    sleep(2)
                elif ELEM==Z :
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[2].click()
                    OptionFound=True
                    sleep(2)
                elif ELEM==B :
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[3].click()
                    OptionFound=True
                    sleep(2)
                elif ELEM==R :
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[4].click()
                    OptionFound=True
                    sleep(2)
                elif ELEM==M:
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[1].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[5].click()
                    OptionFound=True
                    sleep(2)
        else:
            Inputs3=parentElement[2].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
            AvailableOptions=Inputs3
            X=AvailableOptions[0].text
            Y=AvailableOptions[1].text
            Z=AvailableOptions[2].text
            B=AvailableOptions[3].text
            R=AvailableOptions[4].text
            M=AvailableOptions[5].text
            # print([X,Y,Z,B,R,M])
            
            for ELEM in Option:
                if ELEM==X: 
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[2].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[0].click()
                    OptionFound=True
                    sleep(2)
                elif ELEM==Y :
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[2].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[1].click()
                    OptionFound=True
                    sleep(2)
                elif ELEM==Z :
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[2].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[2].click()
                    OptionFound=True
                    sleep(2)
                elif ELEM==B :
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[2].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[3].click()
                    OptionFound=True
                    sleep(2)
                elif ELEM==R :
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[2].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[4].click()
                    OptionFound=True
                    sleep(2)
                elif ELEM==M:
                    parentElement=driver.find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/dropdown")
                    Inputs3=parentElement[2].find_elements(By.ID,"neo.nbkc.smartwealth.demo:id/tvContent")
                    Inputs3[5].click()
                    OptionFound=True
                    sleep(2)
            
        
                

        if OptionFound==False:
            print("Issue in JSON file in Field: "+Field)
        
    else:
        OptionFound=False
        for ELEM in AvailableOptions:
            if ELEM.text==Option:
                OptionFound=True
                ELEM.click()
                sleep(0.5)
                break
        if OptionFound==False:
            print("Issue in JSON file in Field: "+Field)
      
                
        
    

def ChooseBirthDate(driver,Field, DateChosen):
    Year_Found=False
    Month_Found=False
    Day_Found=False

    CheckIfPageLoading(driver)

    ListDate=DateChosen.split()
    
    Day=ListDate[0]
    Month=ListDate[1]
    Year=ListDate[2]
    
    # print(Day+"/"+Month+"/"+Year)
    
    YearButton=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"android:id/date_picker_header_year")))
    YearButton.click()
    
    count=0
    while Year_Found==False and count<=5:
        ListofYears=driver.find_elements(By.ID,"android:id/text1")
        for YearX in ListofYears:
            # print(YearX.text,Year)
            if YearX.text==Year:
                Year_Found=True
                YearX.click()
                sleep(0.5)
                break
                #Year is chosen
        if Year_Found==False:
            scrollDown(driver,500, 1000, 500, 1600)
        count=count+1
        
    if Year_Found==False:
        print ("Error in KYC JSON File in field: "+Field)
        
    count=0    
    Forward=True
    while Month_Found==False:
        parentElement=driver.find_element(By.ID,"android:id/day_picker_view_pager")
        elementList = parentElement.find_elements(By.CLASS_NAME,"android.view.View")
        DatePickedByDefault=elementList[0].get_attribute("content-desc").split()
        MonthPickedByDefault=DatePickedByDefault[1]
        
        if MonthPickedByDefault!=Month and MonthPickedByDefault=="December"and Forward==True:
            Forward=False
            # print(MonthPickedByDefault+" Forward=False")

        if MonthPickedByDefault!=Month and MonthPickedByDefault=="January":
            Forward=True
            # print(MonthPickedByDefault+" Forward=True")
            
        if MonthPickedByDefault==Month:
            Month_Found=True
            sleep(0.5)
            break
        elif Forward==True:
            driver.find_element(By.ID,"android:id/next").click()
            # print("Next")
        elif Forward==False:
            driver.find_element(By.ID,"android:id/prev").click()
            # print("Previous")
        if count==20:
            print ("Error in KYC JSON File in field: "+Field)
            break
        count=count+1

    parentElement=driver.find_element(By.ID,"android:id/day_picker_view_pager")
    elementList = parentElement.find_elements(By.CLASS_NAME,"android.view.View")
    
    for ELEM in elementList:
        if ELEM.text == Day:
            Day_Found=True
            ELEM.click()
            sleep(0.5)
            driver.find_element(By.ID,"android:id/button1").click()
            sleep(1)
            break
    
    if Day_Found==False:
        print ("Error in KYC JSON File in field: "+Field)
    CheckIfPageLoading(driver)



def ChooseExpiryDate(driver,Field, DateChosen):
    Year_Found=False
    Month_Found=False
    Day_Found=False
    
    ListDate=DateChosen.split()
    
    Day=ListDate[0]
    Month=ListDate[1]
    Year=ListDate[2]
    
    # print(Day+"/"+Month+"/"+Year)
    
    YearButton=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"android:id/date_picker_header_year")))
    YearButton.click()
    
    count=0
    while Year_Found==False and count<=5:
        ListofYears=driver.find_elements(By.ID,"android:id/text1")
        for YearX in ListofYears:
            # print(YearX.text,Year)
            if YearX.text==Year:
                Year_Found=True
                YearX.click()
                sleep(0.5)
                break
                #Year is chosen
        if Year_Found==False:
            scrollDown(driver,500, 1500, 500, 900)
        count=count+1
        
    if Year_Found==False:
        print ("Error in KYC JSON File in field: "+Field)
        
    count=0    
    Forward=True
    while Month_Found==False:
        parentElement=driver.find_element(By.ID,"android:id/day_picker_view_pager")
        elementList = parentElement.find_elements(By.CLASS_NAME,"android.view.View")
        DatePickedByDefault=elementList[0].get_attribute("content-desc").split()
        MonthPickedByDefault=DatePickedByDefault[1]
        
        if MonthPickedByDefault!=Month and MonthPickedByDefault=="December"and Forward==True:
            Forward=False
            # print(MonthPickedByDefault+" Forward=False")

        if MonthPickedByDefault!=Month and MonthPickedByDefault=="January":
            Forward=True
            # print(MonthPickedByDefault+" Forward=True")
            
        if MonthPickedByDefault==Month:
            Month_Found=True
            sleep(0.5)
            break
        elif Forward==True:
            driver.find_element(By.ID,"android:id/next").click()
            # print("Next")
        elif Forward==False:
            driver.find_element(By.ID,"android:id/prev").click()
            # print("Previous")
        if count==20:
            print ("Error in KYC JSON File in field: "+Field)
            break
        count=count+1

    parentElement=driver.find_element(By.ID,"android:id/day_picker_view_pager")
    elementList = parentElement.find_elements(By.CLASS_NAME,"android.view.View")
    
    for ELEM in elementList:
        if ELEM.text == Day:
            Day_Found=True
            ELEM.click()
            sleep(0.5)
            driver.find_element(By.ID,"android:id/button1").click()
            sleep(1)
            break
    
    if Day_Found==False:
        print ("Error in KYC JSON File in field: "+Field)

    CheckIfPageLoading(driver)
