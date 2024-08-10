from pydantic import EmailStr
from sqlalchemy import TIMESTAMP, Column, String, Uuid, text, true
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column('user_id', Uuid, primary_key=True, nullable=False,  server_default=text('uuid_generate_v4()'))
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column('user_email',String, nullable=False)
    password = Column('hashed_pwd',String, nullable=False)
    date_created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
