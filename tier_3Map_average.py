import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import natsort
import sys
import glob
import os
import fingerprinting_tier

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils import load_data
from utils import save_file

def Dist(df, target_minor, MAP, Tiers):     # 측정 데이터, 위치, 신호 지도, 누적 카운트
    total_cnt = 0
    num_tiers = len(Tiers)      # len(Tiers) = (0~5) 6
    count_by_tier = [0] * (num_tiers + 1)
    m = 1

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


path = '/media/krri/T7/gatefree/GF/data/col_4/0801/test1/'

file_list = glob.glob(path + 'data' + '*all.csv')
file_list = natsort.natsorted(file_list)

# Data 불러오기
df_list = []
# 6_1 ~ 15_4 까지 더함
for f in file_list:
    df = pd.read_csv(f, index_col = 0)
    df, column_arr = load_data.front_load_file(df, False)   # T: location 사용 / F: location 사용 X
    df = df.replace("127",np.nan)
    df = df.replace(127,np.nan)
    df_list.append(df)


# MAP 불러오기
mapPath = ['/media/krri/T7/gatefree/GF/data/col_4/0713/0713_map.csv',
            '/media/krri/T7/gatefree/GF/data/col_4/0718/0718_map.csv',
            '/media/krri/T7/gatefree/GF/data/col_4/0720/0720_map.csv',
            '/media/krri/T7/gatefree/GF/data/col_4/0721/0721_map.csv',
            '/media/krri/T7/gatefree/GF/data/col_4/0801/0801_map.csv']

# map 평균내서 구하기
map1_data = pd.read_csv(os.path.join(mapPath[0]), index_col=0)
map2_data = pd.read_csv(os.path.join(mapPath[1]), index_col=0)
map3_data = pd.read_csv(os.path.join(mapPath[2]), index_col=0)
map4_data = pd.read_csv(os.path.join(mapPath[3]), index_col=0)
map5_data = pd.read_csv(os.path.join(mapPath[4]), index_col=0)


map1 = (map2_data + map3_data + map4_data + map5_data)/4    # 0609 외 나머지3개 맵 데이터 평균
map2 = (map1_data + map3_data + map4_data + map5_data)/4    # 0612 외 나머지3개 맵 데이터 평균
map3 = (map1_data + map2_data + map4_data + map5_data)/4    # 0613 외 나머지3개 맵 데이터 평균
map4 = (map1_data + map2_data + map3_data + map5_data)/4    # 0616 외 나머지3개 맵 데이터 평균
map5 = (map1_data + map2_data + map3_data + map4_data)/4

target_minor = ['K006-1','K006-2','K006-3','K006-4', 
                'K007-1','K007-2','K007-3','K007-4',
                'K008-1','K008-2','K008-3','K008-4',
                'K009-1','K009-2','K009-3','K009-4',
                'K010-1','K010-2','K010-3','K010-4',
                'K011-1','K011-2','K011-3','K011-4',
                'K012-1','K012-2','K012-3','K012-4',
                'K013-1','K013-2','K013-3','K013-4',
                'K014-1','K014-2','K014-3','K014-4',
                'K015-1','K015-2','K015-3','K015-4'         
                ]


bl_1 = ['K006-1',['K006-2','K006-4'],['K006-3'],['K007-1','K011-1'],['K007-2','K011-4'],['K012-1']]
bl_2 = ['K006-2',['K006-1','K006-3','K011-1'], ['K006-4','K011-4'],['K007-2','K011-2'],['K007-1','K011-3','K012-1'],['K012-2']]
bl_3 = ['K006-3',['K006-2','K006-4','K007-2','K011-4'],['K006-1','K007-1','K011-1','K012-1'], ['K007-3','K011-3'],['K007-4','K012-2','K012-4'],['K012-3']]
bl_4 = ['K006-4',['K006-1','K006-3','K007-1'],['K006-2','K007-2'],['K007-4','K011-4'],['K007-3','K011-1','K012-1'],['K012-4']]
bl_5 = ['K007-1',['K006-4','K007-2','K007-4'],['K006-3','K007-3'],['K006-1','K008-1','K012-1'],['K006-2','K008-2','K011-4','K012-4'],['K011-1','K013-1']]
bl_6 = ['K007-2',['K006-3','K007-1','K007-3','K012-1'],['K006-4','K007-4','K011-4','K012-4'],['K006-2','K008-2','K012-2'],['K006-1','K008-1','K011-1','K011-3','K012-3','K013-1'],['K011-2','K013-2']]
bl_7 = ['K007-3',['K007-2','K007-4','K008-2','K012-4'],['K007-1','K008-1','K012-1','K013-1'],['K006-3','K008-3','K012-3'],['K006-4','K008-4','K011-4','K012-2','K013-2','K013-4'],['K011-3','K013-3']]
bl_8 = ['K007-4',['K007-1','K007-3','K008-1'],['K007-2','K008-2'],['K006-4','K008-4','K012-4'],['K006-3','K008-3','K012-1','K013-1'],['K011-4','K013-4']]
bl_9 = ['K008-1',['K007-4','K008-2','K008-4'],['K007-3','K008-3'],['K007-1','K009-1','K013-1'],['K007-2','K009-2','K012-4','K013-4'],['K012-1','K014-1']]
bl_10 = ['K008-2',['K007-3','K008-1','K008-3','K013-1'],['K007-4','K008-4','K012-4','K013-4'],['K007-2','K009-2','K013-2'],['K007-1','K009-1','K012-1','K012-3','K013-3','K014-1'],['K012-2','K014-2']]
bl_11 = ['K008-3',['K008-2','K008-4','K009-2','K013-4'],['K008-1','K009-1','K013-1','K014-1'],['K007-3','K009-3','K013-3'],['K007-4','K009-4','K012-4','K013-2','K014-2','K014-4'],['K012-3','K014-3']]
bl_12 = ['K008-4',['K008-1','K008-3','K009-1'],['K008-2','K009-2'],['K007-4','K009-4','K013-4'],['K007-3','K009-3','K013-1','K014-1'],['K012-4','K014-4']]
bl_13 = ['K009-1',['K008-4','K009-2','K009-4'],['K008-3','K009-3'],['K008-1','K010-1','K014-1'],['K008-2','K010-2','K013-4','K014-4'],['K013-1','K015-1']]
bl_14 = ['K009-2',['K008-3','K009-1','K009-3','K014-1'],['K008-4','K009-4','K013-4','K014-4'],['K008-2','K010-2','K014-2'],['K008-1','K010-1','K013-1','K013-3','K014-3','K015-1'],['K013-2','K015-2']]
bl_15 = ['K009-3',['K009-2','K009-4','K010-2','K014-4'],['K009-1','K010-1','K014-1','K015-1'],['K008-3','K010-3','K014-3'],['K008-4','K010-4','K013-4','K014-2','K015-2','K015-4'],['K013-3','K015-3']]
bl_16 = ['K009-4',['K009-1','K009-3','K010-1'],['K009-2','K010-2'],['K008-4','K010-4','K014-4'],['K007-3','K009-3','K013-1','K014-1'],['K013-4','K015-4']]
bl_17 = ['K010-1',['K009-4','K010-2','K010-4'],['K009-3','K010-3'],['K009-1','K015-1'],['K009-2','K014-4','K015-4'],['K014-1']]
bl_18 = ['K010-2',['K009-3','K010-1','K010-3','K015-1'],['K009-4','K010-4','K014-4','K015-4'],['K009-2','K015-2'],['K009-1','K014-1','K014-3','K015-3'],['K014-2']]
bl_19 = ['K010-3',['K010-2','K010-4','K011-2','K015-4'],['K010-1','K015-1'],['K009-3','K015-3'],['K009-4','K014-4','K015-2'],['K014-3']]
bl_20 = ['K010-4',['K010-1','K010-3','K011-1'],['K010-2'],['K009-4','K015-4'],['K009-3','K015-1'],['K014-4']]
bl_21 = ['K011-1',['K006-2','K011-2','K011-4'],['K006-3','K011-3'],['K006-1','K012-1'],['K006-4','K007-2','K012-2'],['K007-1']]
bl_22 = ['K011-2',['K011-1','K011-3'],['K011-4'],['K006-2','K012-2'],['K006-3','K012-1'],['K007-2']]
bl_23 = ['K011-3',['K011-2','K011-4','K012-2'],['K011-1','K012-1'],['K006-3','K012-3'],['K006-2','K007-2','K012-4'],['K007-3']]
bl_24 = ['K011-4',['K006-3','K011-1','K011-3','K012-1'],['K006-2','K007-2','K011-2','K012-2'],['K006-4','K012-4'],['K006-1','K007-1','K007-3','K012-3'],['K007-4']]
bl_25 = ['K012-1',['K007-2','K011-4','K012-2','K012-4'],['K006-3','K007-3','K011-3','K012-3'],['K007-1','K011-1','K013-1'],['K006-2','K006-4','K007-4','K008-2','K011-2','K013-2'],['K006-1','K008-1']]
bl_26 = ['K012-2',['K011-3','K012-1','K012-3'],['K011-4','K012-4'],['K007-2','K011-2','K013-2'],['K006-3','K007-3','K011-1','K013-1'],['K006-2','K008-2']]
bl_27 = ['K012-3',['K012-2','K012-4','K013-2'],['K012-1','K013-1'],['K007-3','K011-3','K013-3'],['K007-2','K008-2','K011-4','K013-4'],['K006-3','K008-3']]
bl_28 = ['K012-4',['K007-3','K012-1','K012-3','K013-1'],['K007-2','K008-2','K012-2','K013-2'],['K007-4','K011-4','K013-4'],['K006-3','K007-1','K008-1','K008-3','K011-3','K013-2'],['K006-4','K008-4']]
bl_29 = ['K013-1',['K008-2','K012-4','K013-2','K013-4'],['K007-3','K008-3','K012-3','K013-3'],['K008-1','K012-1','K014-1'],['K007-2','K007-4','K008-4','K009-2','K012-2','K014-2'],['K007-1','K009-1']]
bl_30 = ['K013-2',['K012-3','K013-1','K013-3'],['K012-4','K013-4'],['K008-2','K012-2','K014-2'],['K007-3','K008-3','K012-1','K014-1'],['K007-2','K009-2']]
bl_31 = ['K013-3',['K013-2','K013-4','K014-2'],['K013-1','K014-1'],['K008-3','K012-3','K014-3'],['K008-2','K009-2','K012-4','K014-4'],['K007-3','K009-3']]
bl_32 = ['K013-4',['K008-3','K013-1','K013-3','K014-1'],['K008-2','K009-2','K013-2','K014-2'],['K008-4','K012-4','K014-4'],['K007-3','K008-1','K009-1','K009-3','K012-3','K014-2'],['K007-4','K009-4']]
bl_33 = ['K014-1',['K009-2','K013-4','K014-2','K014-4'],['K008-3','K009-3','K013-3','K014-3'],['K009-1','K013-1','K015-1'],['K008-2','K008-4','K009-4','K010-2','K013-2','K015-2'],['K008-1','K010-1']]
bl_34 = ['K014-2',['K013-3','K014-1','K014-3'],['K013-4','K014-4'],['K009-2','K013-2','K015-2'],['K008-3','K009-3','K013-1','K015-1'],['K008-2','K010-2']]
bl_35 = ['K014-3',['K014-2','K014-4','K015-2'],['K014-1','K015-1'],['K009-3','K013-3','K015-3'],['K009-2','K010-2','K013-4','K015-4'],['K008-3','K010-3']]
bl_36 = ['K014-4',['K009-3','K014-1','K014-3','K015-1'],['K009-2','K010-2','K014-2','K015-2'],['K009-4','K013-4','K015-4'],['K008-3','K009-1','K010-1','K010-3','K013-3','K015-2'],['K008-4','K010-4']]
bl_37 = ['K015-1',['K010-2','K014-4','K015-2','K015-4'],['K009-3','K010-3','K014-3','K015-3'],['K010-1','K014-1'],['K009-2','K009-4','K010-4','K014-2'],['K009-1']]
bl_38 = ['K015-2',['K014-3','K015-1','K015-3'],['K014-4','K015-4'],['K010-2','K014-2'],['K009-3','K010-3','K014-1'],['K009-2']]
bl_39 = ['K015-3',['K015-2','K015-4'],['K015-1'],['K010-3','K014-3'],['K010-2','K014-4'],['K009-3']]
bl_40 = ['K015-4',['K010-3','K015-1','K015-3'],['K010-2','K015-2'],['K010-4','K014-4'],['K009-3','K010-1','K014-3'],['K009-4']]


tier_lists = [bl_1, bl_2, bl_3, bl_4, bl_5, bl_6, bl_7, bl_8, bl_9, bl_10,
              bl_11,bl_12,bl_13,bl_14,bl_15,bl_16,bl_17,bl_18,bl_19,bl_20,
              bl_21,bl_22,bl_23,bl_24,bl_25,bl_26,bl_27,bl_28,bl_29,bl_30,
              bl_31,bl_32,bl_33,bl_34,bl_35,bl_36,bl_37,bl_38,bl_39,bl_40]

data_list = []

cumulative_accuracy_scores = [0.0] * 7 

for i in range(len(df_list)):
    result = Dist(df_list[i], target_minor[i], map5, tier_lists[i])
    target_minor_result = result[0]
    accuracy_scores_by_tier_result = result[1]

    cumulative_accuracy_scores = [cumulative_accuracy_scores[j] + accuracy_scores_by_tier_result[j] for j in range(7)]

    tier_result_formatted = ', '.join([f"{score:.4f}" for score in cumulative_accuracy_scores])
    data_list.append([target_minor_result] + list(accuracy_scores_by_tier_result))  # 수정된 부분
    print([target_minor_result] + list(accuracy_scores_by_tier_result))

    # 누적 값을 다음 데이터를 위해 초기화
    cumulative_accuracy_scores = [0.0] * 7
    
# 파일 저장
savePath = '/media/krri/T7/gatefree/GF/data/col_4/Tier_20/'
sfile = 'avgTier_s_5_5D_20ms.csv'
df = pd.DataFrame(data_list, columns=['target'] + [f'Tier_{i}' for i in range(7)])

df.to_csv(os.path.join(savePath, sfile), index=False,header= False)

# save_file.saveFile(savePath, sfile, flattened_data_list)
