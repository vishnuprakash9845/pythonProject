import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with
#

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///F:/B57/Sample11.html")
time.sleep(1)
# driver.find_element(By.ID,"A8").click()
driver.find_element(By.ID,"A8").submit()
time.sleep(3)
