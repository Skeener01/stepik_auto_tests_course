import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://qa-todo.vercel.app"

with webdriver.Chrome() as browser:
    browser.get(link)

    titleAdd = browser.find_element(By.CSS_SELECTOR, "#new-todo")
    buttonAdd = browser.find_element(By.CSS_SELECTOR, "button[onclick='addTodo()']")
    for x in range(258):
        titleAdd.send_keys(x)
    buttonAdd.click()
    time.sleep(10)
