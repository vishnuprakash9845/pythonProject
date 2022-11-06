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
v=500
for i in range(0,5):
    print("window.scrollTo(0,"+str(v)+")")
    driver.execute_script("window.scrollTo(0,"+str(v)+")")
    time.sleep(1)
    v = v + 500

time.sleep(2)
for i in range(0,5):
    v = v - 500
    print("window.scrollTo(0,"+str(v)+")")
    driver.execute_script("window.scrollTo(0,"+str(v)+")")
    time.sleep(1)

time.sleep(2)

driver.close()

driver.quit()







