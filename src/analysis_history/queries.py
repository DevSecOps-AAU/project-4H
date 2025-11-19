from src.analysis_history.schemas import analysis_history
from src.database.execution import db_client
from src.authentication.hash import HashHelper
from src.analysis_history.models import AnalysisHistoryCreate
from uuid import UUID
from sqlalchemy import (
    select,
    insert,
)


class HistoryQueries:
    def __init__(self):
        self.db_client = db_client
        self.hash_helper = HashHelper()

    def create_analysis_history(self, analysis_history:AnalysisHistoryCreate):
        stmt = insert(analysis_history).values(analysis_history).returning(analysis_history)
        result = self.db_client.execute_one(stmt)
        return result
    
    def get_record_by_id(self, record_id: UUID):
        stmt = select(analysis_history).where(analysis_history.c.id == record_id)
        result = self.db_client.execute_one(stmt)
        return result
    
    def get_history_by_user_id(self, user_id: UUID):
        stmt = (
            select(analysis_history)
            .where(analysis_history.c.user_id == user_id) 
        )
        result = self.db_client.execute_all(stmt)
        return result
    
