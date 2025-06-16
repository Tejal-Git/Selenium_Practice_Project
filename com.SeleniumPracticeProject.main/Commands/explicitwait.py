from jinja2.nodes import FromImport
from selenium import webdriver
import time

from selenium.common import NoSuchDriverException, NoSuchElementException, ElementNotVisibleException,ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.maximize_window()

# mywait=WebDriverWait(driver,10)
mywait=WebDriverWait(driver,10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException,Exception]) #explicit wait declaration

driver.get("https://www.google.com/")

searchbox=driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
searchbox.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
searchlink.click()

driver.close()

