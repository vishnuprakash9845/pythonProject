import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.service import Service

month_year="April 2023";
date="1"

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.makemytrip.com/")

driver.find_element(By.XPATH,"//span[@class='langCardClose']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//span[contains(text(),'DEPARTURE')]").click()
time.sleep(1)
for i in range(1,12):
    try:
        xp="//div[text()='"+month_year+"']/../../div[3]//p[text()='"+date+"']"
        print(xp)
        driver.find_element(By.XPATH,xp).click()
        print('date found,select , exitting...')
        break
    except:
        print('date not found,click next ->',i)
        driver.find_element(By.XPATH,"//span[@aria-label='Next Month']").click()
        time.sleep(1)

time.sleep(3)

driver.close()
