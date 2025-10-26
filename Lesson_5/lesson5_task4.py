from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import FireFoxDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.FireFox(service=FireFoxService(FireFoxDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

search_box = driver.find_element(By.NAME, "username")
search_box.send_keys("tomsmith")

search_box = driver.find_element(By.NAME, "password")
search_box.send_keys("SuperSecretPassword")

driver.find_element(By.LINK_TEXT,"Button Login").click()

#Вывести текст с зеленой плашки в консоль. не знаю как

driver.quit()