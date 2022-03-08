from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "Edge":
        driver = webdriver.Edge(executable_path="C:\\Selenium_Browser_Drivers\\msedgedriver.exe")
    elif browser == "Firefox":
        driver = webdriver.Firefox (executable_path="C:\\Selenium_Browser_Drivers\\geckodriver.exe")
    elif browser == "Chrome":
        #driver = webdriver.Chrome(service=s)
        driver = webdriver.Chrome(executable_path= "C:\\Selenium_Browser_Drivers\\chromedriver.exe")
    elif browser == "Ie":
        driver = webdriver.Ie(executable_path="C:\\Selenium_Browser_Drivers\\IEDriverServer_64.exe")
    return driver


def pytest_addoption(parser):
    parser.addoption('--browser',action="store", default="Edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')
    #return request.config.getoption('--html')

############## PyTest HTML Report ##############

# It is Hooks for adding Environment Info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'NEW PLP'
    config._metadata['Module Name'] = 'NEW PLP Test'
    config._metadata['Tester'] = 'Dharmendra Yadav'

#It is Hook to Delete/Modify Environment info to HTML Report#

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("CATNAV HOME ", None)
    metadata.pop("plugins ", None)