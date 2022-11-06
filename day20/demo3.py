import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.service import Service
# driver=webdriver.Chrome(ChromeDriverManager().install())
import os

driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample16.html")
time.sleep(1)
driver.find_element(By.ID,"A3").click()
time.sleep(1)
driver.find_element(By.ID,"PageLink_9").click()
time.sleep(1)
driver.find_element(By.ID,"DirectLink_13").click()
time.sleep(3)
#verify that file is present or not in download folder- present -PASS , not present -FAIL
path = '/Users/vishnu/Downloads/tender_datasheet.pdf'

isExist = os.path.exists(path)
print(isExist)

if isExist:
    print("File downloaded successfully")
else:
    print("File not downloaded successfully")

driver.quit()
