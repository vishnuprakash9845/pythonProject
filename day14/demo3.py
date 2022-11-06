import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#can we find the element using xpath in JS?-->No
#only way to identify the element is xpath, and that element disable , how to perform the action
#we can xpath in selenium,but we can handle disabled element using JS

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample11.html")

time.sleep(2)
element=driver.find_element(By.XPATH,"//input[@id='A4']")
input='Akshara'
# driver.execute_script("element=arguments[0];element.value='Akshara';",element)
# driver.execute_script("arguments[0].value='Akshara';",element)
driver.execute_script("arguments[0].value=arguments[1];",element,input)
time.sleep(2)

driver.close()