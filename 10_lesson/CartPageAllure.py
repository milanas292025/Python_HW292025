from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CartPage:
    """
    Представляет страницу корзины Sauce Demo.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы корзины.

        :param driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")  # Кнопка "Оформить заказ"

    def proceed_to_checkout(self) -> None:
        """
        Начинает оформление заказа.
        """
        self.driver.find_element(*self.checkout_button).click()