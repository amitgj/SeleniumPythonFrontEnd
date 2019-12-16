import time
import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append("C://Users//User//PycharmProjects//SmokeTestWebUI")
from PageObjects.loginPage import loginPage


class LoginTest(unittest.TestCase):
    baseURL = "https://marketplace.staging.crosslend.net/"#"https://admin@crosslend.com:123456XL@marketplace.staging.crosslend.net/"

    driver = webdriver.Chrome(executable_path="C://Users//User//PycharmProjects//SmokeTestWebUI//drivers//chromedriver.exe")
    username = "admin@crosslend.com"
    password = "123456XL"


    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        time.sleep(4)
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(5)

    def test_login(self):
        lp= loginPage(self.driver)
        lp.setUsername(self.username)
        lp.setpassword(self.password)
        lp.clickonLogin()
        time.sleep(3)
        self.assertEqual("Marketplace", self.driver.title, "Webpage Title does not match")

    @classmethod
    def tearDown(cls):
        cls.driver.close()

if __name__ =="__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="C://Users//User//PycharmProjects//SmokeTestWebUI//reports")
    )



