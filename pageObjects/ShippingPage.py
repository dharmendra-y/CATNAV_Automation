from selenium.webdriver.common.by import By


class shipping_page_info:

    textbox_firstname_xpath = "//input[@name='FirstName']"


    def __init__(self, driver):
        self.driver = driver

    def s_firstname(self, ship_firstname):
        self.driver.find_element_by_xpath(shipping_page_info.textbox_firstname_xpath).clear()
        self.driver.find_element_by_xpath(shipping_page_info.textbox_firstname_xpath).send_keys(ship_firstname)

