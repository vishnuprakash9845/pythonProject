import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#WAP to close only child browser
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample17.html")
driver.find_element(By.ID,'A5').click()
time.sleep(1)
allwhs=driver.window_handles
n=len(allwhs)
for i in range(1,n):
    driver.switch_to.window(allwhs[i])
    driver.close()
    time.sleep(1)

time.sleep(10)