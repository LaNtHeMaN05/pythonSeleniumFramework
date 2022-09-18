import pytest

from Utilities.customLogger import LogGen
from Utilities.readProperties import readConfig
from pageObjects.NaveenLogin import NaveenLogin


class Test_NaveenLoginTest:
    user = readConfig.naveenUser()
    url = readConfig.naveenUrl()
    pswd = readConfig.naveenPswd()
    log = LogGen.logsGenerator()

    @pytest.mark.sanity
    def test_login(self, driverInit):

        self.log.info("******************Naveen Automation Labs Login Test************************")

        self.driver = driverInit
        self.log.info("Driver initialized Successfully")

        self.driver.maximize_window()
        self.log.info("Window maximized Successfully")
        self.driver.get(self.url)
        self.log.info("Navigated to the URL")
        self.nl=NaveenLogin(self.driver)
        self.nl.clickMyAccout()
        self.nl.clickLogin()
        self.log.info("Navigated to the LOGIN PAGE")
        self.nl.set_Username(self.user)
        self.nl.set_password(self.pswd)
        self.nl.clickSignin()
        self.log.info("Login Successful")

        if self.driver.title=="My Account":
            self.driver.get_screenshot_as_file(".\\Screenshots\\Passed_NaveenLoginTest.png")
            self.log.info("Passed Screenshot captured successfully")
            assert True
            self.driver.close()
            self.log.info("******************Naveen Automation Labs Login Rest - PASSED************")

        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\Failed_NaveenLoginTest.png")
            self.log.info("Failed Screenshot captured successfully")
            self.driver.close()
            assert False
            self.log.info("******************Naveen Automation Labs Login Rest - FAILED************")

