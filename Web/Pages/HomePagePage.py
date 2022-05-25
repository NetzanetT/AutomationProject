import allure
from Web.Locators.LocatorsHomePage import HomePageLocators
import pytest
from selenium.webdriver.common.by import By

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://atid.store/")
        self.shopNowWomen = HomePageLocators.shopNowWomen
        self.shopNowMen = HomePageLocators.shopNowMen
        self.checkOut = HomePageLocators.checkOut
        self.search= HomePageLocators.search
        self.insertKeys = HomePageLocators.insertKeys
        self.clickSearch = HomePageLocators.clickSearch
        self.prudactName= HomePageLocators.prudactName
        self.prudactDescr = HomePageLocators.prudactDescr
        self.prudact_error= HomePageLocators.prudact_error

    def click_on_searchField(self):
        self.driver.find_element(By.XPATH, self.search).click()

    def insert_prudact_name(self,prudact):
        self.driver.find_element(By.XPATH, self.insertKeys).send_keys(prudact)

    def click_search(self):
        self.driver.find_element(By.XPATH, self.clickSearch).click()







