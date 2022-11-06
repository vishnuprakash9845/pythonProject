import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with

#How to send a cmd line argument to js
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.google.com/")

# driver.execute_script("v='Bhanu';alert(v);")
name1='Bhanu'
name2='Prakash'
driver.execute_script("p1=arguments[0];p2=arguments[1];alert(p1+' '+p2)",name1,name2)
time.sleep(4)

driver.quit()




