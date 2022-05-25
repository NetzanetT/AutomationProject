import pytest
import allure
from selenium.webdriver.common.by import By
from Base.BasePage import Base
from Pages.WomenPage import WomenDepPage

@pytest.mark.usefixtures('set_up')
class Test_WomenDep(Base):

    def test_Women_Select_Bright_Red_Bag(self):
        driver= self.driver
        women = WomenDepPage(driver)
        women.click_on_sorting_field()
        women.open_sorting_box_and_select_sortingType(2)
        # women.select_sorting_type(2)
        women.select_elemnt_from_list()
        women.select_specific_item(3)

