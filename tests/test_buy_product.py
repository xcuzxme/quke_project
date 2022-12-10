import time

from selenium import webdriver

from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.samsung_a73_page import Samsung_a73_page
from pages.smartphone_page import Smartphone_page


def test_buy_product():
    driver = webdriver.Firefox(executable_path='C:\\Users\\user\\PycharmProjects\\driver\\geckodriver.exe\\')
    print("Start Test")

    login = Login_page(driver)
    login.autorization()

    main = Main_page(driver)
    main.select_catalog()

    smartphone = Smartphone_page(driver)
    smartphone.select_smartphone()

    samsung_a73 = Samsung_a73_page(driver)
    samsung_a73.select_samsung_a73()

    f = Finish_page(driver)
    f.finish()

    time.sleep(5)
    driver.close()
