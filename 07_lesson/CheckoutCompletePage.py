from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.total_price = (By.CLASS_NAME, "summary_total_label")

    def get_total_cost(self):
        return float(self.driver.find_element(*self.total_price).text.replace("Total: $", ""))