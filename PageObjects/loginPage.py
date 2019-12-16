class loginPage():
    #locators of the login Page
    textbox_username_xpath = "//input[@id='login-email-input']"
    textbox_password_xpath = "//input[@id='login-password-input']"
    button_login_xpath = "//*[@type='submit' and @class='btn btn-primary' and contains(text(),'Log in')]"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,userName):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(userName)

    def setpassword(self,password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickonLogin(self):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).click()



