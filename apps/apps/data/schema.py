from datetime import datetime
from pydantic import BaseModel

# Pydantic을 이용한 Type Hinting
class Create(BaseModel):
    time : str
    rfid : str
    temp : float
    breath : int
    
class MemoCreate(BaseModel):
    regdate : datetime
    title : str
    body : str
    
class Select(BaseModel):
    time : str
    rfid : str
    temp : float
    breath : int