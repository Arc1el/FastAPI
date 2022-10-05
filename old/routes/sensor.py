from typing import Optional
import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.connection import get_db
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    time : str
    temp : float
    breath : int
    rfid : str

@router.post("/sensor")
async def get_sensor_data(data : Item):
    return data.dict()