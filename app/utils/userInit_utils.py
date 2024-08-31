import redis
import json
import fastapi
from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import models, schemas
from app.config import get_settings
from app.database import get_db

initializer = FastAPI()

origins = [
    'http://localhost:5173'
]

initializer.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"],
)

settings = get_settings()

cache = redis.Redis(host=settings.redis_host, port=settings.redis_port,
                    password=settings.redis_password, decode_responses=True)


@initializer.get('/init/', status_code=status.HTTP_200_OK)
def init(db: Session = Depends(get_db)):
    names = list()
    usernames = db.query(models.User.username).all()
    for (name,) in usernames:
        names.append(name)

    encoded_names = (json.dumps(names)).encode('utf-8')
    cache.set('usernames', encoded_names)

    return {'Initialized'}


@initializer.post('/init/get_names/', status_code=status.HTTP_200_OK)
def get_init(payload: schemas.PayloadSchema):
    names = cache.get('usernames')
    decoded_names = json.loads(names)
    name_set = set(decoded_names)
    return {'found': True} if payload.username in name_set else {'found': False}
    
    # if user_payload.username not in name_set:
    #     return {'Found': False}
    # print(decoded_names)

    # return {'Found': True}
