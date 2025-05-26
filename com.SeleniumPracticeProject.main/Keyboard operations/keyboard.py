from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://text-compare.com/")

input1=driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input1.send_keys("Hello, world!")

act=ActionChains(driver)

# input1--> ctrlA select the text
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()


# input1 --> ctrlC copy text
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()


# press tab key to navigate to input2
act.send_keys(Keys.TAB)
act.perform()


# input2 -->ctrlV paste the text
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()