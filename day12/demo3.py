import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with

#selenium code to take screenshot of part of the page
#png->Portable Network Graphics
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.actitime.com/login.do")
driver.find_element(By.ID,"whiteBoxWithLogo").screenshot("box.png")
driver.save_screenshot("login.png")
driver.quit()