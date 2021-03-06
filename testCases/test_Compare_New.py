import logging
import time
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import datetimeutilityNew

class Test_Compare_Item:

    baseURL = "https://build49-legacy.cn-qa-stage.catnav.us/result/ll-categories-home-page-created-from-am-cat1testam?plpver=1155"
    logger = LogGen.loggen()


    def test_CompareItem_1(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.maximize_window()
        time.sleep(2)
        #Item 1 Compare click
        self.logger.info("******************** Compare Item clicked ********************")
        self.driver.execute_script("return document.querySelector('plp-item-results > plp-thumbnail >plp-compareitem').shadowRoot.querySelector('a > span#compareitemText')").click()
        time.sleep(2)
        Compare_Button_Click2 = self.driver.execute_script("return document.querySelector('plp-item-results > plp-thumbnail:nth-child(2)>plp-compareitem').shadowRoot.querySelector('a > span#compareitemText')")
        self.driver.execute_script("arguments[0].click();", Compare_Button_Click2)
        time.sleep(3)
        #Item 1 Compare click
        self.logger.info("******************** Compare button clicked ********************")
        self.logger.info(self.driver.execute_script("return document.querySelector('plp-itemcard').shadowRoot.querySelector('div > div > div:nth-child(2)').innerText"))
        time.sleep(1)
        self.logger.info(self.driver.execute_script("return document.querySelector('plp-itemsqueue > plp-itemcard:nth-child(2)').shadowRoot.querySelector('div > div > div:nth-child(2)').innerText"))

        self.driver.execute_script("return document.querySelector('plp-itemsqueue').shadowRoot.querySelector('#btnCompare')").click()
        time.sleep(2)

        self.driver.close()


    def test_CompareItem_2(self, setup):
        self.logger.info("******************** Test case 2 started ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.maximize_window()
        time.sleep(2)
        # Item 1 Compare click
        self.logger.info("******************** Compare Item clicked ********************")
        self.driver.execute_script("return document.querySelector('plp-item-results > plp-thumbnail >plp-compareitem').shadowRoot.querySelector('a > span#compareitemText')").click()
        time.sleep(2)
        Compare_Button_Click2 = self.driver.execute_script("return document.querySelector('plp-item-results > plp-thumbnail:nth-child(2)>plp-compareitem').shadowRoot.querySelector('a > span#compareitemText')")
        self.driver.execute_script("arguments[0].click();", Compare_Button_Click2)
        time.sleep(3)
        self.logger.info("******************** Clear all Button Clicked ********************")
        # Clear all button click
        Clearall_Click = self.driver.execute_script("return document.querySelector('plp-itemsqueue').shadowRoot.querySelector('#btnClearAll')")
        self.driver.execute_script("arguments[0].click();", Clearall_Click)
        time.sleep(1)

        time.sleep(1)
        self.driver.close()