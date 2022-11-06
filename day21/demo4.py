import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#WAP to close specified browser- Akshara
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample17.html")
driver.find_element(By.ID,'A5').click()
time.sleep(1)
allwhs=driver.window_handles
for wh in allwhs:
    driver.switch_to.window(wh)
    title=driver.title
    if title=="Akshara":
        driver.close()
        break

time.sleep(3)

driver.quit()