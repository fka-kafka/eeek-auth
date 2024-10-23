from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


import models
from database import engine
from routers import auth_login, auth_signup, auth_reset
from services.cache_service import app0
from config import get_settings

models.Base.metadata.create_all(bind=engine)
settings = get_settings()

app = FastAPI(
    title='EEEK-Auth'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_url,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/utils/initializer', app0, name='initializer')


@app.get('/')
def homepage():
    return {'Hi.'}


app.include_router(auth_login.router)
app.include_router(auth_signup.router)
app.include_router(auth_reset.router)
