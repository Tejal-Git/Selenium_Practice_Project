from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests as requests

driver=webdriver.Chrome()
driver.maximize_window()

# driver.get("https://demo.nopcommerce.com/")

# click on link
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital downloa").click()

# FIND NUMBER OF LINKS IN A PAGE
# links=driver.find_elements(By.XPATH, "//a")
# print(len(links))
#
# print all the link names
# for link in links:
#     print(link.text)

#  broken links
# we need to install requests package through file--> setting--> project interpreter-->requests

driver.get("http://www.deadlinkcity.com/")
alllinks=driver.find_elements(By.TAG_NAME, "a")
count=0

for link in alllinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url, "is a broken link")
        count+=1
    else:
        print(url, "is a valid link")

print("total numbers of links", count)

