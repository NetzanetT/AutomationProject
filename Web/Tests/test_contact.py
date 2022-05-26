import pytest
from Web.Pages.ContactPage import ContactUsForm
from Web.Locators.ContactLocators import ContactUsLocators
from selenium.webdriver.common.by import By
from Web.Base.BasePage import Base
from selenium.common.exceptions import *
import allure
from allure_commons.types import AttachmentType

@pytest.mark.usefixtures('set_up')
class Test_ContactUs(Base):

    # __user_data_file = r"\login_details.xlsx"
    # df = pd.read_excel(os.getcwd() + __user_data_file)

    @pytest.mark.regression
    def test_contact_correctly(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('Netzanet')
        contact.enter_subject("shalom")
        contact.enter_email("netzanet123@gmail.com")
        contact.enter_message("hey i love your website")
        contact.click_send()
        # result = driver.find_element(By.ID,"wpforms-confirmation-15").get_attribute("innerText")
        # assert result == "Thanks for contacting us! We will be in touch with you shortly."

        try:
            assert "Contact Us – ATID Demo Store" == driver.title
        except Exception as e:
            raise
            print("Title is wrong", format(e))

    @pytest.mark.regression
    def test_ContactCorrectly_without_OptionalField(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('Netzanet')
        contact.enter_email("netzanet123@gmail.com")
        contact.enter_message("hey i love your website")
        contact.click_send()

        try:
            assert "Contact Us – ATID Demo Store" == driver.title
        except Exception as e:
            raise
            print("Title is wrong", format(e))

    @pytest.mark.regression
    def test_ContactIncorrectly_When_FieldsIsNull(self):
        driver= self.driver
        contact = ContactUsForm(driver)
        contact.click_send()

        name = driver.find_element(By.ID, "wpforms-15-field_0-error").get_attribute("innerText")
        email = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")
        message = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")

        try:
            assert name and email and message == "This field is required."
        except Exception as e:
            raise
            print("Note is wrong", format(e))



    def test_ContactuIncorrectly_when_NameIsNull(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_subject("shalom")
        contact.enter_email("netzanet123@gmail.com")
        contact.enter_message("hey i love your website")
        contact.click_send()

        name= driver.find_element(By.ID,"wpforms-15-field_0-error").get_attribute("innerText")

        try:
            assert name == "This field is required."
        except Exception as e:
            raise
            print("Note is wrong", format(e))

    @pytest.mark.nightly
    def test_ContactIncorrectly_when_EmailIsNull(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('Netzanet')
        contact.enter_subject("shalom")
        contact.enter_message("hey i love your website")
        contact.click_send()

        email = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")

        try:
            assert email == "This field is required."
        except Exception as e:
            raise
            print("Note is wrong", format(e))

    # @pytest.mark.skip
    def test_ContactIncorrectly_when_MessageIsNull(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('Netzanet')
        contact.enter_subject("shalom")
        contact.enter_email("netzanet123@gmail.com")
        contact.enter_message("")
        contact.click_send()

        message = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")

        try:
            assert message == "This field is required."
        except Exception as e:
            raise
            print("Note is wrong", format(e))

    # @pytest.mark.skip
    def test_ConactIncorrectly_when_InsertOnly_name(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('Netzanet')
        contact.click_send()

        email = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")
        message = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")

        try:
            assert email and message == "This field is required."
        except Exception as e:
            raise
            print("Note is wrong", format(e))



    @pytest.mark.skip
    def test_ConactIncorrectly_when_InsertOnly_email(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_email("netzanet123@gmail.com")
        contact.click_send()

        name = driver.find_element(By.ID, "wpforms-15-field_0-error").get_attribute("innerText")
        message = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")

        try:
            assert name and message == "This field is required."
        except Exception as e:
            raise
            print("Note is wrong", format(e))

    @pytest.mark.nightly
    def test_ConactIncorrectly_when_InsertOnly_message(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_message("hey how are you")
        contact.click_send()

        name = driver.find_element(By.ID, "wpforms-15-field_0-error").get_attribute("innerText")
        email = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")

        try:
            assert name and email == "This field is required."
        except Exception as e:
            raise
            print("Note is wrong", format(e))

    def test_ContactIncorrectly_when_EmailIsNumbers(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('Netzanet')
        contact.enter_subject("shalom")
        contact.enter_email("12345")
        contact.enter_message("hey i love your website")
        contact.click_send()

        email = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")

        try:
            assert email == "Please enter a valid email address."
        except Exception as e:
            raise
            print("Note is wrong", format(e))


    def test_ContactIncorrectly_when_NameIsNumbers(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('1234')
        contact.enter_subject("shalom")
        contact.enter_email("nwt@gmail.com")
        contact.enter_message("hey i love your website")
        contact.click_send()

        name = driver.find_element(By.ID,"wpforms-15-field_0-error").get_attribute("innerText")

        try:
            assert name == "Please enter a valid name."
        except Exception:
            driver.get_screenshot_as_png()
            driver.save_screenshot("ContactIncorrectly when nameIsNumbers.png")
        driver.quit()
        driver.close()



    def test_ContactIncorrectly_when_MeassageIsNumbers(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('nwtzanet')
        contact.enter_subject("shalom")
        contact.enter_email("nwt@gmail.com")
        contact.enter_message("128904")
        contact.click_send()

        message = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")

        try:
            assert message == "Please enter a valid message."
        except Exception as e:
            raise
            print("Note is wrong", format(e))

    def test_ContactIncorrectly_when_EmailIsSigns(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('nwtzanet')
        contact.enter_subject("shalom")
        contact.enter_email("#$%^")
        contact.enter_message("hey")
        contact.click_send()

        email = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")

        try:
            assert email == "Please enter a valid email address."
        except Exception as e:
            raise
            print("Note is wrong", format(e))



    def test_ContactIncorrectly_when_NameIsSigns(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('#$%^')
        contact.enter_subject("shalom")
        contact.enter_email("nwt@gmail.com")
        contact.enter_message("HEYEYE")
        contact.click_send()

        name = driver.find_element(By.ID, "wpforms-15-field_0-error").get_attribute("innerText")

        try:
            assert name == "Please enter a valid name."
        except Exception as e:
            raise
            print("Note is wrong", format(e))

    def test_ContactIncorrectly_when_MeassageIsSigns(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('netz')
        contact.enter_subject("shalom")
        contact.enter_email("nwt@gmail.com")
        contact.enter_message("#$%^&*")
        contact.click_send()

        message = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")

        try:
            assert message == "Please enter a valid message."
        except Exception as e:

            raise
            print("Note is wrong", format(e))


    def test_ContactIncorrectly_when_MeassageIsSi(self):
        driver = self.driver
        contact = ContactUsForm(driver)
        contact.enter_name('netz')
        contact.enter_subject("shalom")
        contact.enter_email("nwt@gmail.com")
        contact.enter_message("#$%^&*")
        contact.click_send()

        message = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")

        try:
            assert message == "Please enter a valid message."
        except Exception as e:

            raise
            print("Note is wrong", format(e))



























