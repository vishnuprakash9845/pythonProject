import time

from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

#How do u handle drag and drop

#driver=webdriver.Chrome(ChromeDriverManager().install())
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.dhtmlgoodies.com/submitted-scripts/i-google-like-drag-drop/")
driver.maximize_window()
time.sleep(2)
b1=driver.find_element(By.XPATH,"//h1[.='Block 1']")
b3=driver.find_element(By.XPATH,"//h1[.='Block 3']")
actions=ActionChains(driver)
actions.drag_and_drop(b1,b3).perform()
time.sleep(5)
