import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample11.html")

element1=driver.find_element(By.ID,"A1")
v1=element1.get_attribute("value")
print(v1)

driver.execute_script("element2=document.getElementById('A1');v=element2.value;alert(v)")

time.sleep(2)

# we have to close popup and close it elese we will get UnexpectedAlertPresentException