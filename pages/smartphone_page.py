from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Smartphone_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    filter_price = "//input[@class='f__range-input js-f-range-to js-f-range-input']"
    filter_samsung = "//label[@for='137-210']"
    filter_button = "//div[@class='f__show-btn js-show-btn']"
    filter_samsung_a73 = "//input[@class='catalog2__search-input']"
    filter_samsung_a73_button = "//button[@class='catalog2__search-btn']"

    # Getters
    def get_filter_price(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_price)))

    def get_filter_samsung(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_samsung)))

    def get_filter_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_button)))

    def get_filter_samsung_a73(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_samsung_a73)))

    def get_filter_samsung_a73_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_samsung_a73_button)))

    # Actions
    def input_filter_price(self, filter_price):
        self.get_filter_price().send_keys(filter_price)
        print("Input filter price")

    def click_filter_samsung(self):
        self.get_filter_samsung().click()
        print("Click filter brand 'Samsung'")

    def click_filter_button(self):
        self.get_filter_button().click()
        print("Click filter button")

    def input_filter_samsung_a73(self, filter_samsung_a73):
        self.get_filter_samsung_a73().send_keys(filter_samsung_a73)
        print("Input filter 'Samsung A73'")

    def click_filter_samsung_a73_button(self):
        self.get_filter_samsung_a73_button().click()
        print("Click filter 'Samsung A73' button")

    # Methods
    def select_smartphone(self):
        self.input_filter_price("50000")
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.click_filter_samsung()
        self.click_filter_button()
        self.input_filter_samsung_a73("A73")
        self.click_filter_samsung_a73_button()
