import time

from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Taking Screenshot of complete page
chrome_options=webdriver.ChromeOptions()
chrome_options.headless=True #invisible browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
#driver=webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get("https://demo.actitime.com/")
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
driver.find_element(By.XPATH,"//div[.='Login ']").click()
time.sleep(4)
print(driver.title)
driver.quit()
