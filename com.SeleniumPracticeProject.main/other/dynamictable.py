from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, " //button[normalize-space()='Login']").click()
time.sleep(5)

# alertwindow=driver.switch_to.alert
# alertwindow.accept()

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li").click()
time.sleep(5)


time.sleep(5)

# total rows in a table
rows=len(driver.find_elements(By.XPATH,"url"))
print(rows)

count=0
for r in range(1,rows+1):
    status=driver.find_element(By.XPATH, "url").text
    if status=='enabled':
        count=count+1

print("total numbers of users", rows)
print("total numbers of enabled users", count)
print("total numbers of disabled users", (rows-count))

driver.close()

