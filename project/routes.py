from fastapi import APIRouter, Depends  # type: ignore
from config.database import SessionLocal
from sqlalchemy.orm import Session  # type: ignore
from database import schemas
from services.crypto_service import create_crypto_service
from services.task_service import trigger_task_service

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/crypto", response_model=schemas.Crypto)
def create_crypto(crypto: schemas.CryptoCreate, db: Session = Depends(get_db)):
    return create_crypto_service(crypto, db)


@router.post("/trigger-task/")
async def trigger_task(a: int, b: int):
    return trigger_task_service(a, b)
