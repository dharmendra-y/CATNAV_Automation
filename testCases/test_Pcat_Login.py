
import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import datetimeutilityNew
from pageObjects.PCAT import PCATLogin
from pageObjects.Buttons import button_clicks
from pageObjects.ShippingPage import shipping_page_info
#tst Auto Build test tetrt yt

class Test_003_PCAT_Test:
    baseURL = "http://build49-legacy.cn-qam-pub.catnav.us/item/-categories-home-page-flstest-calculated-attribute/all-categories-flstest-shipping-and-freight/test-shipping"
    username = ReadConfig.getUserName()
    password =ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_Login_1(self, setup):
        self.driver = setup
        pcatlogin = PCATLogin(setup)
        self.driver.get(self.baseURL)
        self.logger.info("******************** Login Test Started ********************")
        time.sleep(5)
        pcatlogin.clicklogin()
        pcatlogin.setUserName(self.username)
        pcatlogin.setpassword(self.password)
        pcatlogin.clicksignin()
        self.logger.info("******************** Login Successful ********************")
        buttonclick = button_clicks(setup)
        time.sleep(5)
        buttonclick.click_catalog_selection()
        time.sleep(5)
        self.logger.info("******************** Catalog Selected Successfully ********************")
        buttonclick.click_add_to_cart()
        self.logger.info("******************** Add to CART clicked Successfully ********************")
        time.sleep(10)
        buttonclick.click_view_cart()
        self.logger.info("******************** View CART (AO PAGE) clicked Successfully ********************")
        time.sleep(5)
        buttonclick.click_proceed_to_checkout()
        self.logger.info("******************** Proceed to Checkout clicked Successfully ********************")
        time.sleep(5)
        shipping=shipping_page_info(setup)
        shipping.s_firstname(ReadConfig.getFirstName())
        time.sleep(5)
        self.logger.info("******************** Shipping First Name Provided ********************")
        self.driver.close()
