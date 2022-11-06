import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


#automate below steps
#open the browser and goto google.com
#open another tab and goto fb.com

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http:/www.google.com")
driver.switch_to.new_window("tab") #opens new tab and switch to it-only in selenium 4
driver.get("http:/www.fb.com")

time.sleep(3)

driver.quit()