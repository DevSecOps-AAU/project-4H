from uuid import UUID
from src.analysis_history.queries import HistoryQueries


class HistoryService:
    def __init__(self):
        self.analysis_queries = HistoryQueries()

    def create_analysis_history(self, analyze_history_data: HistoryQueries):
        row = self.analysis_queries.create_analysis_history(analyze_history_data)
        if not row:
            return 400, None
        return 200, row
    
    def get_record_by_id(self, history_id: UUID):
        row = self.analysis_queries.get_record_by_id(history_id)
        if not row:
            return None
        return row
    
    def get_history_by_user_id(self, user_id:UUID):
        row = self.analysis_queries.get_history_by_user_id(user_id)
        if not row:
            return []
        return row
