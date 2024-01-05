import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import natsort
import glob

path = '/home/krri/Desktop/gatefree/GF/data/col_4/avgMap/'
df_list = glob.glob(path + 'avg_'+'*4D_100ms.csv')
df_list = natsort.natsorted(df_list)

# RSSI 개수 세기
def RSSI_CNT(file):
    df = pd.read_csv(file[0], header=None)
    df.columns = ['location', 'Total', 'Correct', 'Accuracy']
    cnt = df['Total']
    # 20ms 개수 -> 100ms 단위 *5
    cnt = cnt *5
    # 20ms 개수 -> 200ms 단위 * 10
    # cnt = cnt *10
    
    plt.subplot(2, 1, 1)
    plt.xticks(range(40), labels=df['location'], fontsize = 8 )
    plt.plot(cnt, marker='.')

    # 제목 재설정 필요
    plt.title('100ms Map')

    
    # 그래프 값 표시
    for i in range(len(cnt)):
        plt.text(i, cnt[i], '%d' %cnt[i])

# 블록 별 누적 그래프
def acc_by_block(file):
    plt.figure(figsize=(20, 40))
    plt.subplot(2, 1, 2)
    
    cell_text = []
    lgd = ['Day2', 'Day3', 'Day4', 'Day5']
    
    for f in file:
        df = pd.read_csv(os.path.join(path, f), header=None)
        df.columns = ['location', 'Total', 'Correct', 'Accuracy']
        
        plt.plot(df['location'], df['Accuracy'], marker='.')
        plt.ylim(0, 1)
        plt.legend(lgd, bbox_to_anchor = (1, 0.5), loc = 'center left')
        
        # 표
        cell_text.append(list(np.round(df['Accuracy'].values, 4)))
    
    # plt.table(cellText=cell_text, rowLabels=lgd, colLabels=df['location'], cellLoc='center', rowLoc='right', loc='bottom')
    plt.xticks(range(40), labels=df['location'], fontsize = 8)
    
        # 값 수치
        # for i in range(len(df)):
        #     plt.text(df['location'][i], df['Accuracy'][i], round(df['Accuracy'][i], 4))

    # plt.savefig(path + '0517_dy_test.png')


# 누적 별 블록 그래프
# def block_by_acc(file):
#     data = pd.DataFrame()
#     plt.subplot(3, 1, 2)

#     for f in file:
#         df = pd.read_csv(os.path.join(path, f), header=None)
#         data = pd.concat([data, df])
        
#     data.columns = ['location', 'Total', 'Correct', 'Accuracy']

#     for d in data['location']:
#         groups = data.groupby('location')
#         groups_data = groups.get_group(d)
#         groups_data.to_csv(save_path + f'{d}_group.csv', index=False, na_rep='non')
        
#     group_list = glob.glob(save_path + '*.csv')
#     group_list = natsort.natsorted(group_list)
#     group_lgd = []

#     # plt.figure(figsize=(12,10))

#     for g in group_list:
#         group = pd.read_csv(g)  # os.path.join(save_path, g)
#         plt.plot(group.index, group['Accuracy'], marker='.')
#         plt.ylim(0, 1)
#         plt.xticks(range(5), labels=['20ms', '40ms', '60ms', '80ms', '100ms'])

#         group_lgd.append(g[-16:-10])
#         plt.legend(group_lgd, bbox_to_anchor = (1, 0.5), loc = 'center left')


    
acc_by_block(df_list)
RSSI_CNT(df_list)
# block_by_acc(df_list)


plt.savefig(path + '0616_0613_1.png')
plt.show()
