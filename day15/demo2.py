from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Taking Screenshot of complete page
chrome_options=webdriver.ChromeOptions()
chrome_options.headless=True #invisible browser
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
#driver=webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get("https://aksharatraining.com/")
size=driver.get_window_size()
width=size['width']
height1=size['height']
print("height of the browser:",height1)
height2=driver.execute_script("return document.body.scrollHeight")
print("height of the page:",height2)

driver.set_window_size(width,height2)

driver.get_screenshot_as_file("fullpage.png")

driver.quit()