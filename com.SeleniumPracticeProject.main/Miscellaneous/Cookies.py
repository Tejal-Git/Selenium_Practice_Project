from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")

# capture cookies from the browser
cookies=driver.get_cookies()
print(len(cookies))

# prints details or specific about cookies
# for c in cookies:
#     # print(c)
#     print(c.get('name'),":",c.get("value"))

# add new cookie to the browser
driver.add_cookie({"name":"MyCookie", "value":"123456"})
cookie=driver.get_cookies()
print("Size of the cookies after adding new one", len(cookie))

# delete specific cookie from the browser
driver.delete_cookie("MyCookie")
cookie=driver.get_cookies()
print("Size of the cookies after deleted one", len(cookie))

# Delete all cookies
driver.delete_all_cookies()
cookie=driver.get_cookies()
print("Size of the cookies after deleting all cookies", len(cookie))

