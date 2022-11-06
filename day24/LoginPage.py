from selenium.webdriver.common.by import By


class LoginPage:
    #declaration
    __unTB= None
    __pwTB= None
    __loginBTN =None

    #initialization
    def __init__(self,driver):
        self.__unTB=driver.find_element(By.ID, "username")
        self.__pwTB=driver.find_element(By.NAME, "pwd")
        self.__loginBTN=driver.find_element(By.XPATH, "//div[.='Login ']")

    #utilization
    def set_username(self,un):
        self.__unTB.send_keys(un)

    def set_password(self,pw):
        self.__pwTB.send_keys(pw)

    def click_loginbutton(self):
        self.__loginBTN.click()
