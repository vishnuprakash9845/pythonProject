import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class GooglePage:
    __unTB = None  # declaration

    def __init__(self):
        self.__unTB = driver.find_element(By.NAME, "q")  # initialization

    def set_username(self):
        self.__unTB.send_keys("selenium")  # utilization


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")
google_page = GooglePage()
google_page.set_username()
time.sleep(2)

driver.close()
