import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
print("Default script timeout is:",driver.timeouts.script) #deafault value is 30Sec
driver.set_script_timeout(2) #used by execute_script method (JS)
print("After changing script timeout:",driver.timeouts.script)

driver.get("https://news.google.com/")
driver.execute_script("window.scrollBy(0,500)") #if this js takes more than 2 sec to execute then we get
#timeout exception

driver.close()

