from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    #Посчитать математическую функцию от x
    y = calc(x)

    #Ввести ответ в текстовое поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    #Отметить checkbox "I'm the robot"
    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    #Выбрать radiobutton "Robots rule!".
    radiobutton1 = browser.find_element(By.ID, "robotsRule")
    radiobutton1.click()

    #Нажать на кнопку Submit
    submitbutton = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    submitbutton.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()



