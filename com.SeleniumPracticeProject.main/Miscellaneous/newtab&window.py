from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")

regilink=Keys.CONTROL+Keys.RETURN
driver.find_element(By.XPATH, "//a[normalize-space()='Register']").send_keys(regilink)


# new tab: opens new tab in browser
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window("tab")
# driver.get("https://www.orangehrm.com/")

# new window: opens new window on browser
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window("window")
# driver.get("https://www.orangehrm.com/")





