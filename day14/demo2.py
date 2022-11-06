import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with

#how do handle (perform action) the element if it is disabled
#how to u enter the value into textbox without using send_keys

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample11.html")

# element1=driver.find_element(By.ID,"A4")
# element1.send_keys("Hi")
time.sleep(1)
driver.execute_script("document.getElementById('A1').value='Akshara';")
driver.execute_script("document.getElementById('A4').value='Akshara';")

time.sleep(2)
driver.execute_script("document.getElementById('A1').type='checkbox';")
time.sleep(5)

driver.close()