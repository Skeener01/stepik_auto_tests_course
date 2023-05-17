import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get(link)
    # browser.switch_to.window(window_name)
    # new_window = browser.window_handles[1]
    # first_window = browser.window_handles[0]
    browser.find_element(By.CSS_SELECTOR, ".trollface").click()
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(10)
