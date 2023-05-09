from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.time_record import time_records
from config.db import conn
from schemas.time_record import TimeRecord
import uuid

api = APIRouter(
    prefix = '/time_records',
    tags = ['time_records']
)

@api.get('/')
async def fetch_time_records():
    return conn.execute(time_records.select()).fetchall()

@api.get('/id/{uuid}')
async def fetch_time_record(uuid:str):
    return conn.execute(time_records.select().where(time_records.c.uuid == uuid)).first()

@api.get('/user_id/{uuid}')
async def fetch_time_records_by_user(uuid:str):
    return conn.execute(time_records.select().where(time_records.c.user_uuid == uuid)).fetchall()

@api.post('/')
async def create_time_record(time_record: TimeRecord):
    try:
        new_uuid = str(uuid.uuid4())
        conn.execute(time_records.insert().values(
            uuid = new_uuid,
            user_uuid = time_record.user_uuid,
            description = time_record.description,
            duration = time_record.duration,
            start = time_record.start,
            end = time_record.end,
            date = time_record.date           
        ))
        return conn.execute(time_records.select().where(time_records.c.uuid == new_uuid)).first()
    except:
        raise HTTPException(
            status_code=400,
            detail="invalid user uuid"
        )

@api.put('/{uuid}')
async def update_time_record(uuid:str, time_record: TimeRecord):
    try:
        conn.execute(time_records.update().values(
            user_uuid = time_record.user_uuid,
            description = time_record.description,
            duration = time_record.duration,
            start = time_record.start,
            end = time_record.end,
            date = time_record.date  
        ).where(time_records.c.uuid == id))
        return conn.execute(time_records.select().where(time_records.c.uuid == uuid)).first()
    except:
        raise HTTPException(
            status_code=400,
            detail="invalid user uuid"
        )

@api.delete('/{uuid}')
async def delete_time_record(uuid:str):
    conn.execute(time_records.delete().where(time_records.c.uuid == uuid))
    return {"detail":"success"}
