from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get("http://uitestingplayground.com/classattr")

button = driver.find_element(By.CLASS_NAME, 'btn-primary')

for _ in range(3):
        button.click()
        print("Нажата кнопка.")
        time.sleep(1)

driver.quit()