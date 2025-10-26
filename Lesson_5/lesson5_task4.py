from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GECKO_DRIVER_PATH = '/your/path/to/geckodriver'

service = Service(executable_path=GECKO_DRIVER_PATH)

driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/login")

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("tomsmith")
    password_input.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "flash.success"))
    )

    print(success_message.text.strip())

finally:
    driver.quit()