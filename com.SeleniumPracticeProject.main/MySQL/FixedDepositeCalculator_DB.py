from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import mysql.connector

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")

# cop = webdriver.ChromeOptions()
# cop.add_argument("--disable-notifications")
# cop.add_argument("--disable-popup-blocking")

try:
    con = mysql.connector.connect(host="localhost", port="3306", user="root", password="NoAccess@240998", database="Bank")
    curs = con.cursor()  # create cursor
    curs.execute("SELECT * FROM simple_interest_data")  # execute query through cursor

    for row in curs:
        pric = row[0]
        rateofInterest = row[1]
        per1 = row[2]
        per2 = row[3]
        freq = row[4]
        exp_value = row[5]

        # passing data to application
        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pric)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofInterest)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

        perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        perioddrp.select_by_visible_text(per2)

        frequency = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        frequency.select_by_visible_text(freq)

        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()  # calculate button

        act_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        #    Validation
        if float(exp_value) == float(act_value):
            print("Test passed")

        else:
            print("Test failed")

        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(2)
    con.close()
except:
    print("Connection unsuccessful")

driver.close()

