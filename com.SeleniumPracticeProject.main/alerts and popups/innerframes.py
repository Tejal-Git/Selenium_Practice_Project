from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("URL")

name_of_the_outerframe=driver.find_element(By.XPATH, "value of xpath")
driver.switch_to.frame(name_of_the_outerframe)

name_of_the_innerframe=driver.find_element(By.XPATH, "value of xpath")
driver.switch_to.frame(name_of_the_innerframe)

# innerbox insert the value
driver.find_element(By.XPATH, "VALUE").send_keys("welcome")