from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from rpa_common.control.label import Label
from rpa_common.control.text_box import TextBox


class GooglePage:
    def __init__(self, browser):
        # self.browser = browser
        self.search_box_txtbox = TextBox(browser, (By.NAME, 'q'))
        self.result_label = Label(browser, (By.CSS_SELECTOR, 'div.g'))

    def search(self, query):
        self.search_box_txtbox.set_text(query)
        self.search_box_txtbox.set_text(Keys.RETURN)

    def get_results(self):
        return self.result_label.find_elements()