import time

import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


#automate below steps in selenium 3
#open the browser and goto google.com
#open another tab and goto fb.com

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http:/www.google.com")
pyautogui.hotkey('ctrl','t')
time.sleep(1)
allWHS=driver.window_handles
driver.switch_to.window(allWHS[1])
driver.get("http:/www.fb.com")
time.sleep(3)