from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str
    firstname: str
    lastname: str
