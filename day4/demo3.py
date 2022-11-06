import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Sending the URL and wait till page loads
driver.get('http://www.fb.com')
time.sleep(1)
driver.maximize_window()
time.sleep(1)
driver.fullscreen_window()
time.sleep(1)
driver.minimize_window()
time.sleep(1)
driver.quit()