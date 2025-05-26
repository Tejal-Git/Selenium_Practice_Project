from selenium import webdriver
from selenium.webdriver.common.by import  By
import time
from time import sleep




driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# ID and Name locators
# driver.find_element(By.ID,"small-searchterms").send_keys("Apple iPhone 16 128GB")

#linktext and partiallinktext locators
# driver.find_element(By.LINK_TEXT, "Register").click()
# # driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()
# time.sleep(10)

# driver.close()
# driver.quit()

# class_name and tag_name locators
# sliders=driver.find_elements(By.CLASS_NAME, "slider-img")
# print(len(sliders))
# links=driver.find_elements(By.TAG_NAME, "a")
# print(len(links))

