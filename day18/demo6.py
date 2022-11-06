import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
print("Default Implicit Wait timeout is:",driver.timeouts.implicit_wait)#default value is 0Sec
driver.implicitly_wait(10)
print("After changing Implicit Wait timeout:",driver.timeouts.implicit_wait)#10Sec

print("Default page load timeout is:", driver.timeouts.page_load)#default page load time is 300Sec->5min
driver.set_page_load_timeout(5)#change the page load time to 5sec -used by get method
print("After changing page load timeout:",driver.timeouts.page_load)#5

try:
    driver.get("http://www.google.com")#enter url and wait till page is loaded within 5sec
    #after 5sec if page is not loaded  it will throw TimeOutException
    print('Page is loaded within 5sec')
except:
    print('Page is not loaded with in 5sec')

