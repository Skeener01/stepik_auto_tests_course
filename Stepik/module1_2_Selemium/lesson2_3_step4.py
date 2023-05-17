import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    confirm = browser.switch_to.alert.accept()

    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(10)
