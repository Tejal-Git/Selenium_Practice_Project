from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep

driver=webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.get("https://www.google.com/")

driver.back()
driver.forward()

driver.refresh()