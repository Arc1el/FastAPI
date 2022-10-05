from sqlalchemy import Column, TEXT, INT, BIGINT, FLOAT, VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Sensor(Base):
    __tablename__ = "sensor"
    rfid = Column(VARCHAR, nullable=False)
    temp = Column(FLOAT, nullable=False)
    breath =  Column(INT, nullable=False)
    time = Column(VARCHAR, nullable=False)