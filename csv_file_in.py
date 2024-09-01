import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.models.data_fields import HeaderDataType 

# 데이터베이스 연결 설정
DB_URL = 'postgresql+psycopg2://postgres:tmvlzj12@localhost/craft'
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Enum 변환 함수
def convert_header_data_type(value):
    try:
        return HeaderDataType[value]
    except KeyError:
        return None

# CSV 파일을 읽는 함수
def read_csv(file_path):
    return pd.read_csv(file_path)

# 열 이름 매핑 정의
COLUMN_MAPPING = {
    '업무구분': 'business_type',
    'TR-CODE': 'tr_code',
    '인터페이스명': 'interface_name',
    'HEADER/DATA 구분': 'header_data_type',
    '순번': 'sequence_number',
    '항목명': 'item_name',
    '항목영문명': 'item_name_en',
    'Data Type': 'data_type',
    '길이': 'length',
    '필수 여부': 'is_required',
    '정의': 'definition'
}
# COLUMN_MAPPING = {
#     '인터페이스ID': 'interface_id',
#     '인터페이스명': 'interface_name',
#     'TR Name': 'tr_name',
#     '순번': 'sequence_number',
#     '항목명': 'item_name',
#     'Item Name': 'item_name_en',
#     '소수점 이하 자릿수': 'decimal_places',
#     'Data Type': 'data_type',
#     '길이': 'length',
#     '누적 길이': 'cumulative_length',
#     '정의': 'definition',
#     'Remarks': 'remarks'
# }
# 데이터 삽입 함수
def insert_data():
    csv_file_path = '/Users/kang/Desktop/sample/ac.csv'

    # 데이터를 읽어들입니다.
    data = read_csv(csv_file_path)

    # 열 이름 변경
    data.rename(columns=COLUMN_MAPPING, inplace=True)

    # Enum 변환
    data['header_data_type'] = data['header_data_type'].apply(convert_header_data_type)

    # 데이터베이스에 데이터 삽입
    data.to_sql('derivative_execution_detail', con=engine, if_exists='append', index=False)

# main 함수
if __name__ == "__main__":
    insert_data()
    print("데이터가 성공적으로 삽입되었습니다!")
