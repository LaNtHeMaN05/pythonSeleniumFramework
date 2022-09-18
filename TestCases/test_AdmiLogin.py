import pytest

from Utilities.customLogger import LogGen
from pageObjects.AdminLogin import AdminLogin


class Test_AdminLoginTest:
    log = LogGen.logsGenerator()

    @pytest.mark.sanity
    def test_Title(self, driverInit, excelData):
        self.log.info("******************* Admin Login Test - Started *******************")
        self.driver = driverInit
        self.log.info("Driver Initiated Successfully")
        self.driver.maximize_window()
        self.log.info("Browser Window Maximized")
        self.url, self.username, self.password = excelData
        self.log.info("URL,Username and Password fetched from excel")
        self.driver.get(self.url)
        self.al = AdminLogin(self.driver)
        self.al.set_Username(self.username)
        self.al.set_Password(self.password)
        self.al.click_Login()
        self.log.info("Clicking the Login Button")
        logged_title = self.driver.title
        if logged_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "Passed_Test_AdminLoginTest.png")
            self.log.info("Login Successful, Saving Screenshot")
            self.log.info("******************* Admin Login Test - Passed *******************")
            self.driver.close()
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "Failed_Test_AdminLoginTest.png")
            self.log.info("Login failed, Saving Screenshot")
            self.log.info("******************* Admin Login Test - Failed *******************")
            self.driver.close()
            assert False
