from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    xelem = browser.find_element(By.ID, "input_value")
    x = xelem.text
    sum = str(math.log(abs(12*math.sin(int(x)))))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(sum)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radiobutton1 = browser.find_element(By.ID, "robotsRule")
    radiobutton1.click()
    button.click()

    time.sleep(5)

finally:
    time.sleep(10)
    browser.quit()

