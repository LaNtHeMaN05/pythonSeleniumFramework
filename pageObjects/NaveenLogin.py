from selenium.webdriver.common.by import By


class NaveenLogin:
    button_MyAccount_xpath = "//span[contains(text(),'My Account')]"
    button_Login_xpath = "//a[contains(text(),'Login')]"
    text_username_xpath = "//input[@placeholder='E-Mail Address']"
    text_password_xpath = "//input[@placeholder='Password']"
    button_signin_xpath = "//input[@value='Login']"

    def __init__(self, driver):
        self.driver = driver

    def set_Username(self, username):
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def clickMyAccout(self):
        self.driver.find_element(By.XPATH, self.button_MyAccount_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def clickSignin(self):
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()
