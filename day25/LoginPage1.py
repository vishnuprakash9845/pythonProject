from selenium.webdriver.common.by import By


class LoginPage1:
    # declaration
    __unTB = (By.ID, "username")  # tuple
    __driver = None

    # initialization
    def __init__(self, driver):
        self.__driver = driver

    # utilization
    def set_username(self, un):
        # self.__driver.find_element(self.__unTB[0],self.__unTB[1]).send_keys(un)
        self.__driver.find_element(*self.__unTB).send_keys(un)
