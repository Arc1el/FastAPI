from databases.core import Database
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from fastapi.requests import Request
from typing import List

# 스키마 
from apps.data.schema import Create, Select, MemoCreate
# 모델
from apps.data.model import memo

memo_router = APIRouter()


def get_db_conn(request: Request):
    return request.state.db_conn		# middleware 에서 삽입해준 db_conn

@memo_router.get("/test")
async def test():
    return {"say":"hello"}

# create
@memo_router.post("/sensor")
async def create(
    req: MemoCreate,					# 요청을 정의한 create 스키마에 맞게 전달 받음
    db: Database = Depends(get_db_conn)
    ):
    
    query = memo.insert()				# insert 쿼리 생성
    values = req
    
    await db.execute(query, values)		# 쿼리 실행
    
    return {**req.dict()}
    #return {**req.__dict__}

"""
# select
@memo_router.get("/sensor/find/{rfid}", response_model=Select)
async def findone(
    rfid : str,
    db: Database = Depends(get_db_conn)
):
    query = sensor.select().where(sensor.columns.rfid == rfid)
    return await db.fetch_one(query)

@memo_router.get("/sensor/list/{page}", response_model=List[Select])
async def list(
    page: int = 1,
    limit: int = 10,
    db: Database = Depends(get_db_conn)
):
    offset = (page-1)*limit
    query = sensor.select().offset(offset).limit(limit)
    return await db.fetch_all(query)

@memo_router.delete("/sensor/{idx}")
async def delete(
    idx: int,
    db: Database = Depends(get_db_conn)
):
    query = sensor.delete().where(sensor.columns.idx == idx)
    await db.execute(query)
    return {"result": "success"}
"""