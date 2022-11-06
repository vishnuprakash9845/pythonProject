import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Sending the URL and wait till page loads
driver.get('http://www.fb.com')
size=driver.get_window_size()
print(size)
print(size['width'])
print(size['height'])
time.sleep(1)
driver.set_window_size(500,800)
time.sleep(1)
currentPos = driver.get_window_position()
print(currentPos['x'])
print(currentPos['y'])
time.sleep(1)
driver.set_window_position(500,10)
time.sleep(1)
driver.quit()