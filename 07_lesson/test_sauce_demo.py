import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_complete_page import CheckoutCompletePage
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_sauce_demo_order(browser):
    # Инициализация объектов страниц
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    cart_page = CartPage(browser)
    checkout_step_one_page = CheckoutStepOnePage(browser)
    checkout_complete_page = CheckoutCompletePage(browser)

    # Авторизация
    browser.get("https://www.saucedemo.com/")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Добавляем товары в корзину
    products_page.add_backpack_to_cart()
    products_page.add_tshirt_to_cart()
    products_page.add_onesie_to_cart()

    # Переход в корзину
    products_page.go_to_cart()

    # Оформление заказа
    cart_page.proceed_to_checkout()

    # Вводим личные данные
    checkout_step_one_page.fill_first_name("John")
    checkout_step_one_page.fill_last_name("Doe")
    checkout_step_one_page.fill_postal_code("12345")
    checkout_step_one_page.click_continue()

    # Проверка итоговой цены
    final_price = checkout_complete_page.get_total_cost()
    assert final_price == 58.29, f"Final price should be $58.29, but it is ${final_price:.2f}"

    print("Автотест успешно завершился!")