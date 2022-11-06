import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with
#

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Sample11.html")
time.sleep(1)
textBox=driver.find_element(By.ID,"A1")
textBox.clear() #suitable for textbox/password
time.sleep(1)
textBox.send_keys("Akshara")
time.sleep(2)
driver.find_element(By.ID,"A2").click()
time.sleep(2)

driver.close()
