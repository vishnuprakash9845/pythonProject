import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from day25.LoginPage1 import LoginPage1

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.actitime.com/login.do")

loginpage=LoginPage1(driver)
loginpage.set_username("admin")
time.sleep(1)

driver.close()
