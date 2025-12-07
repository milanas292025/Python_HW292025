from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CheckoutCompletePage:
    """
    Представляет финальную страницу оформления заказа Sauce Demo.
    """

    def __init__(self, driver):
        """
        Инициализирует объект финальной страницы оформления заказа.

        :param driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.total_price = (By.CLASS_NAME, "summary_total_label")  # Поле итоговой стоимости

    def get_total_cost(self) -> float:
        """
        Возвращает итоговую стоимость заказа.

        :return: Стоимость заказа (float).
        """
        raw_price = self.driver.find_element(*self.total_price).text
        clean_price = raw_price.replace("Total: $", "")
        return float(clean_price)