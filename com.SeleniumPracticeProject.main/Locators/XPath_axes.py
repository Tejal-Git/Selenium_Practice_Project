from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://money.rediff.com/losers/bse/daily/groupall")
driver.maximize_window()

# Self
# # text_msg=driver.find_element(By.XPATH, "//a[normalize-space()='Hemo Organic']/self::a").text
# # print(text_msg)
#
# # Parent
# # text_msg=driver.find_element(By.XPATH, "//a[normalize-space()='Hemo Organic']/parent::td").text
# # print(text_msg)

# child
# text_msg = driver.find_elements(By.XPATH, "//a[normalize-space()='Hemo Organic']/ancestor::tr/child::td")
# print(len(text_msg))
#
# # ancestor
# text_msg=driver.find_element(By.XPATH, "//a[normalize-space()='Hemo Organic']/ancestor::tr").text
# print(text_msg)

# decendant
# text_msg=driver.find_elements(By.XPATH, "//a[normalize-space()='Hemo Organic']/ancestor::tr/descendant::*")
# print(len(text_msg))

# following
# text_msg=driver.find_elements(By.XPATH, "//a[normalize-space()='Hemo Organic']/ancestor::tr/following::*")
# print(len(text_msg))

# following-sibling
# text_msg=driver.find_elements(By.XPATH, "//a[normalize-space()='Hemo Organic']/ancestor::tr/following-sibling::*")
# print(len(text_msg))

# preceding
# text_msg=driver.find_elements(By.XPATH, "//a[normalize-space()='Hemo Organic']/ancestor::tr/preceding::*")
# print(len(text_msg))

# preceding siblings
# text_msg=driver.find_elements(By.XPATH, "//a[normalize-space()='Hemo Organic']/ancestor::tr/preceding-sibling::tr")
# print(len(text_msg))
