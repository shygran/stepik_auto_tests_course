from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #открытие ссылки
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #нажатие на нужную кнопку
    button = browser.find_element(By.ID, "button")
    button.click()

finally:
    #закрытие страницы через 6 секунд
    time.sleep(6)
    browser.quit()

