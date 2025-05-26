from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.w3schools.com/htmL//html5_draganddrop.asp")

src_ele=driver.find_element(By.XPATH,"//*[@id='div1']")
# src_ele=driver.find_element(By.ID,"div1")
tar_ele= driver.find_element(By.XPATH, "//div[@id='div2']")
# tar_ele= driver.find_element(By.XPATH, "div2")

act=ActionChains(driver)
act.drag_and_drop(src_ele,tar_ele).perform()