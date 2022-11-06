import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
pwh=driver.current_window_handle  #address of the current browser window
print(pwh)

driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample17.html")
time.sleep(1)
driver.find_element(By.ID,'A5').click()
time.sleep(1)
allWHS=driver.window_handles  #address of the all browser windows
print(len(allWHS)) #3
print(allWHS)

driver.quit()

