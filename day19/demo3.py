import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/sample15.html")
time.sleep(1)
listBox=driver.find_element(By.ID,"A1")
select=Select(listBox)
print(select.is_multiple)# None means not a multi select listbox- it is single select list box
time.sleep(1)
listBox=driver.find_element(By.ID,"A2")
select=Select(listBox)
print(select.is_multiple)# True - It is a multi select list box

driver.close()