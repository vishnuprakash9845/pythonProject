import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#how do u handle multitple elements- using find_elements
# can we use any locator with find_elements? yes
# but frequently used locator is xpath
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/Sample13.html")
time.sleep(1)
all_textbox=driver.find_elements(By.XPATH,"//input[@type='text']")
print(len(all_textbox))

for textbox in all_textbox:
    textbox.send_keys("Bhanu")

time.sleep(2)

for i in range(len(all_textbox)- 1, -1, -1):
    all_textbox[i].send_keys("Prakash")

time.sleep(2)

driver.close()
