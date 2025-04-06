from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    car_number = Column(String, nullable=True)
    password = Column(String, nullable=False)
    is_password_changed = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
