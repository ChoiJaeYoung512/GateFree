
# visualization - 데이터 분석 시각화
1. mapInfo.py
    - 취득한 RSSI MAP들의 경향 파악을 위한 코드
    - 4일치 RSSI MAP들의 표준편차 시각화

2. interference.py
    - 시간이 지남에 따라 측정되는 RSSI 개수가 감소하는 경향 파악

3. compare_2apps.py
    - 최적화 전 어플 Ver3와 최적화 후 어플 Ver4의 데이터 개수 비교 시각화
    - 1초 단위로 데이터 개수 파악

4. accuracy_visualize.py
    - 핑거프린팅 알고리즘 결과 시각화 코드
    - acc_by_block(): 블록 별 정확도(밟은 블록 기준)
    - block_by_acc(): 데이터 누적별 정확도(20ms, 40ms, 60ms, 80ms, 100ms 기준) - 사용 X
    - RSSI_CNT(): 측정된 RSSI 개수 세기

5. RSSI_MAP_Analysis.py
    - RSSI MAP 경향 파악 시각화
    - MAP이 일정한지 파악
    - 다른 날 취득한 RSSI MAP 데이터를 블록 별로 나눈 후, 시각화

6. FP3visual.py
    - 핑거프린팅 3가지 방법 시각화
    - 방법1: 4개의 MAP에 대해 하나씩 비교 후, 거리 계산 sum
    - 방법2: 날짜마다 다른 MAP 3개의 평균
    - 방법3: 4개의 MAP에 대해 하나씩 비교 후, 나온 위치 정보 투표 방식

7. front_gate_visualize.py & back_gate_visualize.py
    - 현재 밟고 있는 블록 기준으로 티어별 평균값 시각화 코드
    - 철기연 일용직 시작하자마자 진행한 코드(현재 사용 X)

8. board_heatmap.py
    - 블록의 평균 heatmap으로 표현
    - 철기연 일용직 시작하자마자 진행한 코드(현재 사용 X)

9. tier_RSSI.py & total_RSSI.py
    - RSSI 히스토그램으로 표현
    - 철기연 일용직 시작하자마자 진행한 코드(현재 사용 X)