import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#print the title of all the browsers
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample17.html")
driver.find_element(By.ID,'A5').click()
allWHS=driver.window_handles

for wh in allWHS:
    driver.switch_to.window(wh)
    print(driver.title)

time.sleep(3)
driver.quit()

