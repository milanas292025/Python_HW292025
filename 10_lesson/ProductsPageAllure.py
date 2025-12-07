from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ProductsPage:
    """
    Представляет страницу товаров Sauce Demo.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы товаров.

        :param driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")  # Кнопка добавления рюкзака
        self.tshirt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")  # Кнопка добавления футболки
        self.onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")  # Кнопка добавления костюма
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")  # Картинка корзины

    def add_backpack_to_cart(self) -> None:
        """
        Добавляет рюкзак в корзину.
        """
        self.driver.find_element(*self.backpack_add_button).click()

    def add_tshirt_to_cart(self) -> None:
        """
        Добавляет футболку в корзину.
        """
        self.driver.find_element(*self.tshirt_add_button).click()

    def add_onesie_to_cart(self) -> None:
        """
        Добавляет костюм в корзину.
        """
        self.driver.find_element(*self.onesie_add_button).click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.
        """
        self.driver.find_element(*self.cart_icon).click()