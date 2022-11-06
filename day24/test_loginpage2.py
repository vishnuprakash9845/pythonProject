import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from day24.LoginPage import LoginPage

#open the browser and enter the url
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(7)
driver.get("https://demo.actitime.com/login.do")
#enter only username and click login
loginpage=LoginPage(driver)
loginpage.set_username("admin")
loginpage.click_loginbutton()
#print error msg
msg=driver.find_element(By.XPATH,"//span[contains(text(),'invalid')]").text
print(msg)
#enter only password & click login
loginpage.set_password("manager")
loginpage.click_loginbutton()
#print error msg
msg=driver.find_element(By.XPATH,"//span[contains(text(),'invalid')]").text
print(msg)