from selenium.webdriver.common.by import By


class Sample14:
    __submit = (By.ID, "A1")

    def __init__(self, driver):
        self.__driver = driver

    def click_submit(self):
        self.__driver.find_element(*self.__submit).click()

    def print_alert_msg_and_closeit(self):
        alert = self.__driver.switch_to.alert
        print(alert.text)
        alert.accept()
