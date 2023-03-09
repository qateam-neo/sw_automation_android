

from asyncio import sleep
from Intensive_Tests.config import Application_screens
from Intensive_Tests.helpers import AppiumActions, ApplicationHelpers, Reporting
from Intensive_Tests.kyc.flows.personal_info.config import  KYC_Fields
from Intensive_Tests.kyc.config import IDS, Field_types
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy



class PersonalInfo:
    def __init__(self,driver):
        self.driver=driver
        self.helpers=ApplicationHelpers(self.driver)
        self.AppiumGestures=AppiumActions(self.driver)
    
        self.Report=Reporting(self.driver,"Personal Information KYC ")
    
 
    def fill_field(self,Field):
        if Field.is_visible:
            parent=self.AppiumGestures.find_element_parent_by_text(Field)
            if Field.type == Field_types.selection: self.AppiumGestures.choose_option(parent,Field)
            elif Field.type == Field_types.input: self.AppiumGestures.fill_input(parent,Field)
            elif Field.type == Field_types.date_picker: self.AppiumGestures.fill_date_picker(parent,Field)
            elif Field.type == Field_types.list_picker: self.AppiumGestures.fill_list_picker(parent,Field)
            sleep(1.5)
    
    def test_blue_screen(self):
        try:
            self.helpers.test_screen_localization(Application_screens.Personal_info_blue)
            self.AppiumGestures.click_element(IDS.Blue_Screen.start_button)
        except:
            self.Report.report_testcase(False,"Personal info blue screen","N/A")
            
            
    def start_happy_path(self):
        self.test_blue_screen()
        for field_name, field_class in vars(KYC_Fields).items():
            if isinstance(field_class, type) or not (field_name.startswith("__") or field_name.endswith("__")):
                # use field_class here as needed                
                try:self.fill_field(field_class)
                except:
                    self.AppiumGestures.scroll_down()
                    self.fill_field(field_class)
        self.AppiumGestures.click_element(IDS.submit_button)