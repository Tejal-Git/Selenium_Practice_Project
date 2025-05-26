from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver=webdriver.Chrome(options=ops)
    driver.maximize_window()


    return driver

driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)

