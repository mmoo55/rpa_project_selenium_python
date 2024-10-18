from selenium import webdriver


class Edge:
    @staticmethod
    def open_edge():
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-infobars")
        return webdriver.Edge(options=options)