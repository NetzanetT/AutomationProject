import allure

from Web.Locators.ContactLocators import ContactUsLocators
from selenium.webdriver.common.by import By


class ContactUsForm:

    def __init__(self, driver):
        self.driver = driver
        self.Name_field = ContactUsLocators.Name_field
        self.Subject_field = ContactUsLocators.Subject_field
        self.Email_field = ContactUsLocators.Email_field
        self.Message_field = ContactUsLocators.Message_field
        self.Send_button = ContactUsLocators.Send_button

    @allure.step
    def enter_name(self,name):
        # self.driver.find_element(By.XPATH,self.Name_field).clear()
        self.driver.find_element(By.XPATH,self.Name_field).send_keys(name)

    @allure.step
    def enter_subject(self,subject):
        self.driver.find_element(By.XPATH, self.Subject_field).send_keys(subject)

    @allure.step
    def enter_email(self,mail):
        # self.driver.find_element(By.XPATH,self.Email_field).clear()
        self.driver.find_element(By.XPATH,self.Email_field).send_keys(mail)

    @allure.step
    def enter_message(self,message):
        self.driver.find_element(By.XPATH,self.Message_field).send_keys(message)

    @allure.step
    def click_send(self):
        self.driver.find_element(By.XPATH,self.Send_button).click()
