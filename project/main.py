from config.database import SessionLocal, engine
import database.crud as crud
import database.schemas as schemas
import database.models as models
from fastapi import FastAPI, Depends, HTTPException  # type: ignore
from sqlalchemy.orm import Session  # type: ignore
from config.celery import pouet


models.Base.metadata.create_all(bind=engine)

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
    return crud.create_crypto(db=db, crypto=crypto)

# Endpoint pour déclencher la tâche Celery


@app.post("/trigger-task/")
async def trigger_task(a: int, b: int):
    result = pouet.delay(a, b)  # Déclenche la tâche de manière asynchrone
    return {"message": f"Tâche démarrée avec ID {result.id}"}
