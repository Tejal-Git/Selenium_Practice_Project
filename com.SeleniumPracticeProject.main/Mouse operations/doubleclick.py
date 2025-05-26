from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.w3schools.com/TAgs/tryit.asp?filename=tryhtml5_ev_ondblclick")

driver.switch_to.frame("iframeResult")

field=driver.find_element(By.XPATH, "//button[normalize-space()='Double-click me']")

act=ActionChains(driver)
act.double_click(field).perform()