import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.actimind.com/")
time.sleep(2)
y=driver.find_element(By.XPATH,"//a[contains(text(),'Learn')]").location['y']
print(y)
#scroll to specific element
driver.execute_script("window.scrollTo(0,"+str(y)+")")
time.sleep(3)

driver.quit()





