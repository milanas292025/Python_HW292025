from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class LoginPage:
    """
    Представляет страницу авторизации Sauce Demo.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы авторизации.

        :param driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.username_field = (By.ID, "user-name")  # Поле ввода имени пользователя
        self.password_field = (By.ID, "password")  # Поле ввода пароля
        self.login_button = (By.ID, "login-button")  # Кнопка входа

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле.

        :param username: Имя пользователя (string).
        """
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле.

        :param password: Пароль (string).
        """
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self) -> None:
        """
        Нажимает кнопку входа.
        """
        self.driver.find_element(*self.login_button).click()
