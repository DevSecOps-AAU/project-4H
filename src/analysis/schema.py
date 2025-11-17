from sqlalchemy import Table, Column, String, Text, TIMESTAMP, MetaData
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

metadata = MetaData()

history = Table(
    "history",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("user_id", String(255), nullable=False, unique=True),
    Column("input_text", Text, nullable=False, unique=True),
    Column("sentiment_label", Text, nullable=False),
    Column("confident_score", Text, nullable=False),
    Column("analysis_timestamp", TIMESTAMP, server_default=func.now()),
)
