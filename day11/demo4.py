import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.color import Color

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Enter the url
driver.get("https://demo.actitime.com/login.do")

username = driver.find_element(By.ID,"username")
location = username.location
print(location)
x = location['x']
print("X location : "+ str(x))
y = location['y']
print("Y location : "+ str(y))

size = username.size
print(size)

height = size['height']
print("Element Height : "+ str(height))
width = size['width']
print("Element Width : "+ str(width))

driver.close()
