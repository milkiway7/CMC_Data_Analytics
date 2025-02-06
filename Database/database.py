from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_CONFIG

class Database:
    def __init__(self):
        self.engine = create_engine(
            f"mssql+pyodbc://{DATABASE_CONFIG['server']}/{DATABASE_CONFIG['database']}?driver={DATABASE_CONFIG['driver']}&trusted_connection=yes",
            fast_executemany=True
        )
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    def get_session(self):
        return self.SessionLocal()
