import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument("--disable-notifications") #specify the setting so that no notification popup is displayed
driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)#open the browser with above specified settings
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample17.html")
time.sleep(1)
driver.find_element(By.ID,'A6').click()
driver.find_element(By.XPATH,"//button[text()='OK']").click()
time.sleep(1)
driver.find_element(By.XPATH,"(//input[@role='searchbox'])[1]").send_keys("bhanu")
time.sleep(5)

driver.close()

