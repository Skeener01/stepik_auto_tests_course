import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    # //label[contains(text(),"First")]/following-sibling::input
    selectorList = [".first_class", ".second_class", ".third_class"]
    for ccsSelector in selectorList:
        browser.find_element(By.CSS_SELECTOR, f".first_block {ccsSelector} input")\
            .send_keys("Ivan")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    #----
    # strName = str(math.ceil(math.pow(math.pi, math.e)*10000))
    # link1 = browser.find_element(By.PARTIAL_LINK_TEXT, strName)
    # link1.click()
    # elements = browser.find_elements(By.TAG_NAME, "input")
    # for element in elements:
    #     element.send_keys("Мой ответ")
    #----
    # input1 = browser.find_element(By.TAG_NAME, "input")
    # input1.send_keys("Ivan")
    # input2 = browser.find_element(By.NAME, "last_name")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element(By.CLASS_NAME, "city")
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element(By.ID, "country")
    # input4.send_keys("Russia")
    # button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    # button.click()
    #
    # time.sleep(10)

# не забываем оставить пустую строку в конце файла
