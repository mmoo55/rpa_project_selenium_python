from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Control:
    def __init__(self, browser, locator):
        self.browser = browser
        self.locator = locator
        self.control: WebElement = None

    def find_element(self):
        self.control = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.locator)
        )

    def find_elements(self):
        # Devuelve una lista de elementos que coinciden con el localizador
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(self.locator)
        )

    def click(self):
        self.find_element()
        self.control.click()

    def get_text(self):
        self.find_element()
        return self.control.text