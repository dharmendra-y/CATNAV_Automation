import logging
import time
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import datetimeutilityNew


class Test_001_KeywordSearch():
    baseURL = "http://dytest.cn-qa-stage.catnav.us/result/order-submission"
    logger = LogGen.loggen()
    def test_KyeWordSearch_1(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        self.logger.info("******************** Test_001_KeyWord Search ********************")
        self.driver.execute_script(
            "document.querySelector('plp-search').shadowRoot.querySelector('div > input').value='Item'")
        self.driver.execute_script("document.querySelector('plp-search').shadowRoot.querySelector('button').click()")
        time.sleep(5)
        Search_Text = self.driver.execute_script("return document.querySelector('plp-title').querySelector('span').innerText")
        if Search_Text =='Search Results On "Item" in All Categories':
               assert True
        else:
            assert False
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-categories-scroll').shadowRoot.querySelector('div > h4').innerText"))

        self.logger.info(self.driver.execute_script("return document.querySelector('plp-categories-scroll').shadowRoot.querySelector('div > h4').innerText"))
        assert (self.driver.execute_script(
            "return document.querySelector('plp-categories-scroll').shadowRoot.querySelector('div > h4').innerText")) == \
               "24 Categories"
        self.logger.info((self.driver.execute_script(
            "return document.querySelector('plp-header').shadowRoot.querySelector('div > span').innerText")))
        assert (self.driver.execute_script(
            "return document.querySelector('plp-header').shadowRoot.querySelector('div > span').innerText")) == \
               "281 Results"
        self.logger.info(self.driver.execute_script("return document.title;"))

        self.logger.info(self.driver.execute_script("return document.URL"))
        time.sleep(2)
        self.driver.get_screenshot_as_file("C:/Users/dharmendray/PycharmProjects/CATNAV_Automation/ScreenShots/" + datetimeutilityNew.current_time() + "_New_KyeWord_Search.png")
        self.driver.close()