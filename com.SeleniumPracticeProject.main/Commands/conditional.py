from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

# is_displayed & is_enabled
# search_box=driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# print(search_box.is_displayed())
# print(search_box.is_enabled())

# is_selected
# rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
# rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
#
# print(rd_male.is_selected())
# print(rd_female.is_selected())
#
# rd_male.click()
#
# print(rd_male.is_selected())
# print(rd_female.is_selected())
#
# rd_female.click()
# print(rd_male.is_selected())
# print(rd_female.is_selected())