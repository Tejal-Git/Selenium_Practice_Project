from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.driver_finder import DriverFinder
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

# Date of Birth

driver.find_element(By.XPATH, "//input[@id='dob']").click() #opens date picker element

datepicker_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Sep") #month selection

datepicker_year= Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("1998") #year selection

# select date
dates= driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text=='24':
        ele.click()
        break

time.sleep(5)
