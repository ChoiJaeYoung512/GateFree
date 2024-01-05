import pandas as pd
import numpy as np

def Dist(df, target_minor, MAP, m):     # 측정 데이터, 위치, 신호 지도, 누적 카운트
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
            front = block[target_idx + 1]
            
            if front in min_distance_dict:
                cnt += min_distance_dict[front]
            cnt += min_distance_dict[target_minor]
            
        elif target_minor == 'K010-3':
            back = block[target_idx - 1]
            
            if back in min_distance_dict:
                cnt += min_distance_dict[back]
            cnt += min_distance_dict[target_minor]
        else:
            front = block[target_idx + 1]
            back = block[target_idx - 1]
            
            if front in min_distance_dict and back in min_distance_dict:
                cnt += min_distance_dict[front] + min_distance_dict[back]
            elif front in min_distance_dict and back not in min_distance_dict:
                cnt += min_distance_dict[front]
            elif front not in min_distance_dict and back in min_distance_dict:
                cnt += min_distance_dict[back]
            cnt += min_distance_dict[target_minor]
                
    answer = pd.DataFrame(answer)
    accuracy_score = round(cnt / total_cnt, 4)
    
    return [target_minor, total_cnt, cnt, accuracy_score]