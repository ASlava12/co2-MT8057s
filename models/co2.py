from sqlalchemy import Integer, Float, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from config import engine

Base = declarative_base()

class Co2(Base):
    __tablename__ = 'co2_metrics'
    id = Column(Integer, primary_key=True)   
    created_on = Column(DateTime(), default=datetime.now)
    temp = Column(Float)
    co2 = Column(Float)

Base.metadata.create_all(engine)