from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elem1 = browser.find_element(By.ID, "num1")
    el1 = elem1.text
    elem2 = browser.find_element(By.ID, "num2")
    el2 = elem2.text
    sum = int(el1) + int(el2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

    submitbutton = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    submitbutton.click()

    time.sleep(1)

finally:
    time.sleep(2)
    browser.quit()

