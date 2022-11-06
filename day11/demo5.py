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
password=driver.find_element(By.NAME,"pwd")

x1=username.location['x']
x2=password.location['x']

print("Username Textfield x : "+ str(x1))
print("Password Textfield x : "+ str(x2))

if x1==x2:
    print("Pass: Both the elements are aligned")
else:
    print("Fail: Both the elements are  notaligned")

driver.quit()
