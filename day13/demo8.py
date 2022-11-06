import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with

#How to send a cmd line argument to js
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample11.html")

v=driver.find_element(By.ID,'A1').get_attribute('value')
print(v)

driver.execute_script("v=document.getElementById('A1').value;alert(v)")

time.sleep(4)

driver.quit()