import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#how do you select last Auto suggestions
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("selenium")
time.sleep(2)
all_ASE=driver.find_elements(By.XPATH,"//span[contains(text(),'selenium')]")
time.sleep(2)
count=len(all_ASE)
# all_ASE[count-1].click()
# time.sleep(5)

for element in all_ASE:
    pass

# element.click()
# time.sleep(5)
driver.find_element(By.XPATH,"(//span[contains(text(),'selenium')])[last()]").click()
time.sleep(5)