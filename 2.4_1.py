from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "button")
    button.click()

finally:
    time.sleep(6)
    browser.quit()

