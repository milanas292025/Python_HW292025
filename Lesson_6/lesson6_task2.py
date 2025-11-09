from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)


driver.get("http://uitestingplayground.com/textinput")

text_field = driver.find_element(By.ID, "newButtonName")
text_field.send_keys("SkyPro")

submit_button = driver.find_element(By.ID, "updatingButton")
submit_button.click()


updated_button_text = submit_button.text
print(updated_button_text)

driver.quit()