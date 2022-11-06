import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Open the Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Sending the URL and wait till page loads
driver.get('http://www.google.com')
time.sleep(1)
driver.get('http://www.fb.com')
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
time.sleep(1)

#Close the browser
driver.close()