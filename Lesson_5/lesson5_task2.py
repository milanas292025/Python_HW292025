from time import sleep
from tkinter import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://www.uitestingplayground.com/dynamicid")

driver.find_element(By.LINK_TEXT,"Button with Dynamic ID").click()
element_clik Button color="Blue"    # не знаю, как обозначить синюю кнопку

driver.quit()

sleep(10)