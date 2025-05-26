from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content() #go back to main page

driver.switch_to.frame("")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content() #go back to main page

driver.switch_to.frame("")
driver.find_element(By.XPATH,  "/html/body/div[1]/header/nav/div[1]/ul/li[8]/a")
