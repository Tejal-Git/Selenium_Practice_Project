import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

# 1. select specific checkbox
# checkbox=driver.find_element(By.XPATH,"//input[@id='sunday']")
# checkbox.click()
# time.sleep(3)

# 2. select all the checkboxes
checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains (@id, 'day')]")
print(len(checkboxes))

# approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# approach 2
# for checkbox in checkboxes:
#     checkbox.click()

# approach 3: select multiple check boxes by choice
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('id')
#     if weekname=='sunday' or weekname=='monday':
#         checkbox.click()

# approach 4 : select last checkboxes
# range(5,7)--> 6,7
# totalnumberofelement-2= starting index , totalnumberofelement=last index
# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click()

# approach 5 : select first 2 chekboxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

# approach 6: clearing all the checkboxes
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()