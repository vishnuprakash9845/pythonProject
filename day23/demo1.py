import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as Chrome_Options

#open chrome browser in local system
# driver=webdriver.Chrome(ChromeDriverManager().install())
driver=webdriver.Remote("http://192.168.0.109:4444",options=Chrome_Options())

#grid_url="https://oauth-vishnuprakash9845-72049:0c6acebc-0f1b-4d79-b981-efdf0b2ca98e@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
#driver=webdriver.Remote(grid_url,options=Chrome_Options())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://aksharatraining.com")
print(driver.title)
time.sleep(5)
driver.quit()