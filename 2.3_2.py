from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, "button")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    browser.switch_to.window(browser.window_handles[0])

    #Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    #Посчитать математическую функцию от x
    y = calc(x)

    #Ввести ответ в текстовое поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)


    #Нажать на кнопку Submit
    submitbutton = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submitbutton.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    time.sleep(6)
    browser.quit()



