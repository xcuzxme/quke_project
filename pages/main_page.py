from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog_main = "//div[@class='main-nav__catalog']"
    catalog_smart = "//a[@class='cat-nav__block-title']"

    # Getters
    def get_catalog_main(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.catalog_main)))

    def get_catalog_smart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.catalog_smart)))

    # Actions
    def click_catalog_main(self):
        self.get_catalog_main().click()
        print("Click catalog main")

    def click_catalog_smart(self):
        self.get_catalog_smart().click()
        print("Click catalog smart")

    # Methods
    def select_catalog(self):
        self.click_catalog_main()
        self.click_catalog_smart()
        self.get_current_url()
        self.assert_url("https://quke.ru/shop/smartfony")
