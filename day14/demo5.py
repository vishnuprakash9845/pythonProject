import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#scrolling the inner scrollbar

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://news.google.com/")
driver.maximize_window()
time.sleep(2)
for i in range(1,4):
    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(1)
time.sleep(1)
help_element=driver.find_element(By.XPATH,"//span[text()='Help']")
driver.execute_script("arguments[0].scrollIntoView()",help_element)
time.sleep(7)


driver.close()