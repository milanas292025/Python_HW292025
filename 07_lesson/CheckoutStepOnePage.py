from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CheckoutStepOnePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    def fill_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()