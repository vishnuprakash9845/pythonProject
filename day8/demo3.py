import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 1.open the browser and enter the actitime url
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)
# 2. enter valid user name
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
# 3.enter valid password
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")

# 4. click on login button
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)