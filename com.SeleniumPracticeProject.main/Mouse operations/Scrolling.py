from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)", "")
# value=driver.execute_script("return window.pageYOffset;")
# print("Number of pixer moved: ", value)

# scroll down page till the element is visible
# flag=driver.find_element(By.XPATH, "//img[@alt='Flag of Haiti']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value=driver.execute_script("return window.pageYOffset;")
# print("Number of pixer moved: ", value) #Number of pixer moved:  7268.7998046875

# scroll down to page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixer moved: ", value) #Number of pixer moved:  9592

# scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixer moved ",value) #Number of pixer moved  0
