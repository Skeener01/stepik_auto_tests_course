import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "https://suninjuly.github.io/selects2.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    y = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    result = x + y

    browser.find_element(By.CSS_SELECTOR, "select").click()
    browser.find_element(By.CSS_SELECTOR, "select [value=\"" + str(result) + "\"]").click()

    # browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    # browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(10)
