import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from day25.GooglePage import GooglePage

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(7)
driver.get("http://www.google.com")
gpage=GooglePage(driver)
gpage.count_and_print_links()
driver.quit()
