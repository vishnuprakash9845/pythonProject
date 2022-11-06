import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from day24.google import GooglePage

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")
google_page = GooglePage(driver)
google_page.set_username()
time.sleep(2)
driver.close()
