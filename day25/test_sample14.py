import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from day25.sample14page import Sample14

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(7)
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/HTMLDemo/Sample16.html")
samplepage=Sample14(driver)
samplepage.click_submit()
time.sleep(2)
samplepage.print_alert_msg_and_closeit()
time.sleep(2)
driver.quit()
