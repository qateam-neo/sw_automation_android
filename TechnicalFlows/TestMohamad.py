from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://my.nbkcapital-smartwealth.com")  #Call the variable and should execute the selected url
driver.maximize_window()  #maximize the windows after launch
print(driver.title)  #print the title of the website in the console
