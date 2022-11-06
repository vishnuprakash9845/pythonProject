import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# 1.open the browser and enter the actitime url
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.actitime.com/login.do")
time.sleep(2)
# 2. enter valid user name
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("admin")
# 3.enter valid password
driver.find_element(By.XPATH,"//input[@name='pwd']").send_keys("manager")

# 4. click on login button
driver.find_element(By.XPATH,"//div[starts-with(text(),'Login')]").click()
time.sleep(5)

driver.quit()