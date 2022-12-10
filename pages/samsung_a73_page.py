import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Samsung_a73_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    samsung_a73_256_mint = "//a[@href='/cart/add/113207']"
    continue_buy = "//a[@class='main__continue']"
    cart = "//a[@class='h-basket ']"

    # Getters
    def get_samsung_a73_256_mint(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.samsung_a73_256_mint)))

    def get_continue_buy(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.continue_buy)))

    def get_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions
    def click_samsung_a73_256_mint(self):
        self.get_samsung_a73_256_mint().click()
        print("Click 'Samsung A73 Mint 256'")

    def click_continue_buy(self):
        self.get_continue_buy().click()
        print("Click continue buy")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    # Methods
    def select_samsung_a73(self):
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(3)
        self.click_samsung_a73_256_mint()
        self.click_continue_buy()
        self.click_cart()
