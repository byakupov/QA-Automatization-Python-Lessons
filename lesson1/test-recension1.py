from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    First_name = browser.find_element(By.XPATH,'//input[@placeholder="Input your first name"]')
    First_name.send_keys("Alex")
    Last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    Last_name.send_keys("Kly")
    Email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    Email.send_keys("asfsdf@mail.ru")
    time.sleep(5)
    ...

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(15)
    browser.close()
    browser.quit()
