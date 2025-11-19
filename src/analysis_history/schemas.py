from sqlalchemy import Table, Column, Text, Integer, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from src.database.execution import db_client



analysis_history = Table(
    "analysis_history",
    db_client.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=db_client.new_uuid),
    Column("user_id", UUID(as_uuid=True), nullable=False),
    Column("input_text", Text),
    Column("sentiment_label", Text),
    Column("confidence_score", Text),
    Column("last_analysis_at", DateTime, nullable=False, **db_client.default_now),
    Column("created_at", DateTime, nullable=False, **db_client.default_now),
    Column(
        "updated_at",
        DateTime,
        nullable=False,
        onupdate=db_client.now,
        **db_client.default_now,
    ),
)
