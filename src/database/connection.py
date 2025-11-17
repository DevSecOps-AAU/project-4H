from sqlalchemy import create_engine, MetaData
import uuid
from datetime import datetime , timezone

engine = create_engine("postgresql+psycopg2://postgres:Suliman5544@localhost:5432/todolist_db")

metadata = MetaData()
metadata.create_all(bind=engine)

new_uuid = uuid.uuid4()
now = datetime.now()