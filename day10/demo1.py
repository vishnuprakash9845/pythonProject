import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Sample9.html")
time.sleep(1)
driver.find_element(By.XPATH,"//td[.='API']/..//input").click()
time.sleep(3)
# Find element using relative locators using right of
# find the independent element
api = driver.find_element(By.XPATH,"//td[.='API']")
# If checkbox position is sure present to right use to_right else use near
driver.find_element(locate_with(By.TAG_NAME,"input").to_right_of(api)).click()
#driver.find_element(locate_with(By.TAG_NAME,"input").near(api)).click()
time.sleep(3)

driver.get("file:///Users/vishnu/Downloads/Sample10.html")
time.sleep(1)
api = driver.find_element(By.XPATH,"//td[.='API']")
driver.find_element(locate_with(By.TAG_NAME,"input").to_left_of(api)).click()
#driver.find_element(locate_with(By.TAG_NAME,"input").near(api)).click()
time.sleep(3)

driver.close()