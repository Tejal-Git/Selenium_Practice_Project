from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/")
driver.maximize_window()

#CSS operators/ selectors
# 1. tag & ID
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")
# time.sleep(3)

# tag and class
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abcd")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abcd")
# time.sleep(3)

# tag and attribute
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal-email]").send_keys("abcd@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal-email]").send_keys("abcd@gmail.com")
# time.sleep(3)

# tag and attribute and class
# driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal-pass]").send_keys("abcd@gmail.com")
# time.sleep(3)