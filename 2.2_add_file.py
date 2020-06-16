import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, ".form-group [name='firstname']")
    first_name.send_keys('firstname')

    last_name = browser.find_element(By.CSS_SELECTOR, ".form-group [name='lastname']")
    last_name.send_keys('lastname')

    email = browser.find_element(By.CSS_SELECTOR, ".form-group [name='email']")
    email.send_keys('email@test.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'stepik.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, '#file')
    element.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
