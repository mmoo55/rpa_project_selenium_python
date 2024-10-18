from rpa_common.browser.chrome import Chrome
from rpa_common.browser.edge import Edge
from rpa_common.browser.firefox import Firefox


class BrowserFactory:
    @staticmethod
    def create_browser(browser_type='chrome'):
        if browser_type.lower() == 'chrome':
            return Chrome.open_chrome()
        elif browser_type.lower() == 'firefox':
            return Firefox.open_firefox()
        elif browser_type.lower() == 'edge':
            return Edge.open_edge()
        else:
            raise ValueError(f"Navegador {browser_type} no soportado.")