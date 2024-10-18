class BaseRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def execute_query(self, query, params=None):
        try:
            cursor = self.db_connection.get_connection().cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.db_connection.get_connection().commit()
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            raise

    def insert_data(self, query, params):
        try:
            cursor = self.db_connection.get_connection().cursor()
            cursor.execute(query, params)
            self.db_connection.get_connection().commit()
            print("Datos insertados correctamente")
        except Exception as e:
            print(f"Error al insertar datos: {e}")
            raise

