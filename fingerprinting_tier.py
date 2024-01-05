import pandas as pd
import numpy as np

def Dist(df, target_minor, MAP, Tiers):     # 측정 데이터, 위치, 신호 지도, 누적 카운트
    total_cnt = 0
    num_tiers = len(Tiers)      # len(Tiers) = (0~5) 6
    count_by_tier = [0] * (num_tiers + 1)
    m = 5

    # 20/40/60/80/100ms 변경 시, m 변경
    for i in range(0, len(df),m):
        print(i, end='\r')
        data = df.iloc[i:i+m].mean(numeric_only=True)
        minors = data.index.to_numpy()
        distance_dict = {}
        min_dist= []
        for t in MAP.index:
            distance = np.sqrt(MAP.loc[t][minors].sub(data).pow(2).sum())
            distance_dict[t] = distance

        min_dist = min(distance_dict, key = distance_dict.get) # Dictionary 중 가장 작은 값에 대한 key 값 추출
        
        found_in_tier = False
        for a in range(num_tiers + 1) :     # 0 ~ 5 
            current_tier = Tiers 
            for tier_num, tier_values in enumerate(current_tier, start = 0) :
                if min_dist in tier_values :
                    # print([tier_num])
                    # print([tier_values])
                    count_by_tier[tier_num] += 1
                    found_in_tier = True
                    break
            if found_in_tier :
                break
        else : 
            count_by_tier[num_tiers] += 1
        
        # for문 돈 횟수 count -> 전체 데이터 길이 재는 용도
        total_cnt += 1
        # print(min_dist)
    
    accuracy_scores_by_tier = []
    
    for tier_count in count_by_tier :
        accuracy_scores_by_tier.append(round(tier_count / total_cnt, 4))
    
    return [target_minor, accuracy_scores_by_tier]


                    # if tier_num == 0:
                    #     count_by_tier[0] += 1
                    # elif tier_num == 1:
                    #     count_by_tier[1] += 1
                    # elif tier_num == 2:
                    #     count_by_tier[2] += 1
                    # elif tier_num == 3:
                    #     count_by_tier[3] += 1
                    # elif tier_num == 4:
                    #     count_by_tier[4] += 1
                    # elif tier_num == 5:
                    #     count_by_tier[5] += 1
                    # found_in_tier = True
                    # break