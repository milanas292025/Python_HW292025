from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    """
    Класс представляет страницу калькулятора с методами для взаимодействия с элементами.
    """

    def __init__(self, driver):
        """
        Инициализирует объект страницы калькулятора.

        :param driver: Веб-драйвер Selenium.
        """
        self.driver = driver
        self.delay_field = (By.ID, "delay")  # Поле задержки
        self.result_field = (By.ID, "result")  # Поле результата
        self.buttons = {
            "7": (By.XPATH, "//button[.='7']"),  # Кнопка "7"
            "+": (By.XPATH, "//button[.='+']"),  # Кнопка "+"
            "8": (By.XPATH, "//button[.='8']"),  # Кнопка "8"
            "=": (By.XPATH, "//button[.='=']"),  # Кнопка "="
        }

    def open_page(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает значение задержки в поле 'Delay'.

        :param seconds: Количество секунд задержки.
        """
        delay_input = self.driver.find_element(*self.delay_field)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def press_buttons(self, *buttons: str) -> None:
        """
        Нажимает на кнопки в порядке передачи аргументов.

        :param buttons: Названия кнопок, которые нужно нажать.
        """
        for btn in buttons:
            element = self.driver.find_element(*self.buttons[btn])
            element.click()

    def read_result(self) -> str:
        """
        Возвращает текст из поля результата.

        :return: Текущее значение результата в виде строки.
        """
        return self.driver.find_element(*self.result_field).text

    def wait_until_result_appears(self, expected_result: str) -> None:
        """
        Ожидает, пока результат не появится на экране.

        :param expected_result: Ожидаемая строка результата.
        """
        wait = WebDriverWait(self.driver, 50)  # Увеличенное время ожидания, так как задержка 45 секунд
        wait.until(EC.text_to_be_present_in_element(self.result_field, expected_result))