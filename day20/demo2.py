import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample16.html")
time.sleep(1)
driver.find_element(By.ID,"A2").send_keys("/Users/vishnu/Downloads/APIs.pdf");
time.sleep(7)

driver.close()
