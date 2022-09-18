from selenium.webdriver.common.by import By


class SauceLabsLogin:
    test_Username_xpath = "//input[@placeholder='Username']"
    test_Password_xpath = "//input[@placeholder='Password']"
    button_Login_xpath = "//input[@id='login-button']"
    button_pane_xpath="//button[@id='react-burger-menu-btn']"
    button_logout_xpath="//a[@id='logout_sidebar_link']"

    def __init__(self, driver):
        self.driver = driver


    def setUserName(self,username):
        self.driver.find_element(By.XPATH, self.test_Username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.test_Password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def clickPage(self):
        self.driver.find_element(By.XPATH, self.button_pane_xpath).click()
    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    def clickLogoutElement(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath)