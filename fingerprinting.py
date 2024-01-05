import pandas as pd
import numpy as np

def Dist(df, target_minor, MAP, m):     # 측정 데이터, 위치, 신호 지도, 누적 카운트
    total_cnt = 0
    cnt = 0
    
    # 20/40/60/80/100ms 변경 시, m 변경
    for i in range(0, len(df), m):
        print(i, end='\r')
        
        data = df.iloc[i:i+m].mean(numeric_only=True)
        minors = data.index.to_numpy()
        distance_dict = {}

        for t in MAP.index:
            distance = np.sqrt(MAP.loc[t][minors].sub(data).pow(2).sum())
            print(distance)
            distance_dict[t] = distance

        min_dist = min(distance_dict, key = distance_dict.get) # Dictionary 중 가장 작은 값에 대한 key 값 추출

        if min_dist == target_minor:
            cnt += 1
        
        # for문 돈 횟수 count -> 전체 데이터 길이 재는 용도
        total_cnt += 1
        
    accuracy_score = round(cnt / total_cnt, 4)
    
    return [target_minor, total_cnt, cnt, accuracy_score]