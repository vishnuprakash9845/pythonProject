import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
print("Title after opening the browser:",driver.title) #blank
driver.get("https://demo.actitime.com/login.do") #enter url & wait till page is loaded
print("Title after entering the url:",driver.title) #it will get the title only after page is loaded
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
driver.find_element(By.XPATH,"//div[.='Login ']").click()
print("Title after login:",driver.title)#get the title immediately after click on login button
#driver.title does not use implicit wait

driver.close()