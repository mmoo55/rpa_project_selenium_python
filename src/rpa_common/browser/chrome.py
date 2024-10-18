from selenium import webdriver


class Chrome:
    @staticmethod
    def open_chrome():
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-infobars")
        return webdriver.Chrome(options=options)