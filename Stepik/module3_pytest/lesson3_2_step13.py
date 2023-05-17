import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

pages = ["registration1.html", "registration2.html"]
selectorList = [".first_class", ".second_class", ".third_class"]
finalText = "Congratulations! You have successfully registered!"


class TestAbs(unittest.TestCase):

    def runWebScript(self, pageAdr):
        with webdriver.Chrome() as browser:
            browser.get(f"http://suninjuly.github.io/{pageAdr}")
            for ccsSelector in selectorList:
                browser.find_element(By.CSS_SELECTOR, f".first_block {ccsSelector} input") \
                    .send_keys("Ivan")
            browser.find_element(By.CSS_SELECTOR, "button.btn") \
                .click()
            time.sleep(1)
            self.welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    def test_abs1(self):
        self.runWebScript(pages[0])
        self.assertEqual(self.welcome_text, finalText, "Text should be the same")

    def test_abs2(self):
        self.runWebScript(pages[1])
        self.assertEqual(self.welcome_text, finalText, "Text should be the same")


if __name__ == "__main__":
    unittest.main()
