import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.color import Color
#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Enter the url
driver.get("https://demo.actitime.com/login.do")

username=driver.find_element(By.ID,"username")
x=username.rect['x']
print(x)

y=username.rect['y']
print(y)

height=username.rect['height']
print(height)

width=username.rect['width']
print(width)

driver.quit()