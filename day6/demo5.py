import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# 1.open the browser and enter the actitime url
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.actitime.com/login.do")
# 2. enter valid user name
driver.find_element(By.CSS_SELECTOR,"input#username").send_keys("admin")
# 3.enter valid password
driver.find_element(By.CSS_SELECTOR,"input[name='pwd']").send_keys("manager")
# 4. click on login button
driver.find_element(By.CSS_SELECTOR,"a#loginButton").click()
time.sleep(5)
# 5. Verify that Home Page is Displayed
actualTitle=driver.title
print("Actual Title:"+actualTitle)

expectedTitle = "actiTIME - Enter Time-Track"
print("Expected Title:"+expectedTitle)

if(actualTitle == expectedTitle):
    print("Pass: Home Page is Displayed")
else:
    print("FAIL: Home Page is NOT Displayed")

driver.quit()