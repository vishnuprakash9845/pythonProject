import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#Searching - Verify whether Agra is present or not in the list box
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/sample15.html")

listBox=driver.find_element(By.ID,"A3")
select=Select(listBox)
all_options=select.options
list2 = []
print(type(list2))

all_jobs = [job.text for job in all_options]
print(type(all_jobs))
print(all_jobs)

for option in all_options:
    actual=option.text
    #print("Actual:",actual)
    list2.append(actual)
    list2.sort()

print(list2)

driver.close()



