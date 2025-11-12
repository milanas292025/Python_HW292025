import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_field = driver.find_element(By.ID,"delay")
    delay_field.clear()
    delay_field.send_keys("45")

    for val in ["7", "+", "8", "="]:
        driver.find_element(By.XPATH, f"//span[text()='{val}']").click()

    # Ждём результат "15" на экране
    WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    display_value = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert display_value == "15", f"Результат неверный: {display_value}"

    print("Автотест успешно прошел!")