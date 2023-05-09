from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.organization import organizations
from config.db import conn
from schemas.organization import Organization
import uuid

api = APIRouter(
    prefix = '/organizations',
    tags = ['organizations']
)

@api.get('/')
async def fetch_organizations():
    return conn.execute(organizations.select()).fetchall()

@api.get('/id/{uuid}')
async def fetch_organization(uuid:str):
    return conn.execute(organizations.select().where(organizations.c.uuid == uuid)).first()

@api.post('/')
async def create_organization(organization: Organization):
    try:
        new_uuid = str(uuid.uuid4())
        conn.execute(organizations.insert().values(
            uuid = new_uuid,
            admin_uuid = organization.admin_uuid,
            name = organization.name,
            description = organization.description           
        ))
        return conn.execute(organizations.select().where(organizations.c.uuid == new_uuid)).first()
    except:
        raise HTTPException(
            status_code=400,
            detail="invalid admin uuid"
        )

@api.put('/{uuid}')
async def update_organization(uuid:str, organization: Organization):
    try:
        conn.execute(organizations.update().values(
            admin_uuid = organization.admin_uuid,
            name = organization.name,
            description = organization.description
        ).where(organizations.c.uuid == id))
        return conn.execute(organizations.select().where(organizations.c.uuid == uuid)).first()
    except:
        raise HTTPException(
            status_code=400,
            detail="invalid admin uuid"
        )

@api.delete('/{uuid}')
async def delete_organization(uuid:str):
    conn.execute(organizations.delete().where(organizations.c.uuid == uuid))
    return {"detail":"success"}
