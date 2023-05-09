from pydantic import BaseModel
from datetime import date, time

class TimeRecord(BaseModel):
    user_uuid: str
    description: str
    duration: time
    start: time
    end: time
    date: date
