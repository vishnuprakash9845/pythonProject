import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Sample1.html")

driver.find_element(By.XPATH,"./html/body/a").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/a").click()
time.sleep(1)
driver.back()
time.sleep(1)

driver.close()