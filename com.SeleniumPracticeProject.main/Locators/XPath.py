from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Absolute XPATH
# driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Laptop")
# driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()
# time.sleep(5)

# Relative XPATH
# driver.find_element(By.XPATH, "//*[@id='small-searchterms']").send_keys("Laptop")
# driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button").click()
# time.sleep(10)

