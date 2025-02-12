from sqlalchemy import Column, Integer, String, Numeric, BigInteger 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SmaEmaTechnicalIndicatorsTable(Base):
    __tablename__ = "SmaEmaTechnicalIndicators"
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Symbol = Column(String(10), nullable=False)
    CloseTime = Column(BigInteger, nullable=False)
    Sma5 = Column(Numeric(18,8), nullable=False)
    Sma10 = Column(Numeric(18,8), nullable=False)
    Sma20 = Column(Numeric(18,8), nullable=False)
    Sma50 = Column(Numeric(18,8), nullable=False)
    Sma100 = Column(Numeric(18,8), nullable=False)
    Sma200 = Column(Numeric(18,8), nullable=False)
    Ema5 = Column(Numeric(18,8), nullable=False)
    Ema9 = Column(Numeric(18,8), nullable=False)
    Ema12 = Column(Numeric(18,8), nullable=False)
    Ema50 = Column(Numeric(18,8), nullable=False)
    Ema100 = Column(Numeric(18,8), nullable=False)
    Ema200 = Column(Numeric(18,8), nullable=False)