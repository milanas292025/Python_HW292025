from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


def test_dynamic_id():
    try:

        driver.get('http://uitestingplayground.com/dynamicid')

        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
        button.click()

        time.sleep(2)

        print("Тест успешно пройден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        pass


if __name__ == "__main__":

    for i in range(3):
        print(f"Тест №{i + 1}:")
        test_dynamic_id()
        time.sleep(1)

    driver.quit()