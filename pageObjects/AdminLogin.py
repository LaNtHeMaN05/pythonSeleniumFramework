from selenium.webdriver.common.by import By


class AdminLogin:
    textbox_user_name_xpath = "//input[@type='email']"
    textbox_user_password_css = ".password"
    button_login_xpath = "//button[@type='submit']"
    button_logout_xpath = "//a[contains(text(),'Logout')]"
    button_CustomersDrop_xpath="//i[@class='nav-icon far fa-user']"
    button_CustomerList_xpath="//li/a[@href='/Admin/Customer/List']"

    def __init__(self, driver):
        self.driver = driver

    def set_Username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_user_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_user_name_xpath).send_keys(username)

    def set_Password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_user_password_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_user_password_css).send_keys(password)

    def click_Login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_CustomerDrop(self):
        self.driver.find_element(By.XPATH,self.button_CustomersDrop_xpath).click()

    def click_CustomerList(self):
        self.driver.find_element(By.XPATH,self.button_CustomerList_xpath).click()

