import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#count the number of options present in listbox and print all the options
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/sample15.html")
listBox=driver.find_element(By.ID,"A3")
select=Select(listBox)
only_selected_options= select.all_selected_options
count=len(only_selected_options)
print(count)

for option in only_selected_options:
    print(option.text)

driver.close()