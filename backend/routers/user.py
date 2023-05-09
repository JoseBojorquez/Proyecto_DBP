from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from models.user import users
from config.db import conn
from schemas.user import User
import uuid

api = APIRouter(
    prefix = '/users',
    tags = ['users']
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@api.get('/')
async def fetch_users():
    return conn.execute(users.select()).fetchall()

@api.get('/id/{uuid}')
async def fetch_user(uuid:str):
    return conn.execute(users.select().where(users.c.uuid == uuid)).first()

@api.post('/')
async def create_user(user: User):
    try:
        new_uuid = str(uuid.uuid4())
        conn.execute(users.insert().values(
            uuid = new_uuid,
            email = user.email,
            password = get_password_hash(user.password),
            firstname = user.firstname,
            lastname = user.lastname           
        ))
        return conn.execute(users.select().where(users.c.uuid == new_uuid)).first()
    except:
        raise HTTPException(
            status_code=400,
            detail="email already registered"
        )

@api.put('/{uuid}')
async def update_user(uuid:str, user: User):
    try:
        conn.execute(users.update().values(
            email = user.email,
            firstname = user.firstname,
            lastname = user.lastname 
        ).where(users.c.uuid == id))
        return conn.execute(users.select().where(users.c.uuid == uuid)).first()
    except:
        raise HTTPException(
            status_code=400,
            detail="email already registered"
        )

@api.delete('/{uuid}')
async def delete_user(uuid:str):
    conn.execute(users.delete().where(users.c.uuid == uuid))
    return {"detail":"success"}
