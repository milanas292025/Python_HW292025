from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()


browser.get("http://uitestingplayground.com/ajax")

blue_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
blue_button.click()

wait = WebDriverWait(browser, 10)
green_panel = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bg-success")))

result_text = green_panel.text
if result_text == "Data loaded with AJAX get request.":
 print(result_text)
else:
 raise ValueError(f"Неправильный текст: '{result_text}'")

browser.quit()