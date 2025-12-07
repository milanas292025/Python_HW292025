from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CheckoutStepOnePage:
    """
    Представляет первую страницу оформления заказа Sauce Demo.
    """

    def __init__(self, driver):
        """
        Инициализирует объект первой страницы оформления заказа.

        :param driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")  # Поле ввода имени
        self.last_name_field = (By.ID, "last-name")  # Поле ввода фамилии
        self.postal_code_field = (By.ID, "postal-code")  # Поле ввода почтового индекса
        self.continue_button = (By.ID, "continue")  # Кнопка продолжения

    def fill_first_name(self, first_name: str) -> None:
        """
        Вводит имя пользователя.

        :param first_name: Имя пользователя (string).
        """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    def fill_last_name(self, last_name: str) -> None:
        """
        Вводит фамилию пользователя.

        :param last_name: Фамилия пользователя (string).
        """
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    def fill_postal_code(self, postal_code: str) -> None:
        """
        Вводит почтовый индекс пользователя.

        :param postal_code: Почтовый индекс (string).
        """
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)

    def click_continue(self) -> None:
        """
        Нажимает кнопку продолжения.
        """
        self.driver.find_element(*self.continue_button).click()