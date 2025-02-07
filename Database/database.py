
from config import DATABASE_CONFIG
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self):
        # Zmieniamy 'pyodbc' na 'aioodbc'
        self.engine = create_async_engine(
            f"mssql+aioodbc://{DATABASE_CONFIG['server']}/{DATABASE_CONFIG['database']}?driver={DATABASE_CONFIG['driver']}&trusted_connection=yes",
            echo=True,  # Możesz ustawić na True do debugowania
            fast_executemany=True
        )
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,  # Używamy AsyncSession zamiast zwykłej Session
            expire_on_commit=False
        )

    def get_session(self):
        return self.SessionLocal()  # Zwracamy sesję AsyncSession
