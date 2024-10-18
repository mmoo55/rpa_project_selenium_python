from rpa_common.base_rpa.base_rpa_task import BaseRPATask
from rpa_common.database.db_connection import DBConnection
from rpa_common.repositories.google_search_repository import GoogleSearchRepository
from rpa_common.session.session import Session
from src.bots.first_rpa.pages.google_page import GooglePage

class MyRPA(BaseRPATask):
    def open_application(self):
        print("Iniciando la sesión del navegador")
        self.browser_session = Session()
        self.browser = Session().get_browser()

        # # Conexión a la base de datos
        # self.db_connection = DBConnection("search_results.db")  # Especificar la ruta
        # self.db_connection.connect()
        # self.repository = GoogleSearchRepository(self.db_connection)

    def go_to_url(self):
        print("Navegando a Google")
        self.browser.get("https://www.google.com")

    def perform_task(self):
        print("Realizando búsqueda en Google")
        google_page = GooglePage(self.browser)
        google_page.search("Selenium Python")
        self.results = google_page.get_results()

        # print("Resolviendo CAPTCHA")
        # # Aquí captura la imagen del CAPTCHA y la guarda
        # page.captcha_image.screenshot("captcha_image.png")
        #
        # # Resuelve el CAPTCHA usando TwoCaptcha
        # solver = TwoCaptchaSolver(api_key="TU_API_KEY_AQUI")
        # captcha_text = solver.solve_captcha("captcha_image.png")
        #
        # # Ingresa el resultado del CAPTCHA en el campo correspondiente
        # page.captcha_input.send_keys(captcha_text)

    def save_results(self):
        print("Guardando resultados de la búsqueda")
        for index, result in enumerate(self.results[:5], start=1):  # Solo guardamos los primeros 5
            print(f"Resultado {index}: {result.text}")
            # self.repository.save_search_result("Selenium Python", result.text) # Guardando en la base de datos

    def close_application(self):
        print("Cerrando el navegador")
        self.browser_session.close_browser()