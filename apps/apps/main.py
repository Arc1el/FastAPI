from fastapi import FastAPI, Request
from apps.database import db_instance
from apps.data.router import memo_router


app = FastAPI(
    title="test API",
    description="CRUD API project",
    version="0.0.1"
)

# db connect on server start
@app.on_event("startup")
async def startup():
    await db_instance.connect()

# db disconnect on server stop
@app.on_event("shutdown")
async def shutdown():
    await db_instance.disconnect()

# fastapi middleware, request state 에 db connection 심기
@app.middleware("http")
async def state_insert(request: Request, call_next):
    request.state.db_conn = db_instance
    response = await call_next(request)
    return response

app.include_router(memo_router)
