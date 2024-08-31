# app/models/data_field.py

from sqlalchemy import Column, Integer, String
from app.db.database import Base

class DataField(Base):
    __tablename__ = "data_fields"
    
    interface_id = Column(String, primary_key=True, index=True)
    interface_name = Column(String)
    tr_name = Column(String)
    sequence_number = Column(Integer)
    field_name = Column(String)
    item_name = Column(String)
    decimal_places = Column(Integer)
    data_type = Column(String)
    length = Column(Integer)
    cumulative_length = Column(Integer)
    definition = Column(String)
    remarks = Column(String, nullable=True)
