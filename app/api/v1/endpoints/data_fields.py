from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from services.data_field_service import get_data_fields

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/data_fields/")
def read_data_fields(db: Session = Depends(get_db)):
    return get_data_fields(db)
