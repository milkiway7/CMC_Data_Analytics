from sqlalchemy.future import select
from Database.database import Database
from Database.TableModels.CandlesHistoricalData import Candles
from Database.TableModels.TechnicalIndicatorsTables import TechnicalIndicators
from Database.TableModels.CryptoPanicTable import CryptoPanicTable
from Database.TableModels.AssetsInfoFromBlockchain import AssetsInfoFromBlockchain
from Database.TableModels.BlocksInfoTable import BlocksInfoTable
import logging
from decimal import ROUND_HALF_UP, Decimal

db = Database()

async def save_block_info(data):
    async with db.get_session() as session:
        try:
            record = BlocksInfoTable(
                Symbol=data['data']['context'],
                Time=data['data']['items'][''],
                BlockCount=data['block_count'],
                Difficulty=Decimal(data['difficulty']).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP),
                Size=Decimal(data['size']).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP),
                Weight=Decimal(data['weight']).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP),
                TransactionsCount=data['transactions_count']
            )
        except Exception as e:
            logging.info(f"Database write error: {e}")
            await session.rollback()

async def save_assets_info(data):
    async with db.get_session() as session:
        try:
            record = AssetsInfoFromBlockchain(
                Symbol=data['data']['item']['originalSymbol'],
                Time=int(data['data']['item']['latestRate']['calculationTimestamp']),
                Price=Decimal(data['data']['item']['latestRate']['amount']).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP),
                OneHourPriceChangePercent=Decimal(data['data']['item']['specificData']['1HourPriceChangeInPercentage']).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP),
                OneWeekPriceChangePercent=Decimal(data['data']['item']['specificData']['1WeekPriceChangeInPercentage']).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP),
                OneDayPriceChangePercent=Decimal(data['data']['item']['specificData']['24HoursPriceChangeInPercentage']).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP),
                OneDayTradingVolume=Decimal(data['data']['item']['specificData']['24HoursTradingVolume']).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP),
                CirculationSupply=Decimal(data['data']['item']['specificData']['circulatingSupply']).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP),
                MarketCap=Decimal(data['data']['item']['specificData']['marketCapInUSD']).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP),
                MaxSupply=Decimal(data['data']['item']['specificData']['maxSupply']).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP)
            )
            session.add(record)
            await session.commit()
        except Exception as e:
            logging.info(f"Database write error: {e}")
            await session.rollback()

async def get_lastes_candle(symbol,interval):
    async with db.get_session() as session:
        stmt = (
            select(Candles)
            .where(Candles.Symbol == symbol, Candles.Interval == interval)
            .order_by(Candles.CloseTime.desc())
            .limit(1)
        )
        result = await session.execute(stmt)
        last_candle = result.scalars().first()

        return last_candle

async def save_crypto_panic(data):
    try:
        batch_size = 20
        async with db.get_session() as session:

            info_ids = {str(record["MessageId"]) for record in data}  # Używamy set() zamiast listy, żeby uniknąć duplikatów

            if not info_ids:
                return 
            
            result = await session.execute(select(CryptoPanicTable.MessageId).filter(CryptoPanicTable.MessageId.in_(info_ids)))
            existing_info_ids = {row[0] for row in result.fetchall()}  # Zbieramy istniejące MessageId do setu

            # Filtruj dane, aby zostawić tylko te, które nie są duplikatami
            unique_data = [record for record in data if record["MessageId"] not in existing_info_ids]

            # Jeśli mamy jakieś unikalne dane, zapisz je w bazie

            if unique_data:
                for i in range(0, len(unique_data), batch_size):
                    batch = unique_data[i:i + batch_size]
                    session.add_all([CryptoPanicTable(**record) for record in batch])
                    await session.commit()

    except Exception as e:
        logging.info(f"DATABASE ERROR: saving crypto panic data {e}")

async def save_candles_to_db(candles_data):
    try:
        batch_size = 100  # Możesz dostosować rozmiar partii
        async with db.get_session() as session:
            for i in range(0, len(candles_data), batch_size):
                batch = candles_data[i:i + batch_size]
                session.add_all([Candles(**candle) for candle in batch])
                await session.commit()
    except Exception as e:
        logging.info(f"DATABASE ERROR: saving candle data {e}")
        await session.rollback()
            
async def save_technical_indicators(technical_analysis_data):
    async with db.get_session() as session:
        try:
            for data in technical_analysis_data:
                record = TechnicalIndicators(
                    Symbol=data["symbol"],
                    CloseTime=data["close_time"],
                    Indicator=data["indicator"],
                    Interval=data["interval"],
                    Value=data["value"]
                )
                session.add(record)
            await session.commit()
        except Exception as e:
            logging.info(f"Database write error: {e}")
            await session.rollback()
