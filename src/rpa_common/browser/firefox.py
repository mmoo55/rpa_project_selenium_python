from selenium import webdriver


class Firefox:
    @staticmethod
    def open_firefox():
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-infobars")
        return webdriver.Firefox(options=options)