from pydantic import BaseModel

class Historyrequest(BaseModel):
    input_text: str
    sentiment_label: str
    confindence_score: int
    