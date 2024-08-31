# app/schemas/data_field.py

from pydantic import BaseModel
from typing import Optional

class DataField(BaseModel):
    interface_id: str  # Interface ID
    interface_name: str  # Interface Name
    tr_name: str  # TR Name
    sequence_number: int  # Sequence Number
    field_name: str  # Field Name
    item_name: str  # Item Name
    decimal_places: int  # Decimal Places
    data_type: str  # Data Type
    length: int  # Length
    cumulative_length: int  # Cumulative Length
    definition: str  # Definition
    remarks: Optional[str] = None  # Remarks (Optional)
