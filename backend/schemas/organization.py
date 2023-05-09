from pydantic import BaseModel

class Organization(BaseModel):
    admin_uuid: str
    name: str
    description: str
