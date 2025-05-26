from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

def chrome_setup():
    preferences={"download.default_directory":location, "plugins.always_open_pdf_externally":True} #downloading files in desired locations
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver=webdriver.Chrome(options=ops)

    return driver

driver=chrome_setup()

driver.get("https://www.princexml.com/samples/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@id='dictionary']//a[contains(text(),'PDF')]").click()