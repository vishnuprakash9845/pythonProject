import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Sending the URL and wait till page loads
driver.get('https://demo.actitime.com/login.do')
driver.maximize_window()
time.sleep(3)

#get the address of the element where cusor is blinking
username=driver.switch_to.active_element
username.send_keys('admin')
time.sleep(1)
username.send_keys(Keys.TAB)
time.sleep(1)
password=driver.switch_to.active_element
password.send_keys('manager')
time.sleep(1)
password.send_keys(Keys.TAB)
time.sleep(1)
checkbox=driver.switch_to.active_element
checkbox.send_keys(Keys.TAB)
time.sleep(1)
loginButton=driver.switch_to.active_element
loginButton.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()