from lib2to3.pytree import Base
from tokenize import String
from typing import Optional
import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class Item(BaseModel):
    time : str
    temp : float
    breath : int
    rfid : str

app = FastAPI()

@app.post("/sensors")
async def get_sensor_data(data : Item):
    return data.time