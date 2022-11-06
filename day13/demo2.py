import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.actimind.com/")
time.sleep(2)

#scroll down
for i in range(0,5):
    print(i)
    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(1)

#scroll up
for i in range(0,5):
    print(i)
    driver.execute_script("window.scrollBy(0,-500)")
    time.sleep(1)


driver.quit()

















