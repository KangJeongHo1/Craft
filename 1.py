import pandas as pd

# 파일 경로
file_path = '/Users/kang/Desktop/sample/시세/2.log'

# 로그 데이터를 텍스트 파일에서 읽어오는 함수
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()  # 각 줄을 리스트로 반환

# A301F 로그 데이터를 파싱하는 함수
def parse_A301F(log_data):
    parsed_data = []
    for row in log_data:
        if row.strip() and row.startswith('A301F'):
            processing_time = row[35:47].strip()
            price = float(row[47:56].strip())
            volume = float(row[56:65].strip())
            parsed_data.append([processing_time, price, volume])
    return parsed_data

# 데이터 처리
log_data = read_log_file(file_path)

# A301F 데이터 파싱
a301f_data = parse_A301F(log_data)

# 특정 시간 범위 필터링
start_time_str = '10:00:00'
end_time_str = '14:00:00'

filtered_a301f = []

for row in a301f_data:
    processing_time_str = row[0].strip()
    if start_time_str <= processing_time_str <= end_time_str:
        filtered_a301f.append(row)

# VWAP 계산 함수
def calculate_vwap(filtered_a301f):
    total_trade_value = 0
    total_trade_volume = 0
    
    for row in filtered_a301f:
        price = row[1]
        volume = row[2]
        total_trade_value += price * volume
        total_trade_volume += volume

    # VWAP 계산
    if total_trade_volume > 0:
        vwap = total_trade_value / total_trade_volume
    else:
        vwap = 0

    return vwap

# VWAP 계산
vwap = calculate_vwap(filtered_a301f)
print(f"VWAP (10시~14시): {vwap:.2f}")
