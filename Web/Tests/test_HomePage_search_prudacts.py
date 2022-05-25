import pytest
from Web.Base.BasePage import Base
from Web.Pages.HomePagePage import HomePage
from selenium.webdriver.common.by import By
import allure

@pytest.mark.usefixtures('set_up')
class Test_searchPrudacts(Base):


    def test_DisplayPrudact_AnchlorBracelte(self):
        driver = self.driver
        homepage= HomePage(driver)
        homepage.click_on_searchField()
        homepage.insert_prudact_name("Anchor Bracelet")
        homepage.click_search()

        name= driver.find_element(By.XPATH,HomePage.prudactName).get_attribute("innerText")

        try:
            assert "Anchor Bracelet" == name
        except Exception as e:
            print("Error")
            allure.attach(driver.get_screenshot_as_png(), name = "fail" , attachment_type=allure.attachment_type.PNG)

    def test_DisplayPrudact_FlamingoTshirt(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_on_searchField()
        homepage.insert_prudact_name("Flamingo Tshirt")
        homepage.click_search()

        name = driver.find_element(By.XPATH, HomePage.prudactName).get_attribute("innerText")
        try:
            assert "Flamingo Tshirt" == name
        except Exception as e:
            print(e)
            allure.attach(driver.get_screenshot_as_png(),name="screenshot",attachment_type=allure.attachment_type.PNG)

    @pytest.mark.sanity
    def test_DisplayError_When_searchField_isNull(self):
        driver= self.driver
        homepage= HomePage(driver)
        homepage.click_on_searchField()
        homepage.insert_prudact_name(" ")
        homepage.click_search()

        title= driver.find_element(By.XPATH,homepage.prudactName).get_attribute("innerText")

        try:
            assert "Hello world!" == title
        except Exception as e:
            print(e)
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

    @pytest.mark.sanity
    def test_DisplayError_When_Search_UnexistItem_Watch(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_on_searchField()
        homepage.insert_prudact_name("Watch")
        homepage.click_search()

        message = driver.find_element(By.XPATH,homepage.prudact_error).get_attribute("innerText")
        try:
            assert "Sorry, but nothing matched your search terms. Please try again with some different keywords." == message
        except Exception as e:
            print(e)
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

    @pytest.mark.sanity
    def test_DisplayError_When_Search_numbers(self):
        driver = self.driver
        homepage= HomePage(driver)
        homepage.click_on_searchField()
        homepage.insert_prudact_name("123455")
        homepage.click_search()

        message= driver.find_element(By.XPATH, homepage.prudact_error).get_attribute("innerText")
        try:
            assert "Sorry, but nothing matched your search terms. Please try again with some different keywords." == message
        except Exception as e:
            print(e)
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

    @pytest.mark.sanity
    def test_DisplayError_When_Search_signs(self):
        driver = self.driver
        homepage= HomePage(driver)
        homepage.click_on_searchField()
        homepage.insert_prudact_name("#$%^&")
        homepage.click_search()

        message = driver.find_element(By.XPATH, homepage.prudact_error).get_attribute("innerText")
        try:
            assert "Sorry, but nothing matched your search terms. Please try again with some different keywords." == message
        except Exception as e:
            print(e)
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

















