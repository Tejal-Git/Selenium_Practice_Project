from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("url")

driver.find_element(By.XPATH, "Xpath").click()
driver.find_element(By.XPATH, "xpath").send_keys("location of which file needs to be upload")