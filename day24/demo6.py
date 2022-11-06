import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from day24.google import GooglePage

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.actitime.com/login.do")
unTB=driver.find_element(By.ID, "username")
driver.refresh()
unTB.send_keys("bhanu")


time.sleep(2)