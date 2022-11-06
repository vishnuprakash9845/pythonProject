import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample16.html")
time.sleep(1)
driver.find_element(By.ID,"A1").click()
time.sleep(2)
alert=driver.switch_to.alert
msg=alert.text
print(msg)
alert.accept() #click ok
# alert.dismiss() # click cancel
time.sleep(2)

driver.close()