import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///F:/B57/Sample3.html")
driver.find_element(By.LINK_TEXT,"bhanuprakashahk").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"bhanuprakashahk").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"bhanu").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"prakash").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"akash").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"asha").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"anu").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"anup").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"shah").click()
time.sleep(1)