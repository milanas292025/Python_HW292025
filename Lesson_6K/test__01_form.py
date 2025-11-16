import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_fill_and_submit_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Отправка формы
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Ждём, пока форма обработается и появятся классы ошибок/успеха
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )

    # Проверяем, что zip-code подсвечен КРАСНЫМ
    zip_code_color = driver.find_element(By.ID, "zip-code").value_of_css_property("background-color")
    assert zip_code_color == "rgba(248, 215, 218, 1)", f"Zip-code НЕ подсвечен красным: {zip_code_color}"

    # Проверяем, что все остальные поля - зелёные
    green = "rgba(209, 231, 221, 1)"
    ok_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]
    for field in ok_fields:
        color = driver.find_element(By.ID, field).value_of_css_property("background-color")
        assert color == green, f"Поле {field} не подсвечено зелёным: {color}"
