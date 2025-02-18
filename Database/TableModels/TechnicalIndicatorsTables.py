from sqlalchemy import Column, Integer, String, Numeric, BigInteger 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TechnicalIndicatorsHourly(Base):
    __tablename__ = "TechnicalIndicatorsHourly"
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Symbol = Column(String(10), nullable=False)
    CloseTime = Column(BigInteger, nullable=False)
    Sma5 = Column(Numeric(18,8), nullable=False)
    Sma10 = Column(Numeric(18,8), nullable=False)
    Sma20 = Column(Numeric(18,8), nullable=False)
    Ema5 = Column(Numeric(18,8), nullable=False)
    Ema9 = Column(Numeric(18,8), nullable=False)
    Ema12 = Column(Numeric(18,8), nullable=False)
    
class TechnicalIndicatorsFourHours(Base):
    __tablename__ = "TechnicalIndicatorsFourHours"
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Symbol = Column(String(10), nullable=False)
    CloseTime = Column(BigInteger, nullable=False)
    Sma50 = Column(Numeric(18,8), nullable=False)
    Sma100 = Column(Numeric(18,8), nullable=False)
    Ema26 = Column(Numeric(18,8), nullable=False)
    Ema100 = Column(Numeric(18,8), nullable=False)

class TechnicalIndicatorsDaily(Base):
    __tablename__ = "TechnicalIndicatorsDaily"
    
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Symbol = Column(String(10), nullable=False)
    CloseTime = Column(BigInteger, nullable=False)
    Sma200 = Column(Numeric(18,8), nullable=False)
    Ema200 = Column(Numeric(18,8), nullable=False)
    Rsi = Column(Numeric(18,2), nullable=False)
    Macd = Column(Numeric(18,2), nullable=False)