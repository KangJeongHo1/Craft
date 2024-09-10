import pandas as pd
from datetime import datetime

# 파일 경로
file_path = '/Users/kang/Desktop/sample/시세/2.log'

# 로그 데이터를 텍스트 파일에서 읽어오는 함수
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()  # 각 줄을 리스트로 반환

# B601F 로그 데이터를 파싱하는 함수
def parse_B601F(log_data):
    parsed_data = []
    for row in log_data:
        if row.strip() and row.startswith('B601F'):
            processing_time = row[35:47].strip()
            ask_prices = [float(row[47:56].strip()), float(row[93:102].strip()), float(row[139:148].strip()), float(row[185:194].strip()), float(row[231:240].strip())]
            bid_prices = [float(row[56:65].strip()), float(row[102:111].strip()), float(row[148:157].strip()), float(row[194:203].strip()), float(row[240:249].strip())]
            ask_volumes = [float(row[65:74].strip()), float(row[111:120].strip()), float(row[157:166].strip()), float(row[203:212].strip()), float(row[249:258].strip())]
            bid_volumes = [float(row[74:83].strip()), float(row[120:129].strip()), float(row[166:175].strip()), float(row[212:221].strip()), float(row[258:267].strip())]
            parsed_data.append([processing_time, ask_prices, bid_prices, ask_volumes, bid_volumes])
    return parsed_data

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

# B601F 데이터 파싱
b601f_data = parse_B601F(log_data)

# A301F 데이터 파싱
a301f_data = parse_A301F(log_data)

# 특정 시간 범위 필터링
start_time_str = '09:30:00'
end_time_str = '10:00:00'

filtered_b601f = []
filtered_a301f = []

for row in b601f_data:
    processing_time_str = row[0].strip()
    if start_time_str <= processing_time_str <= end_time_str:
        filtered_b601f.append(row)

for row in a301f_data:
    processing_time_str = row[0].strip()
    if start_time_str <= processing_time_str <= end_time_str:
        filtered_a301f.append(row)

# 취소 수량 계산 함수
def calculate_cancellations(b601f_row, a301f_data):
    processing_time = b601f_row[0]
    ask_prices = b601f_row[1]
    bid_prices = b601f_row[2]
    ask_volumes = b601f_row[3]
    bid_volumes = b601f_row[4]

    total_trade_volume = [0] * 5
    cancellation_volume = [0] * 5

    used_a301f_rows = set()  # 이미 사용된 A301F 행을 추적 (튜플로 변환)

    for i in range(5):
        if ask_prices[i] > bid_prices[i]:  # 하락장
            for a301f_row in a301f_data:
                price = a301f_row[1]
                volume = a301f_row[2]

                if price == bid_prices[i] and tuple(a301f_row) not in used_a301f_rows:  # 체결가가 매수 가격과 동일
                    total_trade_volume[i] += volume
                    used_a301f_rows.add(tuple(a301f_row))  # 튜플로 변환하여 추가

            cancellation_volume[i] = ask_volumes[i] - total_trade_volume[i]

        elif bid_prices[i] > ask_prices[i]:  # 상승장
            for a301f_row in a301f_data:
                price = a301f_row[1]
                volume = a301f_row[2]

                if price == ask_prices[i] and tuple(a301f_row) not in used_a301f_rows:  # 체결가가 매도 가격과 동일
                    total_trade_volume[i] += volume
                    used_a301f_rows.add(tuple(a301f_row))  # 튜플로 변환하여 추가

            cancellation_volume[i] = bid_volumes[i] - total_trade_volume[i]

    # 취소 수량이 음수가 될 수 없으므로 0으로 설정
    cancellation_volume = [max(vol, 0) for vol in cancellation_volume]
    return cancellation_volume

# 전체 취소 수량을 누적 계산
total_cancellation_volume = [0] * 5

for b601f_row in filtered_b601f:
    relevant_a301f_data = [row for row in filtered_a301f if row[0] > b601f_row[0]]  # B601F 이후 A301F 데이터 선택
    cancellation_volumes = calculate_cancellations(b601f_row, relevant_a301f_data)
    total_cancellation_volume = [total + cancellation for total, cancellation in zip(total_cancellation_volume, cancellation_volumes)]

# 최종 결과 출력
for i in range(5):
    print(f"{i+1}호가 총 취소된 주문 수량: {total_cancellation_volume[i]}")
