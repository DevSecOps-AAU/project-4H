from src.database.connection import engine

class DBClinet:
    def __init__(self):
        self.engine = engine

    def execute_one(self, query):
        with self.engine.begin() as connection:
            rows = connection.execute(query)
            if rows:
                return rows.mappings.all()
        return None

    def execute_all(self, query):
        with self.engine.begin() as connection:
            rows = connection.execute(query)
            if rows:
                return rows.mappings.all()
        return None

