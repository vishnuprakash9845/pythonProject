from selenium.webdriver.common.by import By


class LoginPage2:
    __unTB = (By.ID, "username")
    __pwTB = (By.NAME,"pwd")
    __loginBTN = (By.XPATH,"//div[.='Login ']")
    __errMsg = (By.XPATH,"//span[contains(text(),'invalid')]")

    def __init__(self, driver):
        self.__driver = driver

    def set_username(self, un):
        self.__driver.find_element(*self.__unTB).send_keys(un)

    def set_password(self,pw):
        self.__driver.find_element(*self.__pwTB).send_keys(pw)

    def click_loginbutton(self):
        self.__driver.find_element(*self.__loginBTN).click()

    def get_errmsg_text(self):
        return self.__driver.find_element(*self.__errMsg).text