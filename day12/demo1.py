import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample11.html")
staus=driver.find_element(By.ID,"A1").is_enabled() #True enabled
print(staus)

staus=driver.find_element(By.ID,"A4").is_enabled() #False disabled
print(staus)

staus=driver.find_element(By.ID,"A1").is_displayed() #True - visible
print(staus)

staus=driver.find_element(By.ID,"A3").is_displayed() #False - hidden
print(staus)

#Check box , Radio Button , option in list box
staus=driver.find_element(By.ID,"A5").is_selected() #True -> Selected
print(staus)

staus=driver.find_element(By.ID,"A6").is_selected() #False -> Not Selected
print(staus)

driver.close()



















