from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

gecko_path = r'C:/path/to/your/geckodriver.exe'

service = Service(executable_path=gecko_path)

driver = webdriver.Firefox(service=service)


driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.TAG_NAME, "input")

input_field.send_keys("Sky")
time.sleep(1)

input_field.clear()
time.sleep(1)

input_field.send_keys("Pro")
time.sleep(1)

driver.quit()
