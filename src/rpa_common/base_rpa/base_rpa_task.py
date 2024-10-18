class BaseRPATask:
    def execute_task(self):
        self.open_application()
        self.go_to_url()
        self.perform_task()
        self.save_results()
        self.close_application()

    def open_application(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def go_to_url(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def perform_task(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def save_results(self):
        print("Guardando resultados...")

    def close_application(self):
        print("Cerrando la aplicación...")