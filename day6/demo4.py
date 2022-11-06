import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Sample1.html")

driver.find_element(By.CSS_SELECTOR,"a[id='a1']").click()
time.sleep(1)
driver.back()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,"a#a1").click()
time.sleep(1)
driver.back()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,"#a1").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"a[class='c1']").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"a.c1").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,".c1").click()
time.sleep(1)
driver.back()
time.sleep(1)

driver.quit()