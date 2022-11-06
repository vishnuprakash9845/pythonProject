import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/sample14b.html")
time.sleep(1)
# listBox=driver.find_element(By.ID,"A1")
listBox=driver.find_element(By.ID,"t2")
#if this element is not listbox then in select class we get UnexpectedTagNameException
select=Select(listBox)
# select.select_by_index(4) #index starts from 0
# time.sleep(1)
# select.select_by_value("C")
# time.sleep(1)
# select.select_by_visible_text("delhi")
# time.sleep(1)