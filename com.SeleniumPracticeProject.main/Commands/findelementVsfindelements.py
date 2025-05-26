from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


# locator matching with single webelement
# search=driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# search.send_keys("apple laptop")

# locators matching with multiple webelements
# search=driver.find_element(By.XPATH, "//div[@class='footer-upper']//a")
# print(search.text)  -->prints first link from the footer section

# element not available then throw NosuchElementException
# login_element=driver.find_element(By.LINK_TEXT, "Log")
# login_element.click()

#find_elements()- returns multiple webelements
# locator matching with single webelement
# search=driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(search)) #1
# (search[0].send_keys("apple laptop"))
# time.sleep(5)

# locators matching with multiple webelements
# search=driver.find_elements(By.XPATH, "//div[@class='footer-upper']//a")
# print(len(search)) #1
# print(search[0].text)
# time.sleep(5)
# for sea in search:
#     print(sea.text)

# element not available then throw NosuchElementException
# login_element=driver.find_elements(By.LINK_TEXT, "Log")
# print(len(login_element))