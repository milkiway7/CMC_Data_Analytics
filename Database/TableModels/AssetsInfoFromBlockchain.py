from sqlalchemy import Column, Integer, String, Numeric, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AssetsInfoFromBlockchain(Base):

    __tablename__ = "BlockchainAssetsInfo"

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Symbol = Column(String(10), nullable=False)
    Time = Column(BigInteger, nullable=False)
    Price = Column(Numeric(35,8), nullable=False)
    OneHourPriceChangePercent = Column(Numeric(35,8), nullable=False)
    OneWeekPriceChangePercent = Column(Numeric(35,8), nullable=False)
    OneDayPriceChangePercent = Column(Numeric(35,8), nullable=False)
    OneDayTradingVolume = Column(Numeric(35,8), nullable=False)
    CirculationSupply = Column(Numeric(35,8), nullable=False)
    MarketCap = Column(Numeric(35,8), nullable=False)
    MaxSupply = Column(Numeric(35,8), nullable=False)