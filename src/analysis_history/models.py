from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class AnalysisHistoryCreate(BaseModel):
    user_id: UUID
    input_text: str
    sentiment_label: str
    confidence_score: str
    last_analysis_at: datetime


class AnalysisHistory(BaseModel):
    id: UUID
    user_id: UUID
    input_text: str
    sentiment_label: str
    confidence_score: str
    created_at: datetime
    updated_at: datetime
    last_analysis_at: datetime
