import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

#NSEE for logout link
#solution1->time.sleep(7)
#solution2->implicitly_wait
#solution3->explicit wait-> WebDriverWait
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# driver.implicitly_wait(10)

driver.get("https://demo.actitime.com/login.do")

driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
driver.find_element(By.XPATH,"//div[.='Login ']").click()
# time.sleep(7)
# wait=WebDriverWait(driver,10)
# locator=(By.ID,"logoutLink")
# wait.until(expected_conditions.visibility_of_element_located(locator))

for i in range(0,100):
    print(i)
    try:
        driver.find_element(By.ID,"logoutLink").click()
        print('logout link is present and clicked')
        break
    except:
        print('logout link is not present')


driver.quit()