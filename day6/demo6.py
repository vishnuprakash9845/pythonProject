import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# 1.open the browser and enter the actitime url
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
# 2. enter valid user name
driver.find_element(By.NAME,'username').send_keys("Admin")
# 3.enter valid password
driver.find_element(By.NAME,"password").send_keys("admin123")
# 4. click on login button
driver.find_element(By.CSS_SELECTOR,".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
time.sleep(5)
# 5. Verify that Home Page is Displayed
actualURL=driver.current_url
print("Actual Title:"+actualURL)

expectedURL = "viewEmployeeList"
print("Expected Title:"+expectedURL)

if expectedURL in actualURL:
    print("Pass: Home Page is Displayed")
else:
    print("FAIL: Home Page is NOT Displayed")

driver.quit()