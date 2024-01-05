import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import board_heatmap
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils import load_data

# 경로 -> E, W, N, S 변경
# data_path = '/home/krri/GH/RSSI_visualize/front_gate/W/'
data_path = '/home/krri/GH/RSSI_visualize/FP/gatefree/0517/static/map/'
data = pd.read_csv(data_path + 'data_8_2_40_all.csv')

tier1_group = ['K007-3', 'K007-4', 'K008-1', 'K008-3', 'K008-4', 'K012-4', 'K013-1', 'K013-4']
tier2_group = ['K007-1', 'K007-2', 'K009-1', 'K009-2', 'K012-1', 'K012-2', 'K012-3', 
               'K013-2', 'K013-3', 'K014-1', 'K014-2']
tier3_group = ['K006-3', 'K006-4', 'K009-3', 'K009-4', 'K011-3', 'K011-4', 'K014-3', 'K014-4']
tier4_group = ['K006-1', 'K006-2', 'K010-1', 'K010-2', 'K011-1', 'K011-2', 'K015-1', 'K015-2']
tier5_group = ['K010-3', 'K010-4', 'K015-3', 'K015-4']

# file load
df, column_arr = load_data.front_load_file(data, False)

# 8-2 기준 RSSI 시각화
def standard(col_name):
    test = df[col_name]
    cnt = test.count()
    
    plt.plot(test.dropna(axis=0), '.')
    plt.ylim(-40, -100)
    plt.title(col_name + "  [ total count: " + str(cnt) + "]")
    plt.show()
    
# standard('K008-2')

def visualize(tier1_group, tier2_group):
    tier1_lgd = []
    tier2_lgd = []
    stan = abs(df['K008-2'].mean())
    tier1_max = abs(df[tier1_group].mean())#.idxmin()
    tier2_max = abs(df[tier2_group].mean())#.idxmin()
    print(stan, tier1_max, tier2_max)
    
    plt.figure(2)

    # 8-2 기준 RSSI 그래프
    plt.subplot(4, 1, 1)
    plt.plot(df['K008-2'].dropna(axis=0), '.')
    plt.ylim(-20, -100)
    plt.title('K008-2')
    
    # tier1
    for i in range(0, len(tier1_group)):
        # cnt.append(df[tier1_group[i]].count())    # 각 tier 별 RSSI count
        
        plt.subplot(4, 1, 2)
        plt.plot(df[tier1_group[i]].dropna(axis=0), '.')
        plt.ylim(-20, -100)
        plt.title('TIER_1')
        
        tier1_lgd.append(tier1_group[i])
        plt.legend(tier1_lgd, bbox_to_anchor = (1, 0.5), loc = 'center left')
    
    # tier2
    for i in range(0, len(tier2_group)):
        # cnt.append(df[tier2_group[i]].count())
        
        plt.subplot(4, 1, 3)
        plt.plot(df[tier2_group[i]].dropna(axis=0), '.')
        plt.ylim(-20, -100)
        plt.title('TIER_2')
        
        tier2_lgd.append(tier2_group[i])
        plt.legend(tier2_lgd, bbox_to_anchor = (1, 0.5), loc = 'center left')
    
    # 총 RSSI 개수
    cnt = df.count()
    
    plt.subplot(4, 1, 4)
    plt.xticks(rotation = 45)
    plt.title('Total RSSI Count')
    plt.plot(cnt)
    
    # 그래프 값 표시
    for i in range(len(cnt)):
        plt.text(column_arr[i], cnt[i], '%d' %cnt[i])
    
    plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.2, hspace=0.45)
    # plt.show()

# 나머지 - 3, 4, 5 그룹
def visualize_2(tier3_group, tier4_group, tier5_group):
    tier3_lgd = []
    tier4_lgd = []
    tier5_lgd = []
    
    tier3_max = abs(df[tier3_group].mean())#.idxmin()
    tier4_max = abs(df[tier4_group].mean())#.idxmin()
    tier5_max = abs(df[tier5_group].mean())#.idxmin()
    print(tier3_max, tier4_max, tier5_max)
    
    plt.figure(3)
    
    # tier3
    for i in range(0, len(tier3_group)):
        # cnt.append(df[tier1_group[i]].count())    # 각 tier 별 RSSI count
        
        plt.subplot(3, 1, 1)
        plt.plot(df[tier3_group[i]].dropna(axis=0), '.')
        plt.ylim(-20, -100)
        plt.title('TIER_3')
        
        tier3_lgd.append(tier3_group[i])
        plt.legend(tier3_lgd, bbox_to_anchor = (1, 0.5), loc = 'center left')
        
    # tier4
    for i in range(0, len(tier4_group)):
        # cnt.append(df[tier1_group[i]].count())    # 각 tier 별 RSSI count
        
        plt.subplot(3, 1, 2)
        plt.plot(df[tier4_group[i]].dropna(axis=0), '.')
        plt.ylim(-20, -100)
        plt.title('TIER_4')
        
        tier4_lgd.append(tier4_group[i])
        plt.legend(tier4_lgd, bbox_to_anchor = (1, 0.5), loc = 'center left')
        
    plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.2, hspace=0.45)
    
    # tier5
    for i in range(0, len(tier5_group)):
        # cnt.append(df[tier1_group[i]].count())    # 각 tier 별 RSSI count
        
        plt.subplot(3, 1, 3)
        plt.plot(df[tier5_group[i]].dropna(axis=0), '.')
        plt.ylim(-20, -100)
        plt.title('TIER_5')
        
        tier5_lgd.append(tier5_group[i])
        plt.legend(tier5_lgd, bbox_to_anchor = (1, 0.5), loc = 'center left')
        
    plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.2, hspace=0.45)
    # plt.show()

# heatmap 그리기
board = [[0 for i in range(4)] for j in range(10)]
board_heatmap.front_map(board, df, column_arr)
    
visualize(tier1_group, tier2_group)
visualize_2(tier3_group, tier4_group, tier5_group)

plt.show()