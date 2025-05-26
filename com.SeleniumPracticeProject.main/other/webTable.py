from selenium import webdriver
import  time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

# count rows and columns from table
noofrows=(len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")))
print(noofrows)
noofcolumns=(len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")))
print(noofcolumns)

# print specific raw and column value
# data=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[6]/td[2]").text
# print(data)

# print all rows and columns value
# for r in range(2,noofrows+1):
#     for c in range(1,noofcolumns+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end='         ')
#     print()

# read data based on condition
for r in range(2,noofrows+1):
    authorname=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorname=="Mukesh":
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookname, '     ',authorname,'    ',price)


driver.close()