import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import load_data
import natsort
import sys
import glob
import os
import csv
import fingerprinting

# 65, 67, 91, 103, 104 수정 필요

def Dist(df, target_minor, MAP, m):     # 측정 데이터, 위치, 신호 지도, 누적 카운트
    total_cnt = 0
    cnt = 0
    
    # 20/40/60/80/100ms 변경 시, m 변경
    for i in range(0, len(df), m):
        print(i, end='\r')
        
        data = df.iloc[i:i+m].mean(numeric_only=True)
        minors = data.index.to_numpy()
        distance_dict = {}
        min_dist = []
        for t in MAP.index:
            distance = np.sqrt(MAP.loc[t][minors].sub(data).pow(2).sum())
            distance_dict[t] = distance

        min_dist = min(distance_dict, key = distance_dict.get) # Dictionary 중 가장 작은 값에 대한 key 값 추출

        if min_dist == target_minor:
            cnt += 1
        
        # for문 돈 횟수 count -> 전체 데이터 길이 재는 용도
        total_cnt += 1
        
    accuracy_score = round(cnt / total_cnt, 4)
    
    return [target_minor,   total_cnt  , cnt, accuracy_score]

# 블록 ID
idx = [[6, 1], [6, 2],[6, 3], [6, 4],
       [7, 1], [7, 2],[7, 3], [7, 4],
       [8, 1], [8, 2],[8, 3], [8, 4],
       [9, 1], [9, 2],[9, 3], [9, 4],
       [10, 1], [10, 2],[10, 3], [10, 4],
       [11, 1], [11, 2],[11, 3], [11, 4],
       [12, 1], [12, 2],[12, 3], [12, 4],
       [13, 1], [13, 2],[13, 3], [13, 4],
       [14, 1], [14, 2],[14, 3], [14, 4],
       [15, 1], [15, 2],[15, 3], [15, 4]
       ]

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

folder_name = ['0713','0718','0720','0721','0801']

path = '/home/krri/Desktop/gatefree/GF/data/col_4/0801/test1/'       # data

for a, folder in enumerate(folder_name,1) :
    rssi_path = f'/home/krri/Desktop/gatefree/GF/data/col_4/{folder}/rssiMap/'  # map
    file_list = glob.glob(path + 'data' + '*all.csv')
    file_list = natsort.natsorted(file_list)

# # Data 불러오기
    df_list = []
    for f in file_list:
        df = pd.read_csv(f, index_col = 0)
        df, column_arr = load_data.front_load_file(df, False)   # T: location 사용 / F: location 사용 X
        df_list.append(df)

    RSSI_MAP = pd.DataFrame()

    for i in idx:
        rssi_list = rssi_path + 'rssiMap_' + f'{i[0]}_' + f'{i[1]}_' + 'one.csv'
        dt = pd.read_csv(rssi_list, index_col = 0)
        RSSI_MAP = pd.concat([RSSI_MAP, dt])

    RSSI_MAP = RSSI_MAP[column_arr].replace("non", np.nan)
    RSSI_MAP = RSSI_MAP.apply(pd.to_numeric)

    # 초 수정
    ms = 10
    file_list = natsort.natsorted(file_list)
    data_list = []

    for d, tm in zip(df_list, target_minor):
        data_list.append(Dist(d, tm, RSSI_MAP, ms))
        print(Dist(d, tm, RSSI_MAP, ms))

# 파일 저장

    # save_path = '/home/krri/Desktop/gatefree/GF/data/col_4/compare/'
    save_path = '/home/krri/Desktop/gatefree/GF/data/col_4/compare/'
    f = open(f'{save_path}5_{a}_s_200ms.csv', 'a')
    writer = csv.writer(f)

    for data in data_list:
        writer.writerow(data)
    f.close()

