from selenium.webdriver.common.by import By


class GooglePage:
    __search = None  # declaration

    def __init__(self,driver):
        self.__search = driver.find_element(By.NAME, "q")  # initialization

    def set_username(self):
        self.__search.send_keys("selenium")  # utilization