import pytest
from selenium import webdriver
from .pages.calculator_page import CalculatorPage
import allure

@pytest.fixture(scope="session")
def browser():
    """
    Фикстура для инициализации браузера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Функционал калькулятора")
@allure.story("Проверка арифметического расчёта с задержкой")
@allure.title("Корректность расчётов с учётом временной задержки")
@allure.description("""
Тест проверяет корректность арифметических расчетов на странице калькулятора
с учетом временной задержки в 45 секунд.
""")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator_functionality(browser):
    calculator_page = CalculatorPage(browser)
    calculator_page.open_page()

    @allure.step("Устанавливаем задержку в 45 секунд")
    def step_set_delay():
        calculator_page.set_delay(45)

    @allure.step("Нажимаем на кнопки 7, +, 8, =")
    def step_press_buttons():
        calculator_page.press_buttons("7", "+", "8", "=")

    @allure.step("Ожидаем результат 15")
    def step_wait_result():
        calculator_page.wait_until_result_appears("15")

    @allure.step("Проверяем, что результат действительно 15")
    def check_result():
        result = calculator_page.read_result()
        assert result == "15", f"Expected result was 15 but got {result}"

    # Выполняем шаги
    step_set_delay()
    step_press_buttons()
    step_wait_result()
    check_result()