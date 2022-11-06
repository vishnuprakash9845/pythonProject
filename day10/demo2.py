import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Sample10.html")
time.sleep(1)
sql=driver.find_element(By.XPATH,"//td[.='SQL']")

driver.find_element(locate_with(By.TAG_NAME,'input').to_left_of(sql)).click()
time.sleep(1)

price=driver.find_element(locate_with(By.TAG_NAME,'td').to_right_of(sql)).text
print("Right : "+price)
time.sleep(2)

beforeSQL=driver.find_element(locate_with(By.TAG_NAME,'td').above(sql)).text
print("Above : "+beforeSQL)
time.sleep(2)

afterSQl=driver.find_element(locate_with(By.TAG_NAME,'td').below(sql)).text
print("Below : "+afterSQl)
time.sleep(2)

driver.close()


