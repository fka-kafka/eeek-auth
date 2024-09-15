from datetime import datetime
from pydantic import UUID4, BaseModel, EmailStr

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
    password: str
    date_created: datetime

    class Config:
        from_attributes = True

class UserCreated(BaseModel):
    id: UUID4
    username: str
    date_created: datetime

    class Config:
        from_attributes = True
        
class Token(BaseModel):
    access_token: str
    token_type: str

class PayloadSchema(BaseModel):
    content: str | int