from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    spanNumberOne = int(browser.find_element(By.ID, "num1").text)
    spanNumberTwo = int(browser.find_element(By.ID, "num2").text)
    summNumbers = spanNumberOne+spanNumberTwo
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(summNumbers))
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла