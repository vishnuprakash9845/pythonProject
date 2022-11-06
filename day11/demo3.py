import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.color import Color

#open the browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Enter the url
driver.get("https://demo.actitime.com/login.do")

#click on the login button-><div>Login </div>->//div[.='Login ']
driver.find_element(By.XPATH,"//div[.='Login ']").click()
time.sleep(3)

#verify the error msg
xp="//span[@class='errormsg' and not(@id)]"
errMsg=driver.find_element(By.XPATH,xp)
c=errMsg.value_of_css_property("color")
print(c) #rgba(206, 1, 0, 1)
actual_color = Color.from_string(c).hex
print(actual_color)
expected_color = "#ce0100"  #from UI design doc

if actual_color==expected_color:
    print("Pass: Err Message is Red in color")
else:
    print("Fail: Err Message is not in Red color")


actul_fontSize=errMsg.value_of_css_property("font-size")
expected_fontSize = "13px"

print("Actual Font "+actul_fontSize)
print("Expected Font "+expected_fontSize)

if actul_fontSize==expected_fontSize:
    print("Pass: Err Message font is matching to "+ expected_fontSize)
else:
    print("Fail: Err Message is not matching to "+expected_fontSize)


driver.close()
