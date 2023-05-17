import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "https://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = calc(x)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    # browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    button.click()
    time.sleep(10)
