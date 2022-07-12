from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ёж")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Мапёжьевич")
    email1 = browser.find_element(By.NAME, "email")
    email1.send_keys("ejlesnoy@mail.ru")

    uploadfile = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'hw.txt')
    uploadfile.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(1)

finally:
    time.sleep(8)
    browser.quit()