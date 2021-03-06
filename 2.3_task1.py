from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    confirm = browser.switch_to_alert()
    confirm.accept()

    findX = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = findX.text

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(x))

    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
