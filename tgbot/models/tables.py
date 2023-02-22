from sqlalchemy import (
    Column,
    VARCHAR,
    String,
    Integer,
    Float,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Sharik_trouble(Base):
    __tablename__ = 'Sharik_trouble'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False) # autoincrement always gets true or false
    debt = Column(Integer, nullable=False)
    date = Column(VARCHAR, nullable=False, unique=True)