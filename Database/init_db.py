from Database.database import Database
from Database.TableModels.CandlesHistoricalData import CandlesHistoricalData

def initialize_database():
    db = Database()
    CandlesHistoricalData.metadata.create_all(db.engine)
    print("Database initialized")