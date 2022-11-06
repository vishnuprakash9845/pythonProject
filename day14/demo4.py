import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.actitime.com/login.do")

un=driver.find_element(By.ID,"username")
driver.execute_script("arguments[0].value=arguments[1]",un,"admin")

pw=driver.find_element(By.NAME,"pwd")
driver.execute_script("arguments[0].value=arguments[1]",pw,"manager")

login=driver.find_element(By.XPATH,"//div[.='Login ']")
driver.execute_script("arguments[0].click()",login)

time.sleep(5)

driver.close()