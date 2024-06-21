from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, TIMESTAMP  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore

from config.database import Base


class Crypto(Base):
    __tablename__ = "cryptos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    symbol = Column(String(10), index=True)
    base = Column(String(10))

    klines1m = relationship("Kline1m", back_populates="crypto",
                            cascade='save-update, merge, delete, delete-orphan', passive_deletes=True)


class Kline1m(Base):
    __tablename__ = "klines1m"

    id = Column(Integer, primary_key=True, index=True)
    crypto_id = Column(Integer, ForeignKey("cryptos.id"), index=True)
    open_time = Column(TIMESTAMP)
    open_dateTime = Column(DateTime)
    open_price = Column(String(100))
    high_price = Column(String(100))
    low_price = Column(String(100))
    close_price = Column(String(100))
    volume = Column(String)
    close_time = Column(TIMESTAMP)
    close_price_dateTime = Column(DateTime)
    quote_asset_volume = Column(String)
    number_of_trades = Column(Integer)
    taker_buy_base_asset_volume = Column(String)
    taker_buy_quote_asset_volume = Column(String)
    pourcent = Column(Float)

    crypto = relationship("Crypto", back_populates="klines1m")
