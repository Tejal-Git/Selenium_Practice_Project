from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min_slider=driver.find_element(By.XPATH, "//div[@id='slider-range']//span[1]")
max_slider=driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

print(min_slider.location) #{'x': 59, 'y': 256}
print(max_slider.location) #{'x': 613, 'y': 256}

act=ActionChains(driver)

act.drag_and_drop_by_offset(min_slider, 100,0).perform()
act.drag_and_drop_by_offset(max_slider,-38,0).perform()

print(min_slider.location)
print(max_slider.location)