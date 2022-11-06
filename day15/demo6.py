import time

from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

#How do u handle context menu
#using context_click method of ActionChains class

#driver=webdriver.Chrome(ChromeDriverManager().install())
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.plus2net.com/javascript_tutorial/ondblclick-demo.php")
driver.maximize_window()
time.sleep(1)
button=driver.find_element(By.XPATH,"//input[@value='Double Click']")
actions=ActionChains(driver)
msg=driver.find_element(By.ID,'box').text
print(msg)
actions.double_click(button).perform()
msg=driver.find_element(By.ID,'box').text
print(msg)
time.sleep(1)

driver.quit()