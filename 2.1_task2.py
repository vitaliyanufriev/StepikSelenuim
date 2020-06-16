from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    chkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    chkbox.click()

    radiobtn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobtn.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
