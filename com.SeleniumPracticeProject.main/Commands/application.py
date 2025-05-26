from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()