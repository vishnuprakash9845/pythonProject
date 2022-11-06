import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Sending the URL and wait till page loads
driver.get('https://demo.actitime.com/login.do')
driver.maximize_window()
time.sleep(3)

#get the address of the element where cusor is blinking
element=driver.switch_to.active_element

#enter 'admin' on active element
element.send_keys('admin')
time.sleep(3)
driver.quit()