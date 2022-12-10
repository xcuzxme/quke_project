from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    url = 'https://quke.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    enter_button = "//a[@class='h-user__link js-auth']"
    auth_email = "//input[@id='auth-email']"
    auth_pass = "//input[@id='auth-pass']"
    login_button = "//button[@class='btn btn--white auth-form__btn-enter']"
    main_word = "//span[@class='h-phone__text']"

    # Getters
    def get_enter_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_auth_email(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.auth_email)))

    def get_auth_pass(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.auth_pass)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # Actions
    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click enter button")

    def input_auth_email(self, auth_email):
        self.get_auth_email().send_keys(auth_email)
        print("Input email")

    def input_auth_pass(self, auth_pass):
        self.get_auth_pass().send_keys(auth_pass)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods
    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_enter_button()
        self.input_auth_email("xcuzx@ya.ru")
        self.input_auth_pass("UgQ4JDwpqNX4WsM")
        self.click_login_button()
