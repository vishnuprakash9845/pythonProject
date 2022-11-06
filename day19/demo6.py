import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#count the number of options present in listbox and print all the options without using Select class
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/sample15.html")
all_options=driver.find_elements(By.XPATH,"//select[@id='A1']/option")

count=len(all_options)
print(count)
for option in all_options:
    print(option.text)

driver.close()
