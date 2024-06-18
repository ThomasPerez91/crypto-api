from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric, TIMESTAMP # type: ignore
from sqlalchemy.orm import relationship # type: ignore

from config.database import Base


class Crypto(Base):
    __tablename__ = "cryptos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    symbol = Column(String, unique=True, index=True)

    klines = relationship("Kline", back_populates="crypto")


class Kline(Base):
    __tablename__ = "klines"

    id = Column(Integer, primary_key=True, index=True)
    crypto_id = Column(Integer, ForeignKey("cryptos.id"))
    open_time = Column(TIMESTAMP)
    open_price = Column(Numeric(12, 6))
    open_price_dateTime = Column(DateTime)
    high_price = Column(Numeric(12, 6))
    low_price = Column(Numeric(12, 6))
    close_price = Column(Numeric(12, 6))
    volume = Column(String)
    close_time = Column(TIMESTAMP)
    close_price_dateTime = Column(DateTime)
    quote_asset_volume = Column(String)
    number_of_trades = Column(Integer)
    taker_buy_base_asset_volume = Column(String)
    taker_buy_quote_asset_volume = Column(String)
    pourcent = Column(Numeric(12, 6))

    crypto = relationship("Crypto", back_populates="klines")
