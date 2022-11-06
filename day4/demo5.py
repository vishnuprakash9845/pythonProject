import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Sending the URL and wait till page loads
driver.get('http://www.google.com')
driver.maximize_window()
time.sleep(3)

#get the address of the element where cusor is blinking
element=driver.switch_to.active_element

#enter 'python' on active element
element.send_keys('python')
time.sleep(3)
driver.quit()