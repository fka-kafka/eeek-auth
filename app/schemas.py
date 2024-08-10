from datetime import UTC, datetime
from pydantic import UUID4, BaseModel, EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserSignup(BaseModel):
    firstname: str
    lastname: str
    username: str
    email: EmailStr
    password: str

class UserSchema(BaseModel):
    id: UUID4
    firstname: str
    lastname: str
    username: str
    email: EmailStr
    hashed_pwd: str
    date_created: datetime

    class Config:
        from_attributes = True

class UserCreated(BaseModel):
    id: UUID4
    username: str
    date_created: datetime

    class Config:
        from_attributes = True
