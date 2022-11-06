from selenium import webdriver

#Open the Chrome browser
driver = webdriver.Chrome('/Users/vishnu/Downloads/chromedriver')
#Sending the URL and wait till page loads
driver.get('http://www.google.com')
#Close the browser
driver.close()