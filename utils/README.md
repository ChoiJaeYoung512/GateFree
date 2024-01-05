# utils - import 코드 모음
1. fingerprinting.py
    - 핑거프린팅 알고리즘 코드
    - 실험방법대로 진행

2. fingerprinting2.py
    - 핑거프린팅 알고리즘 코드에 오차 범위 추가
    - 오차 범위: target 블록에서 앞뒤 블록까지 인정

3. load_data.py
    - 앞쪽 스마트 블록(K로 시작)은 front_load_file, 뒤쪽 스마트 블록(숫자 시작)은 back_load_file import
    - 블록 40개(게이트 블록 제외)에 해당하는 데이터 전처리 과정(추후 블록 봐야할 블록이 많아지면 추가해야함)
    - input: 전처리할 data, data 중 location(밟은 위치 블록) 사용 여부 T/F
    - output: 전처리 된 df, 블록 40개에 해당하는 블록 ID

4. dataDivision.py
    - 데이터셋 분할 코드
    - random(): frac에 원하는 랜덤한 비율만큼 적고 test셋으로 추출
    - k_prttn(): k개의 셀 중, 1개를 test셋으로 추출

5. save_file.py
    - 파일 저장 코드
    - input: 저장할 path, 저장할 filename, 저장할 data
    - output: path에 filename.csv로 저장
    - filename은 꼭 다르게 지정해주기 -> mode = 'a'이기에 이미 쓰여진 곳에 덧붙여서 작성됨
    - 사용 안하면 주석처리 하기