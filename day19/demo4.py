import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/sample15.html")
listBox=driver.find_element(By.ID,"A2")
select=Select(listBox)
print(select.is_multiple)
time.sleep(1)
select.select_by_index(0)
time.sleep(1)
select.select_by_value("b")
time.sleep(1)
select.select_by_visible_text("Snacks")
time.sleep(1)
select.deselect_by_index(0)
time.sleep(1)
select.deselect_by_value("b")
time.sleep(1)
select.deselect_by_visible_text("Snacks")
time.sleep(1)

listBox=driver.find_element(By.ID,"A3")
select=Select(listBox)
select.deselect_all()
time.sleep(3)

driver.close()