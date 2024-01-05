
import pandas as pd
import numpy as np

totalData = 0
correctData = 0
totalAcc = 0

def Dist(df, target_minor, MAP, m, mrg):     # 측정 데이터, 위치, 신호 지도, 누적 카운트, 오차 범위
    global totalData
    global correctData
    global totalAcc
    
    total_cnt = 0
    cnt = 0
    min_distance_dict = {}
    answer = []
    block = ['K006-2', 'K006-3', 'K007-2', 'K007-3', 'K008-2', 'K008-3', 'K009-2', 'K009-3', 'K010-2', 'K010-3']
    
    for i in range(0, len(df)):
        print(i, end='\r')
        
        data = df.iloc[i:i+m].mean().dropna()
        minors = data.index.to_numpy()
        distance_dict = {}
        
        for t in MAP.index:
            distance = np.sqrt(MAP.loc[t][minors].sub(data).pow(2).sum())
            distance_dict[t] = distance
            
        min_dist = min(distance_dict, key = distance_dict.get)
        answer.append(min_dist)
        
        if min_dist in min_distance_dict:
            min_distance_dict[min_dist] += 1
            
        else:
            min_distance_dict[min_dist] = 1
        
        total_cnt += 1
        
    min_distance_dict = dict(sorted(min_distance_dict.items()))
    # 오차범위 추가(앞, 뒤 블록까지 인정)
    if target_minor in block:
        target_idx = block.index(target_minor)
        
        if target_minor == 'K006-2':
            front = block[target_idx:target_idx + mrg + 1]
            for f in front:
                if f in min_distance_dict:
                    cnt += min_distance_dict[f]
            
        elif target_minor == 'K010-3':
            back = block[target_idx - mrg:target_idx + 1]
            for b in back:
                if b in min_distance_dict:
                    cnt += min_distance_dict[b]
        else:
            if mrg > target_idx:
                fb = block[:target_idx + mrg + 1]
            else:
                fb = block[target_idx - mrg:target_idx + mrg + 1]
            for t in fb:
                if t in min_distance_dict:
                    cnt += min_distance_dict[t]
                
    answer = pd.DataFrame(answer)
    accuracy_score = round(cnt / total_cnt, 4)
    
    totalData += total_cnt
    correctData += cnt
    totalAcc = round(correctData / totalData, 4)
    
    return [totalData, correctData, totalAcc] #[target_minor, total_cnt, cnt, accuracy_score], 
