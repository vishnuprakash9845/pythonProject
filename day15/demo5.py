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
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(1)
button=driver.find_element(By.XPATH,"//span[.='right click me']")
actions=ActionChains(driver)
actions.context_click(button).perform()
time.sleep(1)
driver.find_element(By.XPATH,"//span[.='Copy']").click()
time.sleep(3)