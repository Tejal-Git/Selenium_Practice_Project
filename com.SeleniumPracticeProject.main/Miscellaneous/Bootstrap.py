from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
time.sleep(3)
country_list=driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']//li")
print(len(country_list))

for country in country_list:
    if country.text=="Iran":
        country.click()
        break

time.sleep(3)