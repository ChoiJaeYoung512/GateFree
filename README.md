# GateFree
한국철도기술연구원(KRRI) GateFree 과제 코드

# 실험 방법
- RSSI_MAP: RSSI의 값들을 각 Beacon 별로 평균치 낸 값(Target Data로 쓰일 예정)
- data: 시간대별로 Device가 취득한 데이터들의 값을 각 Beacon 별로 추출한 값
  
데이터 취득
- 40개 Block에서 정적(Static)인 상황, 동적(Dynamic)인 상황으로 나눠 측정

방법
FP(FingerPrinting) 알고리즘 사용하여 RSSI_MAP과 data 비교
- compare : 지정 날짜의 data와 지정 날짜 외의 날짜의 RSSI_MAP과 비교하여 가장 가까운 Distance의 블록과 data의 블록이 일치하는 정확도(Accuracy) 측정
- 3Map_average : 지정 날짜의 data와 지정 날짜 외 모든 RSSI_MAP을 평균하여 비교한 후 정확도 측정
- soft_voting : 지정 날짜의 data와 지정 날짜 외 모든 RSSI_MAP을 FP 알고리즘에 의해 계산된 값을 평균하여 비교 후 정확도 측정
- hard_voting : 지정 날짜의 data와 지정 날짜 외 모든 RSSI_MAP을 FP 알고리즘을 통해 가장 가깝다고 측정된 블록을 과반수에 의해 판단된 값과 비교하여 정확도 측정
- Tier : 해당 블록과 가장 가까운 블록을 1 Tier, 그 다음으로 가까운 블록을 2 Tier로 5 Tier까지 지정하여 오차범위 파악을 위한 분석
  
결과
- 한 프레임과 RSSI_MAP을 연산 한 결과, Distance가 가장 짧은 값에 해당하는 Beacon이 Device가 있는 위치로 추정한다.
- 모든 프레임을 RSSI_MAP과 연산한 후 가장 가까운 Distance에 해당하는 Beacon과 실제 Device가 있었던 beacon을 비교하여 Accuracy 를 구할 수 있다.

# 코드
1. utils - import 코드 모음

- 
