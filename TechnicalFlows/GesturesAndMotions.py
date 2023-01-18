import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def RefreshScreenusingswipe(self):
    self.swipe(452, 544, 416, 1694, 626)

def taponcoordinates(self,x_coord,y_coord):
    self.tap([(x_coord, y_coord)])

def closeapp(self,x_start,y_start,x_end,y_end,speed=400):
    self.swipe(x_start,y_start,x_end,y_end,speed)
    
def scrollDown(self,x_start,y_start,x_end,y_end):
    self.swipe(x_start,y_start,x_end,y_end,1000)


        


# def SearchText(self,Text):
#     self.find_element_by_xpath(Text)
