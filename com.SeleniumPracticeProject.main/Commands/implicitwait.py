from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.google.com/")
searchbox=driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
# time.sleep(5)
searchbox.submit()

driver.close()