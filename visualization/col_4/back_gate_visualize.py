import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import board_heatmap
import utils.load_data as load_data


# 경로 -> E, W, N, S 변경
data_path = '/home/krri/GH/RSSI_visualize/back_gate/S/'
data = pd.read_csv(data_path + 'data__all.csv')

tier1_group = ['007-1', '007-4', '008-1', '012-1', '012-2', '012-4', '013-1', '013-2']
tier2_group = ['006-3', '006-4', '007-2', '007-3', '008-2', '008-3', '008-4', 
               '011-3', '011-4', '013-3', '013-4']
tier3_group = ['006-1', '006-2', '009-1', '009-2', '011-1', '011-2', '014-1', '014-2']
tier4_group = ['009-3', '009-4', '014-3', '014-4']

# file load
df, column_arr = load_data.back_load_file(data)

# 기준 보드 RSSI 시각화
def standard(col_name):
    test = df[col_name]
    cnt = test.count()
    
    plt.plot(test.dropna(axis=0), '.')
    plt.ylim(-20, -100)
    plt.title(col_name + "  [ total count: " + str(cnt) + "]")
    plt.show()
    
# standard('012-3')

# main - 기준 보드, 1, 2 그룹, 총 RSSI 개수
def visualize(tier1_group, tier2_group):
    tier1_lgd = []
    tier2_lgd = []
    
    stan = abs(df['012-3'].mean())
    tier1_max = abs(df[tier1_group].mean())#.idxmin()
    tier2_max = abs(df[tier2_group].mean())#.idxmin()
    print(stan, tier1_max, tier2_max)
    # cnt = []
    
    plt.figure(2)

    # 12-3 기준 RSSI 그래프
    plt.subplot(4, 1, 1)
    plt.plot(df['012-3'].dropna(axis=0), '.')
    plt.ylim(-20, -100)
    plt.title('012-3')
    
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

# 나머지 - 3, 4 그룹
def visualize_2(tier3_group, tier4_group):
    tier3_lgd = []
    tier4_lgd = []
    
    tier3_max = abs(df[tier3_group].mean())#.idxmin()
    tier4_max = abs(df[tier4_group].mean())#.idxmin()
    print(tier3_max, tier4_max)
    
    plt.figure(3)
    
    # tier3
    for i in range(0, len(tier3_group)):
        # cnt.append(df[tier1_group[i]].count())    # 각 tier 별 RSSI count
        
        plt.subplot(2, 1, 1)
        plt.plot(df[tier3_group[i]].dropna(axis=0), '.')
        plt.ylim(-20, -100)
        plt.title('TIER_3')
        
        tier3_lgd.append(tier3_group[i])
        plt.legend(tier3_lgd, bbox_to_anchor = (1, 0.5), loc = 'center left')
        
    # tier4
    for i in range(0, len(tier4_group)):
        # cnt.append(df[tier1_group[i]].count())    # 각 tier 별 RSSI count
        
        plt.subplot(2, 1, 2)
        plt.plot(df[tier4_group[i]].dropna(axis=0), '.')
        plt.ylim(-20, -100)
        plt.title('TIER_4')
        
        tier4_lgd.append(tier4_group[i])
        plt.legend(tier4_lgd, bbox_to_anchor = (1, 0.5), loc = 'center left')
        
    plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.2, hspace=0.45)
    # plt.show()
        
# heatmap 그리기
board = [[0 for i in range(4)] for j in range(10)]
board_heatmap.back_map(board, df, column_arr)

visualize(tier1_group, tier2_group)
visualize_2(tier3_group, tier4_group)

plt.show()
