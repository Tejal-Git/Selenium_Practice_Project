from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("Hello, world!")

# alertwindow.accept() #close alert window by using ok button
alertwindow.dismiss() #close alert window by using cancel button
time.sleep(5) 