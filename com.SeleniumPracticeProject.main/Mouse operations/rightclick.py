from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button=driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)
act.context_click(button).perform()