from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

# driver.save_screenshot(os.getcwd() +"\image.png")
# driver.save_screenshot("D:\Tejal\software projects\Selenium_Projects\Git\Selenium_Practice_Project\com.SeleniumPracticeProject.main\Miscellaneous\Screenshot.py\homepage.png")
driver.get_screenshot_as_file(os.getcwd() +"\image.png")