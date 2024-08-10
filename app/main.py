from fastapi import FastAPI
from app.routers import auth_login, auth_signup
from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def get_root(): 
    return {'Hi.'} 

app.include_router(auth_login.router)
app.include_router(auth_signup.router)
