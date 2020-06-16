from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)

    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x + y))

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
