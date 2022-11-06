import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Sample1.html")
element=driver.find_element(By.TAG_NAME,"a")
element.click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.ID,"a1").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.NAME,"n1").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CLASS_NAME,"c1").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.LINK_TEXT,"Akshara").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"Ak").click()
time.sleep(1)
driver.close()