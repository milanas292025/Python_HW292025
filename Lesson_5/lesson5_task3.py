from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import FireFoxDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.FireFox(service=FireFoxService(FireFoxDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Sky")

driver.clear()

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Pro")

driver.quit()

