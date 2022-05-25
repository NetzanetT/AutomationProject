from Web.Locators.LocatorsWomen import WomenLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class WomenDepPage(WomenLocators):

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://atid.store/product-category/women/")
        self.addToCart = WomenLocators.addToCart
        self.cart = WomenLocators.cart
        self.itemsIncart= WomenLocators.itemsIncart
        self.openSorting =WomenLocators.openSorting
        self.clickOnsort = WomenLocators.clickOnsort
        self.elements = WomenLocators.elements

    def click_on_sorting_field(self):
        self.driver.find_element(By.XPATH,self.clickOnsort).click()

    def open_sorting_box_and_select_sortingType(self,num):
        select = Select(self.driver.find_element(By.XPATH, self.openSorting))
        select.select_by_index(num)

    def select_elemnt_from_list(self):
        self.driver.find_element(By.XPATH, self.elements)

    def select_specific_item(self, y):
       x=  self.select_elemnt_from_list()

    def select_specific_items(self, y):
       x=  self.select_elemnt_from_list()






