import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#How do u scroll to the bottom of the page
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.actimind.com/")
driver.maximize_window()
time.sleep(1)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(7)

driver.close()