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
#count the number of auto-suggestions
count=len(all_ASE)
print("Number of Auto-Suggestions:",count)

#print all the auto suggestions - (text)
for element in all_ASE:
    print(element.text)

time.sleep(2)
#select the last Auto suggestion
element.click()

time.sleep(5)