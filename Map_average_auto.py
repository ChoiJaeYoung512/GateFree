import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import natsort
import sys
import glob
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils import load_data
from utils import fingerprinting
from utils import save_file

def Dist(df, target_minor, MAP, m):     # 측정 데이터, 위치, 신호 지도, 누적 카운트
    total_cnt = 0
    cnt = 0
    
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

        if min_dist == target_minor:
            cnt += 1
        
        # for문 돈 횟수 count -> 전체 데이터 길이 재는 용도
        total_cnt += 1
        
    accuracy_score = round(cnt / total_cnt, 4)
    
    return [target_minor, total_cnt, cnt, accuracy_score]

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

mapPath = ['/home/krri/Desktop/gatefree/GF/data/col_4/0713/0713_map.csv',
           '/home/krri/Desktop/gatefree/GF/data/col_4/0718/0718_map.csv',
           '/home/krri/Desktop/gatefree/GF/data/col_4/0720/0720_map.csv',
           '/home/krri/Desktop/gatefree/GF/data/col_4/0721/0721_map.csv',
           '/home/krri/Desktop/gatefree/GF/data/col_4/0801/0801_map.csv']

# map 평균내서 구하기
map1_data = pd.read_csv(os.path.join(mapPath[0]), index_col=0)
map2_data = pd.read_csv(os.path.join(mapPath[1]), index_col=0)
map3_data = pd.read_csv(os.path.join(mapPath[2]), index_col=0)
map4_data = pd.read_csv(os.path.join(mapPath[3]), index_col=0)
map5_data = pd.read_csv(os.path.join(mapPath[4]), index_col=0)

folder_name = ['0713','0718','0720','0721','0801']

for a, folder_name in enumerate(folder_name, 1) :
    path = f'/home/krri/Desktop/gatefree/GF/data/col_4/{folder_name}/test1/'
    file_list = glob.glob(path + 'data' + '*all.csv')
    file_list = natsort.natsorted(file_list)

    # Data 불러오기
    df_list = []
    for f in file_list:
        df = pd.read_csv(f, index_col = 0)
        df, column_arr = load_data.front_load_file(df, False)   # T: location 사용 / F: location 사용 X
        df = df.replace("127",np.nan)
        df = df.replace(127,np.nan)
        df_list.append(df)

    # MAP 불러오기
    map1 = (map2_data + map3_data + map4_data + map5_data)/4    # 0609 외 나머지3개 맵 데이터 평균
    map2 = (map1_data + map3_data + map4_data + map5_data)/4    # 0612 외 나머지3개 맵 데이터 평균
    map3 = (map1_data + map2_data + map4_data + map5_data)/4    # 0613 외 나머지3개 맵 데이터 평균
    map4 = (map1_data + map2_data + map3_data + map5_data)/4
    map5 = (map1_data + map2_data + map3_data + map4_data)/4    # 0616 외 나머지3개 맵 데이터 평균

    ms = 5
    data_list = []
    map_data_list = [map1, map2, map3, map4, map5]
    
    map_df = map_data_list[a-1]

    print(map_df)
    exit()

    for d, tm in zip(df_list, target_minor):
        data_list.append(Dist(d, tm, map_df, ms))
        print(Dist(d, tm, map_df, ms))
    
# 파일 저장
    savePath = '/home/krri/Desktop/gatefree/GF/data/col_4/avgMap/'
    sfile = f'avg_{a}_5D_100ms.csv'
    save_file.saveFile(savePath, sfile, data_list)