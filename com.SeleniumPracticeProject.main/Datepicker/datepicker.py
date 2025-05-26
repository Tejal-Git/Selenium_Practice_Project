from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)

# driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys('05/30/1998')

# select month and year
year= "2026"
month="August"
date="24"

driver.find_element(By.XPATH, "//*[@id='datepicker']").click()

while True:
    mon=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  #next arrow


# select date
dates=driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for ele in dates:
    if ele.text==date:
        ele.click()
        break

time.sleep(5)