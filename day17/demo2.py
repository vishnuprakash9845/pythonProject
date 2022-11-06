import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#how do you handle Auto suggestions
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("selenium")
time.sleep(2)
all_ASE=driver.find_elements(By.XPATH,"//span[contains(text(),'selenium')]")
time.sleep(2)
expected_text="selenium webdriver"
for element in all_ASE:
    actual_text=element.text
    print(actual_text)
    if actual_text==expected_text:
        element.click()
        break

time.sleep(3)

driver.close()