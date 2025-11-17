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
