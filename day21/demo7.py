import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#handling tabs
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("https://demo.actitime.com/login.do")
driver.find_element(By.XPATH,"//a[.='actiTIME Inc.']").click()
time.sleep(1)
allwhs=driver.window_handles
print(len(allwhs))
driver.switch_to.window(allwhs[1]) #switching from 1st tab to 2nd tab
driver.find_element(By.XPATH,"//a[text()='Try Free']").click()
time.sleep(1)
driver.close() #close the 2nd tab
time.sleep(1)
driver.switch_to.window(allwhs[0])#switching  to 1st tab
driver.close()
time.sleep(3)