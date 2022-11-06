import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome(ChromeDriverManager().install())
wait=WebDriverWait(driver,10)
driver.maximize_window()
driver.get("https://demo.actitime.com/login.do")

driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
driver.find_element(By.XPATH,"//div[.='Login ']").click()


wait.until(expected_conditions.title_contains("Enter"))
print("Title after login:",driver.title)

driver.find_element(By.ID,"logoutLink").click()
wait.until(expected_conditions.title_contains("Login"))
print("Title after logout:",driver.title)