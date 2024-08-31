from fastapi import FastAPI

from app import models
from app.database import engine
from app.routers import auth_login, auth_signup
from app.utils.userInit_utils import initializer
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='EEEK-Auth'
)


origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"],
)

app.mount('/utils/initializer', initializer, name='initializer')


@app.get('/')
def homepage():
    return {'Hi.'}


app.include_router(auth_login.router)
app.include_router(auth_signup.router)
