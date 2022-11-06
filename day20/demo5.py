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
driver.get("https://www.makemytrip.com/")

driver.find_element(By.XPATH,"//span[@class='langCardClose']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//span[contains(text(),'DEPARTURE')]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[text()='November 2022']/../../div[3]//p[text()='30']").click()
time.sleep(3)

driver.close()
