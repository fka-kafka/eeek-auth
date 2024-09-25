from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app import models
from app.database import engine
from app.routers import auth_login, auth_signup, auth_reset
from app.services.cache_service import app0
from app.config import get_settings

models.Base.metadata.create_all(bind=engine)
settings = get_settings()

app = FastAPI(
    title='EEEK-Auth'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
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
