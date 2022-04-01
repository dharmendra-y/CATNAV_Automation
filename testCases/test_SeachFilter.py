import logging
import time
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import datetimeutilityNew


class Test_001_SearchFilter():
    baseURL = "https://build49-legacy.cn-qa-pub.catnav.us/result/e-flex-drives?plpver=1155"
    logger = LogGen.loggen()
    def test_SearchFilter_1(self, setup):
        self.logger.info("********** Test_001 | Test for Single Attribute Selection **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        self.logger.info("Search Filter page loaded")
        time.sleep(2)
        self.logger.info(self.driver.execute_script("return document.querySelector('plp-header').shadowRoot.querySelector('div > span#spanCount').innerText"))
        self.driver.execute_script("return document.querySelector('plp-checkbox').shadowRoot.querySelector('div > div> div> input')").click()
        self.logger.info("Attribute OUTPUT AMPERE RATING | Checkbox selected for '10.06'")
        time.sleep(2)
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-header').shadowRoot.querySelector('div > span#spanCount').innerText"))
        self.driver.close()

    def test_SearchFilter_2(self, setup):
        self.logger.info("********** Test_002 | Test for Multiple Attribute Selection **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        self.logger.info("Search Filter page loaded")
        time.sleep(2)
        self.logger.info(self.driver.execute_script("return document.querySelector('plp-header').shadowRoot.querySelector('div > span#spanCount').innerText"))
        self.driver.execute_script("return document.querySelector('plp-checkbox').shadowRoot.querySelector('div > div> div> input')").click()
        self.logger.info("Attribute OUTPUT AMPERE RATING | Checkbox selected for '10.06'")
        time.sleep(2)
        self.driver.execute_script("return document.querySelector('plp-checkbox:nth-child(4)').shadowRoot.querySelector('#lblCheckboxValue')").click()
        self.logger.info("Attribute ENCLOSURE RATING | Checkbox selected for 'Type 1'")
        time.sleep(2)
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-header').shadowRoot.querySelector('div > span#spanCount').innerText"))
        self.driver.close()

    def test_SearchFilter_3(self, setup):
        self.logger.info("********** Test_003 | Test for No Results Found **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        self.logger.info("Search Filter page loaded")
        time.sleep(2)
        self.logger.info(self.driver.execute_script("return document.querySelector('plp-header').shadowRoot.querySelector('div > span#spanCount').innerText"))
        self.driver.execute_script("return document.querySelector('plp-checkbox').shadowRoot.querySelector('div > div> div> input')").click()
        self.logger.info("Attribute OUTPUT AMPERE RATING | Checkbox selected for '10.06'")
        time.sleep(2)
        self.driver.execute_script("return document.querySelector('plp-checkbox:nth-child(4)').shadowRoot.querySelector('#lblCheckboxValue')").click()
        self.logger.info("Attribute ENCLOSURE RATING | Checkbox selected for 'Type 1'")
        time.sleep(2)
        self.driver.execute_script("return document.querySelector('plp-checkbox:nth-child(6)').shadowRoot.querySelector('#divChkItem >#B')").click()
        self.logger.info("Attribute FRAME SIZE | Checkbox selected for 'B'")
        time.sleep(2)
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-header').shadowRoot.querySelector('div > span#spanCount').innerText"))

        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-item-results').shadowRoot.querySelector('div > #spanNoRecordMsg').innerHTML"))
        time.sleep(2)
        self.driver.close()



