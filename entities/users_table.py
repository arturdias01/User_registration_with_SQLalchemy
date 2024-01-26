from configs.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
