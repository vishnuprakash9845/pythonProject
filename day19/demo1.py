import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/sample14.html")
time.sleep(1)
listBox=driver.find_element(By.ID,"A1")
select=Select(listBox)
select.select_by_index(1) #index starts from 0
time.sleep(1)
select.select_by_value("c")
time.sleep(1)
select.select_by_visible_text("Delhi")
time.sleep(1)

driver.close()