from selenium.webdriver.common.by import By


class GooglePage:
    __all_links = (By.XPATH, "//a")

    def __init__(self, driver):
        self.__driver = driver

    def count_and_print_links(self):
        links = self.__driver.find_elements(*self.__all_links);
        count = len(links)
        print("Number of links", count)
        for link in links:
            if (len(link.text) != 0):
                print(link.text)
