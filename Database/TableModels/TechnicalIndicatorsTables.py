from sqlalchemy import Column, Integer, String, Numeric, BigInteger 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TechnicalIndicators(Base):
    __tablename__ = "TechnicalIndicators"
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Symbol = Column(String(10), nullable=False)
    CloseTime = Column(BigInteger, nullable=False)
    Indicator = Column(String(10), nullable=False)
    Interval = Column(String(10), nullable=False)
    Value = Column(Numeric(18,8), nullable=False)

    