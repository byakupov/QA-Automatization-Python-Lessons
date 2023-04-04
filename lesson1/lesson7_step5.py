from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    inputName = browser.find_element(By.XPATH, "//input[@name= 'firstname']")
    inputName.send_keys("Ivan")
    inputLastName = browser.find_element(By.XPATH, "//input[@name= 'lastname']")
    inputLastName.send_keys("Ivanov")
    inputEmail = browser.find_element(By.XPATH, "//input[@name= 'email']")
    inputEmail.send_keys("trest@test.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    inputFile = browser.find_element(By.XPATH, "//input[@name='file']")
    inputFile.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()