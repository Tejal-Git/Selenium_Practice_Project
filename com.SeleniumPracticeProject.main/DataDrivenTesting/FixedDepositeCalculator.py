from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from DataDrivenTesting import XLUtility


driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")

cop=webdriver.ChromeOptions()
cop.add_argument("--disable-notifications")
cop.add_argument("--disable-popup-blocking")

file= "D:\Tejal\software projects\Selenium_Projects\Git\Book3.xlsx"

time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='wzrk-cancel']").click()
rows=XLUtility.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    pric=XLUtility.readData(file,"Sheet1",r,1)
    rateofInterest=XLUtility.readData(file,"Sheet1",r,2)
    per1=XLUtility.readData(file,"Sheet1",r,3)
    per2=XLUtility.readData(file,"Sheet1",r,4)
    freq=XLUtility.readData(file,"Sheet1",r,5)
    exp_value=XLUtility.readData(file,"Sheet1",r,6)

    # passing data to application
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofInterest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

    perioddrp=Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)

    frequency=Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequency.select_by_visible_text(freq)


    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click() #calculate button

    act_value=driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

#    Validation
    if float(exp_value)==float(act_value):
        print("Test passed")
        XLUtility.writeData(file,"Sheet1",r,8, "Passed")
        XLUtility.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test failed")
        XLUtility.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtility.fillRedColor(file, "Sheet1", r, 8)

    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)

driver.close()

