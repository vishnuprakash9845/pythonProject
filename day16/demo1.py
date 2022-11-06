import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///Users/vishnu/Downloads/Python-Selenium/SampleA.html")

time.sleep(1)
driver.switch_to.frame(0) #1st frame - index -int
driver.find_element(By.ID,"t2").send_keys("A")

time.sleep(1)
driver.switch_to.default_content()  #exit from frame and go to main page
driver.find_element(By.ID,"t1").send_keys("A")
time.sleep(1)

driver.switch_to.frame("f1")#using id or name -String
driver.find_element(By.ID,"t2").send_keys("B")
time.sleep(1)
driver.switch_to.default_content()  #exit from frame and go to main page
driver.find_element(By.ID,"t1").send_keys("B")
time.sleep(1)

frame_element=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(frame_element)
driver.find_element(By.ID,"t2").send_keys("C")
time.sleep(1)
driver.switch_to.parent_frame()  #exit from frame and go to main page
driver.find_element(By.ID,"t1").send_keys("C")
time.sleep(1)



driver.close()
