from sqlalchemy import insert, select, func
from src.database.execute import DBClinet
from src.analysis.schema import history

class SentimentAnalysisQuieres:
    def __init__(self):
        self.db_client = DBClinet()

    def record_sentiment(self, text_input, sentiment_score):
        "Insert a new record into history table"
        stmt = insert(history).values(
            text=text_input,
            score=sentiment_score
        )
        row = self.db_client.execute_one(stmt)
        return row

    def get_history(self):
        "Retrive all records"

        stmt = select(history)
        row = self.db_client.execute_all(stmt)
        return row
    

    def get_analytics(self):
        stmt = select (
            func.count(history.c.id).label("total_analysis"),
            func.avg(history.c.score).label("average_score")
        )
        row = self.db_client.execute_all(stmt)
        return row