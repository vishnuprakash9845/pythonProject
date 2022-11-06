import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#automate below steps
#open the browser and goto google.com
#open another browser and goto fb.com

# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get("http:/www.google.com")
#
# driver2=webdriver.Chrome(ChromeDriverManager().install())
# driver2.get("http:/www.fb.com")
#
# driver.quit()
# driver2.quit()
# time.sleep(10)

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http:/www.google.com")

#open new broswer as child for the 1st browser & auto swtich to child browser
driver.switch_to.new_window("window") #opens new window - in selenium 4
driver.get("http:/www.fb.com")

time.sleep(3)

driver.quit()