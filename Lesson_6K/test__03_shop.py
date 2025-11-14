import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

wait = WebDriverWait(driver, 10)

def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

element = wait.until(EC.presence_of_element_located((By.ID, "some-element")))

USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

FIRST_NAME = 'Lana'
LAST_NAME = 'Serebro'
POSTAL_CODE = '624074'

username_field = driver.find_element(By.ID, 'user-name')
password_field = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'login-button')

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
login_button.click()

items = ['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie']
for item in items:
    add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), "f"'{item}')]/ancestor::div/div/button"))).click()
    cart_link = driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    checkout_button = wait.until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()

    first_name_field = driver.find_element(By.ID, 'first-name')
    last_name_field = driver.find_element(By.ID, 'last-name')
    postal_code_field = driver.find_element(By.ID, 'postal-code')
    continue_button = driver.find_element(By.ID, 'continue')

    first_name_field.send_keys(FIRST_NAME)
    last_name_field.send_keys(LAST_NAME)
    postal_code_field.send_keys(POSTAL_CODE)
    continue_button.click()

    total_amount = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label'))).text.split(':')[1].strip()

    assert total_amount == '$58.29', f"Итоговая сумма не совпадает, получено: {total_amount}, ожидается: $58.29"

    print("Автотест успешно завершён!")

    driver.quit()