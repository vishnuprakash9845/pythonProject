import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


#write login and logout code for actitime
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://demo.actitime.com/login.do")
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
driver.find_element(By.XPATH,"//div[.='Login ']").click()
time.sleep(5)
driver.find_element(By.ID,"logoutLink").click()

driver.close()