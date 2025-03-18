from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base 

Base = declarative_base()

class CryptoPanicTable(Base):
    __tablename__ = "CryptoPanic"


    Id = Column(Integer, primary_key=True, autoincrement=True)  # unikalny identyfikator
    MessageId = Column(Integer, nullable=False)
    Title = Column(String(500), nullable=False)  # Tytuł wiadomości
    VotesPositive = Column(Integer, default=0)  # Liczba pozytywnych głosów
    VotesNegative = Column(Integer, default=0)  # Liczba negatywnych głosów
    VotesImportant = Column(Integer, default=0)  # Liczba głosów "ważnych"
    PublishedAt = Column(BigInteger, nullable=False)  # Czas publikacji wiadomości
    Url = Column(String(1000), nullable=False)  # URL wiadomości
    Currencies = Column(String(500), nullable=True)  # Lista kryptowalut związanych z wiadomością (np. BTC, ETH)
    Sentiment = Column(String(20), nullable=True)  # Sentiment wiadomości (bullish, bearish, unclassified)
