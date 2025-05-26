from selenium import webdriver
import time
from time import sleep

from selenium.webdriver.common.by import By



driver= webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
time.sleep(3)

driver.find_element(By.ID, "Email").clear()
time.sleep(3)
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
time.sleep(3)
driver.find_element(By.NAME, "Password").clear()
time.sleep(3)
driver.find_element(By.NAME,"Password").send_keys("admin")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
time.sleep(3)

act_title1=driver.title
exp_title1="nopCommerce"

if act_title1==exp_title1:
    print("Login test Passed")
else:
    print("Login test failed ")

driver.close()

