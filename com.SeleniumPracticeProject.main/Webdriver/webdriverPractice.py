import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
sleep(3)
# driver.minimize_window()
# time.sleep(3)
# driver.close()

driver.find_element( By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()



act_title=driver.title
exp_title="Human Resources Management Software | OrangeHRM HR Software"

if act_title==exp_title:
    print("Login test passed")
else:
    print("login test failed")

time.sleep(10)
driver.close()