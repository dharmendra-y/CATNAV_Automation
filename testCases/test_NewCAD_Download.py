import time

from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import datetimeutilityNew

class Test_001_CAD_Form_Submission:
    baseURL = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()

    def test_CAD_Submission_3D(self, setup):
        self.logger.info("********************Test_001_CAD_Submission_3D********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(20)
        self.driver.execute_script("return document.querySelector('plp-thumbnail').shadowRoot.querySelector('div > div:nth-child(3) > a')").click()
        time.sleep(5)
        self.driver.execute_script("return document.querySelector('plp-button#downloadCadBtn').shadowRoot.querySelector('button#downloadCadBtn > span')").click()
        time.sleep(2)
        Formate_Selection = self.driver.execute_script("return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.dropdown-container > div >a:nth-child(2)')")
        self.driver.execute_script("arguments[0].click();", Formate_Selection)
        time.sleep(2)
        self.logger.info(self.driver.execute_script("return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script("return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#radiobtn-container > div:nth-child(1) >label').innerText"))
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input').value='First Name'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-1').value='Orion'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-2').value='dharmendray@orioninc.com'")
        self.driver.execute_script("return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-3').value='Project Name - 3D'")
        time.sleep(3)
        
        CAD_Download = self.driver.execute_script("return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#downloadCadBtn').shadowRoot.querySelector('#downloadCadBtn > span')")
        self.driver.execute_script("arguments[0].click();", CAD_Download)
        time.sleep(10)
        
        self.logger.info(self.driver.execute_script("return document.title"))
        
        self.logger.info(self.driver.execute_script("return document.querySelector('plp-alert').shadowRoot.querySelector('#alert > span:nth-child(2)').innerText"))
        time.sleep(3)
        self.driver.get_screenshot_as_file("C:/Users/dharmendray/PycharmProjects/CATNAV_Automation/ScreenShots/" + datetimeutilityNew.current_time() + "_3D.png")
        self.logger.info(self.driver.execute_script("return document.URL"))
        self.driver.close()

    def test_CAD_Submission_2D_Front_View(self, setup):
        self.logger.info("********************Test_002_CAD_Submission_2D********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-thumbnail').shadowRoot.querySelector('div > div:nth-child(3) > a')").click()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-button#downloadCadBtn').shadowRoot.querySelector('button#downloadCadBtn > span')").click()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#radiobtn-container > div:nth-child(2) >input#inputCadType1')").click()
        Formate_Selection = self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.dropdown-container > div >a:nth-child(2)')")
        self.driver.execute_script("arguments[0].click();", Formate_Selection)
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#radiobtn-container > div:nth-child(2) >label').innerText"))
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input').value='First Name'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-1').value='Orion'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-2').value='dharmendray@orioninc.com'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-3').value='Project Name - 3D'")
        time.sleep(3)

        CAD_Download = self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#downloadCadBtn').shadowRoot.querySelector('#downloadCadBtn > span')")
        self.driver.execute_script("arguments[0].click();", CAD_Download)
        time.sleep(10)

        self.logger.info(self.driver.execute_script("return document.title"))

        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-alert').shadowRoot.querySelector('#alert > span:nth-child(2)').innerText"))
        time.sleep(3)
        self.driver.get_screenshot_as_file(
            "C:/Users/dharmendray/PycharmProjects/CATNAV_Automation/ScreenShots/" + datetimeutilityNew.current_time() + "_2D_Front.png")
        self.logger.info(self.driver.execute_script("return document.URL"))
        self.driver.close()

    def test_CAD_Submission_2D_Left_Side_View(self, setup):
        self.logger.info("******************** Test_003_CAD_Submission_2D Left Side View ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-thumbnail').shadowRoot.querySelector('div > div:nth-child(3) > a')").click()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-button#downloadCadBtn').shadowRoot.querySelector('button#downloadCadBtn > span')").click()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#radiobtn-container > div:nth-child(3) >input#inputCadType2')").click()
        Formate_Selection = self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.dropdown-container > div >a:nth-child(2)')")
        self.driver.execute_script("arguments[0].click();", Formate_Selection)
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#radiobtn-container > div:nth-child(3) >label').innerText"))
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input').value='First Name'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-1').value='Orion'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-2').value='dharmendray@orioninc.com'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-3').value='Project Name - 3D'")
        time.sleep(3)

        CAD_Download = self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#downloadCadBtn').shadowRoot.querySelector('#downloadCadBtn > span')")
        self.driver.execute_script("arguments[0].click();", CAD_Download)
        time.sleep(10)

        self.logger.info(self.driver.execute_script("return document.title"))

        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-alert').shadowRoot.querySelector('#alert > span:nth-child(2)').innerText"))
        time.sleep(3)
        self.driver.get_screenshot_as_file(
            "C:/Users/dharmendray/PycharmProjects/CATNAV_Automation/ScreenShots/" + datetimeutilityNew.current_time() + "_2D_Left.png")
        self.logger.info(self.driver.execute_script("return document.URL"))
        self.driver.close()

    def test_CAD_Submission_2D_Top_View(self, setup):
        self.logger.info("******************** Test_004_CAD_Submission_2D Top Side ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-thumbnail').shadowRoot.querySelector('div > div:nth-child(3) > a')").click()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-button#downloadCadBtn').shadowRoot.querySelector('button#downloadCadBtn > span')").click()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#radiobtn-container > div:nth-child(4) >input#inputCadType3')").click()
        Formate_Selection = self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.dropdown-container > div >a:nth-child(2)')")
        self.driver.execute_script("arguments[0].click();", Formate_Selection)
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#radiobtn-container > div:nth-child(4) >label').innerText"))
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input').value='First Name'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-1').value='Orion'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-2').value='dharmendray@orioninc.com'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-3').value='Project Name - 3D'")
        time.sleep(3)

        CAD_Download = self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#downloadCadBtn').shadowRoot.querySelector('#downloadCadBtn > span')")
        self.driver.execute_script("arguments[0].click();", CAD_Download)
        time.sleep(10)

        self.logger.info(self.driver.execute_script("return document.title"))

        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-alert').shadowRoot.querySelector('#alert > span:nth-child(2)').innerText"))
        time.sleep(3)
        self.driver.get_screenshot_as_file(
            "C:/Users/dharmendray/PycharmProjects/CATNAV_Automation/ScreenShots/" + datetimeutilityNew.current_time() + "_2D_Top.png")
        self.logger.info(self.driver.execute_script("return document.URL"))
        self.driver.close()

    def test_CAD_Submission_2D_Bottom_View(self, setup):
        self.logger.info("******************** Test_005_CAD_Submission_2D Bottom View ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-thumbnail').shadowRoot.querySelector('div > div:nth-child(3) > a')").click()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-button#downloadCadBtn').shadowRoot.querySelector('button#downloadCadBtn > span')").click()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#radiobtn-container > div:nth-child(5) >input#inputCadType4')").click()
        Formate_Selection = self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.dropdown-container > div >a:nth-child(2)')")
        self.driver.execute_script("arguments[0].click();", Formate_Selection)
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#radiobtn-container > div:nth-child(5) >label').innerText"))
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input').value='First Name'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-1').value='Orion'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-2').value='dharmendray@orioninc.com'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-3').value='Project Name - 3D'")
        time.sleep(3)

        CAD_Download = self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#downloadCadBtn').shadowRoot.querySelector('#downloadCadBtn > span')")
        self.driver.execute_script("arguments[0].click();", CAD_Download)
        time.sleep(10)

        self.logger.info(self.driver.execute_script("return document.title"))

        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-alert').shadowRoot.querySelector('#alert > span:nth-child(2)').innerText"))
        time.sleep(3)
        self.driver.get_screenshot_as_file(
            "C:/Users/dharmendray/PycharmProjects/CATNAV_Automation/ScreenShots/" + datetimeutilityNew.current_time() + "_2D_Bottom.png")
        self.logger.info(self.driver.execute_script("return document.URL"))
        self.driver.close()


    def test_CAD_Submission_Revit_Model(self, setup):
        self.logger.info("******************** Test_006_CAD_Submission_Revit Model ********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-thumbnail').shadowRoot.querySelector('div > div:nth-child(3) > a')").click()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-button#downloadCadBtn').shadowRoot.querySelector('button#downloadCadBtn > span')").click()
        time.sleep(2)
        self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#radiobtn-container > div:nth-child(6) >input#inputCadType5')").click()
        Formate_Selection = self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.dropdown-container > div >a:nth-child(2)')")
        self.driver.execute_script("arguments[0].click();", Formate_Selection)
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('.modal-body > div:nth-child(2)').innerText"))
        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#radiobtn-container > div:nth-child(6) >label').innerText"))
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input').value='First Name'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-1').value='Orion'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-2').value='dharmendray@orioninc.com'")
        self.driver.execute_script(
            "return document.querySelector('plp-quick-cad-download-form').shadowRoot.querySelector('input#input-child-3').value='Project Name - 3D'")
        time.sleep(3)

        CAD_Download = self.driver.execute_script(
            "return document.querySelector('plp-cad-download-form').shadowRoot.querySelector('#downloadCadBtn').shadowRoot.querySelector('#downloadCadBtn > span')")
        self.driver.execute_script("arguments[0].click();", CAD_Download)
        time.sleep(10)

        self.logger.info(self.driver.execute_script("return document.title"))

        self.logger.info(self.driver.execute_script(
            "return document.querySelector('plp-alert').shadowRoot.querySelector('#alert > span:nth-child(2)').innerText"))
        time.sleep(3)
        self.driver.get_screenshot_as_file(
            "C:/Users/dharmendray/PycharmProjects/CATNAV_Automation/ScreenShots/" + datetimeutilityNew.current_time() + "_Revit.png")
        self.logger.info(self.driver.execute_script("return document.URL"))
        self.driver.close()