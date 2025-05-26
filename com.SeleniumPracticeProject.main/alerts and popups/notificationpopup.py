from selenium import webdriver
import time
from selenium.webdriver.common.by import By

cop=webdriver.ChromeOptions()
cop.add_argument("--disable-notifications")

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://whatmylocation.com/")
