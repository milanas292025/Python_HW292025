from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

delay_field = driver.find_element(By.ID,"delay")
delay_field.clear()
delay_field.send_keys("45")

buttons = {
    "seven": "7",
    "plus": "+",
    "eight": "8",
    "equal": "=",
    }

for key in ["seven", "plus", "eight", "equal"]:
    button = driver.find_element(By.ID, key)
    button.click()

time.sleep(50)

display_value = driver.find_element(By.ID,"display").text
assert display_value == "15", f"Результат неверный. Текущий результат: {display_value}"

print("Автотест успешно прошел!")
driver.quit()