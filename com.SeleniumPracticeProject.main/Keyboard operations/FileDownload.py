from selenium import webdriver
import time
from  selenium.webdriver.common.by import By
import os
location=os.getcwd()

def chrome_setup():

    preferences={"download.default_directory": location }
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(options=ops)


    return driver

driver=chrome_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='table-files'']/tbody/tr[1]/td[5]/a").click()