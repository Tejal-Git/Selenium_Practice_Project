from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep

driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)
# driver.close()
driver.quit()