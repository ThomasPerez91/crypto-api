from fastapi import HTTPException  # type: ignore
from sqlalchemy.orm import Session  # type: ignore
from database import crud, schemas, redis_queries


def create_crypto_service(crypto: schemas.CryptoCreate, db: Session):
    db_crypto = crud.get_crypto_by_name(db=db, name=crypto.name)
    if db_crypto:
        raise HTTPException(
            status_code=400, detail="Crypto already registered")
    created_crypto = crud.create_crypto(db=db, crypto=crypto)
    update_redis_with_all_cryptos_from_db(db)
    return created_crypto


def update_redis_with_all_cryptos_from_db(db: Session):
    cryptos = crud.get_cryptos(db=db)
    crypto_list = [{"id": crypto.id, "name": crypto.name, "symbol": crypto.symbol, "base": crypto.base}
                   for crypto in cryptos]
    redis_queries.update_redis_with_all_cryptos(crypto_list)
