from sqlalchemy.orm import Session  # type: ignore

from . import models
from . import schemas


def get_crypto(db: Session, crypto_id: int):
    return db.query(models.Crypto).filter(models.Crypto.id == crypto_id).first()


def get_crypto_by_name(db: Session, name: str):
    return db.query(models.Crypto).filter(models.Crypto.name == name).first()


def get_cryptos(db: Session):
    return db.query(models.Crypto).all()


def create_crypto(db: Session, crypto: schemas.CryptoCreate):
    db_crypto = models.Crypto(
        name=crypto.name, symbol=crypto.symbol, base=crypto.base)
    db.add(db_crypto)
    db.commit()
    db.refresh(db_crypto)
    return db_crypto


def get_klines(db: Session, crypto_id: int):
    return db.query(models.Kline).filter(models.Kline.crypto_id == crypto_id).all()


def create_kline(db: Session, kline: schemas.KlineCreate, crypto_id: int):
    db_kline = models.Kline(**kline.dict(), crypto_id=crypto_id)
    db.add(db_kline)
    db.commit()
    db.refresh(db_kline)
    return db_kline
