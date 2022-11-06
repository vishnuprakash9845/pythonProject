import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(1)
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//button[text()='No thanks']").click()
time.sleep(2)
driver.close()
