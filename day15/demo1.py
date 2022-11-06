from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import ImageGrab
from selenium.webdriver.chrome.service import Service

#Taking Screenshot of complete Desktop using Pillow package

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://aksharatraining.com/")
ImageGrab.grab().save("desktop.png")
driver.quit()
