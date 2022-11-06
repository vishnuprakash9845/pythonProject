import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#Enter the url
driver.get("https://demo.actitime.com/login.do")
#click on the login button-><div>Login </div>->//div[.='Login ']
driver.find_element(By.XPATH,"//div[.='Login ']").click()
time.sleep(3)
#verify the error msg
xp="//span[@class='errormsg' and not(@id)]"
errMsg=driver.find_element(By.XPATH,xp)
actul_msg=errMsg.text
expected_msg="Username or Password is invalid. Please try again."
print("Expected  Err Msg is:"+expected_msg)
print("Actual Err Msg is:"+actul_msg)
if actul_msg==expected_msg:
    print("Pass:Err Msg is Valid")
else:
    print("Fail:Err Msg is invalid")
driver.quit()



