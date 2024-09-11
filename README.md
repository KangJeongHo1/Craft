
# 시장 데이터 분석 API
이 프로젝트는 FastAPI를 기반으로 시장 로그 데이터를 분석하는 애플리케이션입니다. 주로 VWAP(거래량 가중 평균 가격) 계산과 취소 수량 분석에 중점을 두고 있습니다.

# 주요 기능
VWAP 계산: 시장 로그 데이터를 기반으로 VWAP을 계산하고 시각화합니다.
취소 수량 분석: 다양한 가격 수준에서 총 취소된 주문 수량을 분석하고 계산합니다.

# 엔드포인트
## 1. /VWAP
설명: 지정된 시간 범위 내에서 VWAP을 계산하고 시각화합니다.
응답: 선택한 시간 동안의 VWAP 그래프를 반환합니다.

## 2. /cancellation
설명: 각 가격 레벨에서 총 취소된 주문 수량을 계산합니다.
응답: 각 호가별 총 취소 수량을 반환합니다.

## 파일 경로 설정
프로젝트를 실행하기 전에, 로그 파일 경로를 올바르게 설정해야 합니다. 기본적으로 파일 경로는 main.py 또는 관련 스크립트 내에 하드코딩되어 있으므로, 환경에 맞게 변경해야 합니다.
예시:
### file_path = '/Users/kang/Desktop/sample/시세/2.log'

### 데이터 처리 시간 주의
취소 수량을 수집할 때, 데이터 양이 많으면 처리 시간이 오래 걸릴 수 있습니다. 대용량 로그 파일을 다루는 경우 성능을 고려해야 합니다.

### Poetry를 이용한 가상환경 설정
이 프로젝트는 Poetry를 사용하여 가상환경을 관리하고 의존성을 설치합니다. 아래 명령어를 통해 필요한 패키지를 설치할 수 있습니다:

### poetry install
이 명령어는 pyproject.toml 파일에 정의된 모든 의존성을 설치합니다.
