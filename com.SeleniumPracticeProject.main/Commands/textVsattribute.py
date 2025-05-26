from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
driver.maximize_window()

# emailbox=driver.find_element(By.XPATH, "//input[@id='Email']")
# emailbox.send_keys("abc@gmail.com")
#
# print("result of text: ", emailbox.text)
# print("result of get_attribute: ", emailbox.get_attribute("value"))

button= driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
# print("result of text: ", button.text)
# print("result of get_attribute: ", button.get_attribute("value"))