from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log((abs(12 * math.sin(int(x))))))


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(x))

    robot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot.click()

    radiobtn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobtn)
    radiobtn.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()