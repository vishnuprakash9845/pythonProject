from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# driver = Chrome('/Users/vishnu/Downloads/chromedriver') #absolute path
# driver = Chrome('./../driver/chromedriver') # relative

#Open the Chrome browser
driver = webdriver.Chrome(service=Service("./../driver/chromedriver"))

#Sending the URL and wait till page loads
driver.get('http://www.google.com')

#get the title and print it
print(driver.title)

#Close the browser
driver.close()