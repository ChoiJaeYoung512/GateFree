import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils import load_data

# ======== 시간이 지남에 따라 측정되는 RSSI 개수가 감소하는 경향 파악 ======== #

# path = '/home/krri/GH/RSSI_visualize/FP/Interference_effect/0525/'
path = '/media/krri/4E17-D17F/2023/GateFree/Data/0608/9'
file = 'data_9_all.csv'
# file = 'data_30m_1_one.csv'

data = pd.read_csv(os.path.join(path, file))
df, column_arr = load_data.front_load_file(data, False)
df.insert(0, 'time', data['time'])


standard = ['K007-3']
loc = ['K006-2', 'K006-3', 'K007-2', 'K007-3', 'K008-2', 'K008-3', 'K009-2', 'K009-3', 'K010-2', 'K010-3']

n = 5
cnt = 1
xlabel = range(0, len(df), 5000)

##### 1분 동안의 평균 그래프 #####
# time을 pandas의 datetime 형태로 변환
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d-%H-%M-%S.%f', errors='raise')
df = df.set_index('time')

test = df[loc].resample(rule='1S').count()
for i in range(0, len(loc), 2):
    plt.subplot(n, 1, cnt)
    plt.plot(test[loc[i:i+2]])
    plt.legend(loc[i:i+2], bbox_to_anchor = (1, 0.5), loc = 'center left')
    # plt.ylim(100, 1)
    cnt += 1
    
plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.2, hspace=0.45)
plt.show()


'''
## subplot1: 블록 별 RSSI 측정된 개수
## subplot2: resample(rule='x') x초마다 측정된 블록 별 RSSI 개수

cnt = df[loc].count()

plt.figure(figsize=(15, 8))
plt.subplot(2, 1, 1)
plt.plot(cnt)
plt.legend(loc, bbox_to_anchor = (1, 0.5), loc = 'center left')

for i in range(len(cnt)):
    plt.text(loc[i], cnt[i], '%d' %cnt[i])

plt.subplot(2, 1, 2)
plt.plot(test[loc])
plt.legend(loc, bbox_to_anchor = (1, 0.5), loc = 'center left')

plt.show()'''

'''
##### RSSI #####
기준점 블록
plt.figure(figsize=(15, 8))
plt.subplot(n, 1, 1)
plt.plot(df[standard])
plt.ylim(-90, -55)
plt.xticks(xlabel, df.iloc[xlabel]['time'].str.slice(11,))
plt.legend(standard, bbox_to_anchor = (1, 0.5), loc = 'center left')

# 나머지 블록
for i in range(1, len(loc), 3):
    plt.subplot(n, 1, cnt)
    plt.plot(df[loc[i:i+3]])
    plt.ylim(-95, -55)
    plt.legend(loc[i:i+3], bbox_to_anchor = (1, 0.5), loc = 'center left')
    
    cnt += 1
    
plt.show()
'''