from config.database import SessionLocal
import database.crud as crud
import database.schemas as schemas
from database.redis_queries import update_redis_with_all_cryptos
from fastapi import FastAPI, Depends, HTTPException  # type: ignore
from sqlalchemy.orm import Session  # type: ignore
from tasks.test import pouet
from celery.result import AsyncResult  # type: ignore


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def read_root():
    return {"message": "Hello World"}


@app.post("/crypto", response_model=schemas.Crypto)
def create_crypto(crypto: schemas.CryptoCreate, db: Session = Depends(get_db)):
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
    update_redis_with_all_cryptos(crypto_list)


# Endpoint pour déclencher la tâche Celery
@app.post("/trigger-task/")
async def trigger_task(a: int, b: int):
    result = pouet.delay(a, b)  # Déclenche la tâche de manière asynchrone
    return {"message": f"Tâche démarrée avec ID {result.id}"}
