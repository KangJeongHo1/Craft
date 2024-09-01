from sqlalchemy import Column, Integer, String, Float, Text, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DerivativeTrade(Base):
    __tablename__ = 'derivative_trades'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)  # 고유 ID
    interface_id = Column(String(50), nullable=False)  # 인터페이스 ID
    interface_name = Column(String(50), nullable=False)  # 인터페이스명
    tr_name = Column(String(50), nullable=False)  # TR Name
    sequence_number = Column(Integer, nullable=False)  # 순번
    item_name = Column(String(50), nullable=False)  # 항목명
    item_name_en = Column(String(50), nullable=False)  # Item Name
    decimal_places = Column(Integer, nullable=False)  # 소수점 이하 자릿수
    data_type = Column(String(50), nullable=False)  # Data Type
    length = Column(Integer, nullable=False)  # 길이
    cumulative_length = Column(Integer, nullable=False)  # 누적 길이
    definition = Column(Text, nullable=True)  # 정의
    remarks = Column(Text, nullable=True)  # Remarks

class DerivativeExecution(Base):
    __tablename__ = 'derivative_execution'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)  # 고유 ID
    interface_id = Column(String(50), nullable=False)  # 인터페이스 ID
    interface_name = Column(String(50), nullable=False)  # 인터페이스명
    tr_name = Column(String(50), nullable=False)  # TR Name
    sequence_number = Column(Integer, nullable=False)  # 순번
    item_name = Column(String(50), nullable=False)  # 항목명
    item_name_en = Column(String(50), nullable=False)  # Item Name
    decimal_places = Column(Integer, nullable=False)  # 소수점 이하 자릿수
    data_type = Column(String(50), nullable=False)  # Data Type
    length = Column(Integer, nullable=False)  # 길이
    cumulative_length = Column(Integer, nullable=False)  # 누적 길이
    definition = Column(Text, nullable=True)  # 정의
    remarks = Column(Text, nullable=True)  # Remarks


from enum import Enum as PyEnum

class HeaderDataType(PyEnum):
    HEADER = 'HEADER'
    DATA = 'DATA'

class DerivativeExecutionDetail(Base):
    __tablename__ = 'derivative_execution_details'  # 새 테이블 이름

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)  # Unique ID
    business_type = Column(String(20), nullable=False)  # Business Type
    tr_code = Column(String(20), nullable=False)  # TR Code
    interface_name = Column(String(100), nullable=False)  # Interface Name
    header_data_type = Column(Enum(HeaderDataType), nullable=False)  # HEADER/DATA Type
    sequence_number = Column(Integer, nullable=False)  # Sequence Number
    item_name = Column(String(50), nullable=False)  # Item Name
    item_name_en = Column(String(50), nullable=False)  # Item Name (English)
    data_type = Column(String(20), nullable=False)  # Data Type
    length = Column(Integer, nullable=False)  # Length
    is_required = Column(String(5), nullable=False)  # Required (Yes/No)
    definition = Column(Text, nullable=True)  # Definition
