from datetime import datetime
from typing import List
from pydantic import BaseModel  # type: ignore


class CryptoBase(BaseModel):
    id: int
    name: str
    symbol: str


class CryptoCreate(CryptoBase):
    pass


class Crypto(CryptoBase):
    id: int
    klines: List["Kline"] = []

    class Config:
        from_attribute = True


class KlineBase(BaseModel):
    open_time: datetime
    open_price: float
    open_price_dateTime: datetime
    high_price: float
    low_price: float
    close_price: float
    volume: str
    close_time: datetime
    close_price_dateTime: datetime
    quote_asset_volume: str
    number_of_trades: int
    taker_buy_base_asset_volume: str
    taker_buy_quote_asset_volume: str
    pourcent: float


class KlineCreate(KlineBase):
    crypto_id: int


class Kline(KlineBase):
    id: int
    crypto_id: int

    class Config:
        from_attribute = True
