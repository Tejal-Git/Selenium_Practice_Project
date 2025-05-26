from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# approach 1
# # windowid=driver.current_window_handle
# # # print(windowid) 5B505B8728C2D4224534382F34F5CCF7
#
driver.find_element(By.PARTIAL_LINK_TEXT,"OrangeH").click()
windowIDs=driver.window_handles
#
# parentwindow=windowIDs[0]
# childwindow=windowIDs[1]
#
# # print(parentwindow,childwindow)
#
# driver.switch_to.window(childwindow)
# print("title of the childwindow", driver.title)
#
# driver.switch_to.window(parentwindow)
# print("title of the parent window", driver.title)

# approach 2
# for winid in windowsIDs:
#     driver.switch_to.window(windid)
#     print(driver.title)

# approach 3
# for winid in windowsIDs:
#     driver.switch_to.window(windid)
#     if driver.title==orangeHRM:
#         driver.close()
