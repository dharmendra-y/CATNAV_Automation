

class button_clicks:
    link_addtocart_xpath = "//a[contains(text(),'Add To Cart')]"
    link_Catalogselection_xpath = "//span[normalize-space()='build22bnewdesign']"
    link_ViewCARTButton_xpath = "//div[@id='plp-popup-buttonbar']//button[@id='edit-attr-view-cart']"
    button_ProceedtoChckout_xpath = "//body/div[@id='plp-container']/section[1]/a[3]/span[1]"


    def __init__(self, driver):
        self.driver = driver

    def click_catalog_selection(self):
        self.driver.find_element_by_xpath(button_clicks.link_Catalogselection_xpath).click()

    def click_add_to_cart(self):
        self.driver.find_element_by_xpath(self.link_addtocart_xpath).click()
        #self.driver.find_element_by_xpath(self.link_addtocart_xpath).click()

    def click_view_cart(self):
        self.driver.find_element_by_xpath(button_clicks.link_ViewCARTButton_xpath).click()

    def click_proceed_to_checkout(self):
        self.driver.find_element_by_xpath(button_clicks.button_ProceedtoChckout_xpath).click()