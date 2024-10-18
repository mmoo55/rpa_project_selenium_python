import sqlite3

class DBConnection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            print("Conexión a la base de datos establecida")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión a la base de datos cerrada")

    def get_connection(self):
        if not self.connection:
            self.connect()
        return self.connection
