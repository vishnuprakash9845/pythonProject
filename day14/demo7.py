import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.actimind.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH,"//a[contains(text(),'Learn')]").click()
time.sleep(7)

driver.close()