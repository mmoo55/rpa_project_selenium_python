from rpa_common.repositories.base_repository import BaseRepository

class GoogleSearchRepository(BaseRepository):
    def save_search_result(self, search_term, result):
        query = """
            INSERT INTO google_searches (search_term, result)
            VALUES (?, ?)
        """
        self.insert_data(query, (search_term, result))

    def get_search_results(self, search_term):
        query = "SELECT * FROM google_searches WHERE search_term = ?"
        return self.execute_query(query, (search_term,))
