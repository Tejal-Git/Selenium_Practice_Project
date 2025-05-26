from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.opencart.com/index.php?route=account/register")

time.sleep(15)

dropdown=driver.find_element(By.XPATH, "//select[@id='input-country']")
drops=Select(dropdown)

# select option from dropdown
# drop.select_by_visible_text("India")
# drop.select_by_value("14")
# drop.select_by_index(15)

# capture all the options and print them
# alloptions=drops.options
# print(len(alloptions))
#
# for opt in alloptions:
#     print(opt.text)

# # select all the options from dropdown without using built-in method
# for opt in alloptions:
#     if opt.text=="India":
#         opt.click()
#         break

# if we don't want to use the select class
alloptions=driver.find_elements(By.XPATH, "//select[@id='input-country']/option")
print(len(alloptions))