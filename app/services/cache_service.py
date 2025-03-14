import redis
import json
from typing import List
from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware


import models
import schemas
from config import get_settings
from redis_db import get_redis
from utils.connection_utils import get_connections

app0 = FastAPI()

settings = get_settings()

app0.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=False,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app0.get('/init/', status_code=status.HTTP_200_OK)
def init(connections: tuple = Depends(get_connections)):
    try:
        db, cache = connections
        usernames: List[str] = [
            name for (name,) in db.query(models.User.username).all()]
        cache.set('usernames', json.dumps(usernames))
        return {"status": "initialization successful"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Initialization failed: {str(e)}")


@app0.post('/check_username/', status_code=status.HTTP_200_OK)
async def check_username(payload: schemas.PayloadSchema, redis_conn: redis.Redis = Depends(get_redis)):
    try:
        names = redis_conn.get('usernames')
        if names is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usernames not initialized")
        decoded_names = json.loads(names)
        return {'found': payload.content in decoded_names}
    except redis.RedisError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Redis error: {str(e)}")
    except json.JSONDecodeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"JSON decode error: {str(e)}")
