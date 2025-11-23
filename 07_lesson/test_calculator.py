import pytest
from selenium import webdriver
from.pages.calculator_page import CalculatorPage

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator_functionality(browser):
    calculator_page = CalculatorPage(browser)
    calculator_page.open_page()

    # Устанавливаем задержку 45 секунд
    calculator_page.set_delay(45)

    # Нажимаем кнопки 7, +, 8, =
    calculator_page.press_buttons("7", "+", "8", "=")

    # Ожидаем результат 15
    calculator_page.wait_until_result_appears("15")

    # Проверяем, что результат действительно 15
    result = calculator_page.read_result()
    assert result == "15", f"Expected result was 15 but got {result}"