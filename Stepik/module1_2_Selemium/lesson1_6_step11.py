import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"
selectorList = [".first_class", ".second_class", ".third_class"]

with webdriver.Chrome() as browser:
    browser.get(link)
    for uniqueSelector in selectorList:
        browser.find_element(By.CSS_SELECTOR, f".first_block {uniqueSelector} input")\
            .send_keys("Text filler")
    browser.find_element(By.CSS_SELECTOR, "button.btn")\
        .click()
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(5)  # just to see result
