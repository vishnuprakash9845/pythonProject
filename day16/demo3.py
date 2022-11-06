import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample12.html")
time.sleep(1)
element=driver.find_element(By.TAG_NAME,"input")
print(type(element))

all_elements=driver.find_elements(By.TAG_NAME,"input")
print(type(all_elements))
print(len(all_elements))
element1=all_elements[0]
print(type(element1))

all_elements[0].send_keys("Bhanu")
all_elements[1].send_keys("Bhanu")
#all_elements[2].send_keys("Bhanu") #list index out of range
time.sleep(2)

driver.close()