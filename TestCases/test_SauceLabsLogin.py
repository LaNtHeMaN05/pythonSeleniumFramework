import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.customLogger import LogGen
from Utilities.readProperties import readConfig
from pageObjects.SauceLabsLogin import SauceLabsLogin
from Utilities import XLUtilitiesSauceLabs


class Test_SauceLabsLogin:
    url = readConfig.sauceLabsUrl()
    testDataPath = ".//TestData/saucelabs.xlsx"
    sheet = "login"
    log = LogGen.logsGenerator()

    @pytest.mark.nf
    def test_saucelabsLogin(self, driverInit):
        self.log.info("*******************Sauce Labs Multi Login Test - STARTED****************")
        self.driver = driverInit
        self.log.info("Driver Initialized Successfully")
        self.driver.maximize_window()
        self.log.info("Window Maximized")
        self.sl = SauceLabsLogin(self.driver)

        self.rowCount = XLUtilitiesSauceLabs.getRowCount(self.testDataPath, self.sheet)
        self.log.info("Max Row count from DDT Excel fetched")

        for r in range(2, self.rowCount + 1):
            self.log.info("FOR loop to fetch the login details and perform Login")
            self.username = XLUtilitiesSauceLabs.readData(self.testDataPath, self.sheet, r, 1)
            self.password = XLUtilitiesSauceLabs.readData(self.testDataPath, self.sheet, r, 2)
            self.driver.get(self.url)
            self.sl.setUserName(self.username)
            self.sl.setPassword(self.password)
            self.sl.clickLogin()
            self.driver.get_screenshot_as_file(".\\Screenshots\\Passed_SauceLabs_" + self.username + ".png")
            self.log.info("Screenshot captured for current Login Details")
            self.sl.clickPage()
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, self.sl.button_logout_xpath)))
            self.sl.clickLogout()
        self.driver.close()
        self.log.info("******************Sauce Labs Login test - PASSED*****************")
