import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from day25.LoginPage2 import LoginPage2

#open the browser and enter the url
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(7)
driver.get("https://demo.actitime.com/login.do")
#enter only username and click login
loginpage=LoginPage2(driver)
loginpage.set_username("admin")
loginpage.click_loginbutton()
time.sleep(2)
#print error msg
msg=loginpage.get_errmsg_text()
print(msg)
#enter only password & click login
loginpage.set_password("manager")
loginpage.click_loginbutton()
time.sleep(2)
#print error msg
msg=loginpage.get_errmsg_text()
print(msg)

driver.close()