import logging
import time
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import datetimeutilityNew

class Compare_Item():

    baseURL = "https://build49-legacy.cn-qa-stage.catnav.us/result/ll-categories-home-page-created-from-am-cat1testam?plpver=1155"
    logger = LogGen.loggen()
    def test_CompareItem_1(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)
        #Item 1 Compare click

        driver.execute_script("return document.querySelector('plp-item-results > plp-thumbnail >plp-compareitem').shadowRoot.querySelector('a > span#compareitemText')").click()
        time.sleep(2)
        Compare_Button_Click2 = driver.execute_script("return document.querySelector('plp-item-results > plp-thumbnail:nth-child(2)>plp-compareitem').shadowRoot.querySelector('a > span#compareitemText')")
        driver.execute_script("arguments[0].click();", Compare_Button_Click2)
        time.sleep(3)

        #Clear all button click
        # Clearall_Click = driver.execute_script("return document.querySelector('plp-itemsqueue').shadowRoot.querySelector('#btnClearAll')")
        # driver.execute_script("arguments[0].click();", Clearall_Click)
        # time.sleep(1)

        driver.execute_script("return document.querySelector('plp-itemsqueue').shadowRoot.querySelector('#btnCompare')").click()
        #Compare_Click = driver.execute_script("return document.querySelector('plp-itemsqueue').shadowRoot.querySelector('#btnCompare')")

        #driver.execute_script("arguments[0].click();", Compare_Click)
        time.sleep(1)

        print(driver.execute_script("return document.title;"))

        print(driver.execute_script("return document.URL"))

        driver.close()