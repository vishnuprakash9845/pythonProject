import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from day24.LoginPage import LoginPage

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.actitime.com/login.do")
loginpage=LoginPage(driver)
loginpage.set_username("admin")
loginpage.set_password("manager")
loginpage.click_loginbutton()
time.sleep(2)
driver.close()