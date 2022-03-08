from selenium.webdriver.common.by import By

class PCATLogin:
    textbox_username_id="UserName"
    textbox_password_id="Password"
    button_login_id="plpSignInLink"
    link_logout_linktext="Sign Out"
    button_signin_id='plpPCATLogin'


    def __init__(self, driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(PCATLogin.textbox_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

    def clicksignin(self):
        self.driver.find_element_by_id(self.button_signin_id).click()