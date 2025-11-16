from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_field = (By.ID, "delay")
        self.result_field = (By.ID, "result")
        self.buttons = {
            "7": (By.XPATH, "//button[.='7']"),
            "+": (By.XPATH, "//button[.='+']"),
            "8": (By.XPATH, "//button[.='8']"),
            "=": (By.XPATH, "//button[.='=']"),
        }

    def open_page(self):
        #Метод для открытия страницы калькулятора."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        #Устанавливает значение задержки в поле 'Delay'. """
        delay_input = self.driver.find_element(*self.delay_field)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def press_buttons(self, *buttons):
        #Нажимает на кнопки в порядке передачи аргументов."""
        for btn in buttons:
            element = self.driver.find_element(*self.buttons[btn])
            element.click()

    def read_result(self):
        #Возвращает текст из поля результата."""
        return self.driver.find_element(*self.result_field).text

    def wait_until_result_appears(self, expected_result):
        #Ожидает, пока результат не появится на экране."""
        wait = WebDriverWait(self.driver, 50)  # Увеличенное время ожидания, так как задержка 45 секунд
        wait.until(EC.text_to_be_present_in_element(self.result_field, expected_result))
