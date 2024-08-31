from sqlalchemy.orm import Session
from models import DataField  # 모델을 임포트

def get_data_fields(db: Session):
    return db.query(DataField).all()
