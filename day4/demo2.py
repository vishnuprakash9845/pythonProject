import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Sending the URL and wait till page loads
driver.get('http://www.fb.com')
time.sleep(1)
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.get('http://www.google.com')
driver.back()
driver.forward()
driver.refresh()
driver.quit()