from selenium.webdriver import Chrome

#Open the Chrome browser
driver = Chrome('/Users/vishnu/Downloads/chromedriver')
#Sending the URL and wait till page loads
driver.get('http://www.google.com')
#Close the browser
driver.close()