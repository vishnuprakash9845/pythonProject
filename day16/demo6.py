import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#count the number of links present on the page
#print text of all the links present on the page

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.google.com")
time.sleep(1)
all_links=driver.find_elements(By.XPATH,"//a")
print(len(all_links))

for link in all_links:
    print(link.text,link.is_displayed())

driver.close()

