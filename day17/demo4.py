import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#how do you select last Auto suggestions
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("Selenium")
time.sleep(2)
all_ASE=driver.find_elements(By.XPATH,"//ul[@role='listbox']/li")
for element in all_ASE:
    print(element.text)

driver.close()
