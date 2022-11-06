import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with
#

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample11.html")
time.sleep(1)
element=driver.find_element(By.ID,"A2")
tag=element.tag_name
print(tag)

url=element.get_attribute("href")
print(url)

text=element.text
print(text)
