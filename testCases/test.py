import selenium
from selenium.webdriver.chrome import webdriver

baseURL = "https://admin@crosslend.com:123456XL@marketplace.staging.crosslend.net/"

driver = webdriver.Chrome(executable_path="C://Users//User//PycharmProjects//SmokeTestWebUI//drivers//chromedriver.exe")
driver.get(baseURL)
