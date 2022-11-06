import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#what happens if locator is not matching with any element
#w.r.t find_elements -> will return empty list
#w.r.t find_element-> will throw NoSuchElementException

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample12.html")
time.sleep(1)

all_elements=driver.find_elements(By.TAG_NAME,"output") #empty list
print(type(all_elements))
print(len(all_elements))

element=driver.find_element(By.TAG_NAME,"output")

driver.close()


