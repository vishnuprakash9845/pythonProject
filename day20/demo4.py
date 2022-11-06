import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.service import Service
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@type='text' and not(name='q')]").send_keys("bhanu")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("bhanu123")
time.sleep(5)

driver.close()

