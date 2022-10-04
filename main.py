from typing import Optional
import uvicorn
from fastapi import FastAPI
from routes.sensor import router as sensor_router

app = FastAPI()
app.include_router(sensor_router)

@app.post("/")
async def index():
    return {"Hello":"World"}