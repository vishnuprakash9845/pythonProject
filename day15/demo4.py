import time

from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

#How do u handle drop down menu
#using move_to_element method of ActionChains class
#we must call perform() at the end

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.actimind.com/")
driver.maximize_window()
xp="//a[contains(.,'AREAS OF EXPERTISE')]"
menu_element=driver.find_element(By.XPATH,xp)
actions=ActionChains(driver)
actions.move_to_element(menu_element).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//a[.='Web Crawling']").click()
time.sleep(4)

driver.quit()