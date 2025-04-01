from sqlalchemy import Column, Integer, String, Numeric, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BlocksInfoTable(Base):

    __tablename__ = "BlocksInfo"

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Symbol = Column(String(10), nullable= False)
    Time = Column(BigInteger, nullable=False)
    BlockCount = Column(Integer, nullable=False)
    Difficulty = Column(Numeric, nullable=False)
    Size = Column(Numeric, nullable=False)
    Weight = Column(Numeric, nullable=False)
    TransactionsCount = Column(Integer, nullable=False)         
