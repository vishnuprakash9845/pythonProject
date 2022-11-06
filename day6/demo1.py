import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/sample4.html")
driver.find_element(By.CSS_SELECTOR,"input[Type='Text']").send_keys("bhanu")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("akshara")
time.sleep(1)

driver.close()