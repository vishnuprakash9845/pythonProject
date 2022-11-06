import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")

class GooglePage:
    __unTB=driver.find_element(By.NAME,"q")

    def set_username(self):
        self.__unTB.send_keys("selenium")



google_page=GooglePage()
google_page.set_username()
time.sleep(2)


