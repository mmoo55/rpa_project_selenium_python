from rpa_common.browser.browser import BrowserFactory


class Session:
    _instance = None
    # _browser = None

    def __new__(cls, browser_type='chrome'):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._browser = BrowserFactory.create_browser(browser_type)
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Session()
        return cls._instance
    def get_browser(self):
        return self._instance._browser

    def close_browser(self):
        if self._instance._browser:
            self._instance._browser.quit()
            Session._instance = None