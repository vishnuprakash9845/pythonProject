import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#Searching - Verify whether Agra is present or not in the list box
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/sample15.html")

listBox=driver.find_element(By.ID,"A1")
select=Select(listBox)
all_options=select.options

expected="Pune"
msg="Not Found"

for option in all_options:
    actual=option.text
    print("Actual:",actual)
    if actual==expected:
        msg="Found"
        break


print(expected," is ",msg)

driver.close()



