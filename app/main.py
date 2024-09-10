from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
from datetime import datetime

app = FastAPI()

# 파일 경로
file_path = '/Users/kang/Desktop/CRAFT/app/data/summarize.log'

# 로그 데이터를 텍스트 파일에서 읽어오는 함수
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# A301F 로그 데이터를 파싱하는 함수
def parse_A301F(log_data):
    parsed_data = []
    for row in log_data:
        if row.strip() and row.startswith('A301F'):
            processing_time = row[35:47].strip()
            price = float(row[47:56].strip())
            volume = float(row[56:65].strip())
            
            # HHMMSSuuuuuu 형식의 시간을 datetime 객체로 변환
            processing_time_dt = datetime.strptime(processing_time, '%H%M%S%f')
            parsed_data.append([processing_time_dt, price, volume])
    return parsed_data

# VWAP 계산 함수
def calculate_vwap(filtered_a301f):
    df = pd.DataFrame(filtered_a301f, columns=['time', 'price', 'volume'])
    df.set_index('time', inplace=True)
    
    # VWAP 계산
    df['trade_value'] = df['price'] * df['volume']
    df['cumulative_trade_value'] = df['trade_value'].cumsum()
    df['cumulative_volume'] = df['volume'].cumsum()
    df['vwap'] = df['cumulative_trade_value'] / df['cumulative_volume']
    
    # 30분 단위로 리샘플링하여 VWAP 계산
    vwap_resampled = df.resample('30T').last()  # 마지막 값으로 리샘플링
    return vwap_resampled

@app.get("/", response_class=HTMLResponse)
async def read_root():
    log_data = read_log_file(file_path)
    a301f_data = parse_A301F(log_data)
    
    # 필터링: 10시부터 14시까지
    start_time_str = '10:00:00'
    end_time_str = '14:00:00'
    filtered_a301f = [row for row in a301f_data if start_time_str <= row[0].strftime('%H:%M:%S') <= end_time_str]
    
    # VWAP 데이터 생성
    vwap_df = calculate_vwap(filtered_a301f)
    
    # 데이터 시각화
    fig, ax = plt.subplots()
    ax.plot(vwap_df.index, vwap_df['vwap'], marker='o', linestyle='-', color='b')
    ax.set(xlabel='시간', ylabel='VWAP',
           title='VWAP 변동')
    ax.grid()
    
    # X축 형식 설정
    plt.xticks(rotation=45)  # X축 레이블 회전
    
    # 그래프를 메모리 버퍼에 저장
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # HTML 반환
    html_content = f'<img src="data:image/png;base64,{img_str}" alt="VWAP 그래프"/>'
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
