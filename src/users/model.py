from pydantic import BaseModel

class Userrequest(BaseModel):
    name: str
    email: str
    password: str
