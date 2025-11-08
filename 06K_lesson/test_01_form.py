import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestForm(unittest.TestCase):

def setUp(self):

service = Service('/path/to/msedgedriver')
self.driver = webdriver.Edge(service=service)
self.driver.maximize_window()

def tearDown(self):
self.driver.quit()

def test_fill_and_submit_form(self):
driver = self.driver
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Заполнение формы
first_name = driver.find_element(By.NAME,"first-name")
last_name = driver.find_element(By.NAME,"last-name")
address = driver.find_element(By.NAME,"address")
email = driver.find_element(By.NAME,"email")
phone_number = driver.find_element(By.NAME,"phone-number")
zip_code = driver.find_element(By.NAME,"zip-code")
city = driver.find_element(By.NAME,"city")
country = driver.find_element(By.NAME,"country")
job_position = driver.find_element(By.NAME,"job-position")
company = driver.find_element(By.NAME,"company")

first_name.send_keys("Иван")
last_name.send_keys("Петров")
address.send_keys("Ленина, 55-3")
email.send_keys("test@skypro.com")
phone_number.send_keys("+7985899998787")

city.send_keys("Москва")
country.send_keys("Россия")
job_position.send_keys("QA")
company.send_keys("SkyPro")


submit_button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
submit_button.click()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "form-control.is-invalid")))

zip_code_invalid = driver.find_element(By.CSS_SELECTOR,"#zip-code.form-control.is-invalid")
assert zip_code_invalid is not None, "Поле Zip code не подсвечено красным!"

fields_to_check = [
(first_name, '#first-name'),
(last_name, '#last-name'),
(address, '#address'),
(email, '#email'),
(phone_number, '#phone-number'),
(city, '#city'),
(country, '#country'),
(job_position, '#job-position'),
(company, '#company')
        ]

for field, selector in fields_to_check:
valid_field = driver.find_element(By.CSS_SELECTOR,f"{selector}.form-control.is-valid")
assert valid_field is not None, f"Поле {field.get_attribute('name')} не подсвечено зеленым!"

if __name__ == '__main__':
     unittest.main()