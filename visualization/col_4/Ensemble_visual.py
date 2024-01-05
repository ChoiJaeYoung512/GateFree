import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import natsort
import glob

sub_plots = plt.subplots(5, 1, figsize=(40,40))
fig = sub_plots[0]
graph = sub_plots[1]

# 4개의 MAP에 대해 하나씩 비교 후, 거리 계산 sum
path = '/home/krri/Desktop/gatefree/GF/data/col_4/avgMap/'
df_list = glob.glob(path + '*5D_100ms.csv')
df_list = natsort.natsorted(df_list)

data_list = []
for f in df_list:
    data = pd.read_csv(f, index_col=0, header=None)
    data_list.append(data)


# # 날짜마다 다른 MAP 3개의 평균 (soft voting)
path2 = '/home/krri/Desktop/gatefree/GF/data/col_4/soft_vote/'
df_list2 = glob.glob(path2 + '*5D_vote_s.csv')  
df_list2 = natsort.natsorted(df_list2)

data_list2 = []
for f2 in df_list2:
    data2 = pd.read_csv(f2, index_col=0, header=None)
    data_list2.append(data2)
    
# 1(data) : 3(map) 비교하여 과반수 이상 맵 매칭 결과 
path3 = '/home/krri/Desktop/gatefree/GF/data/col_4/hard_vote/'
df_list3 = glob.glob(path3 + '*_s.csv')
df_list3 = natsort.natsorted(df_list3)

data_list3 = []
for f3 in df_list3:
    data3 = pd.read_csv(f3, index_col=0, header=None)
    data_list3.append(data3)

graph[0].plot(data_list[0].index, data_list[0][3])
graph[0].plot(data_list2[0].index, data_list2[0][3], '-.')
graph[0].plot(data_list3[0].index, data_list3[0][3], '.')
graph[0].set_title('Day 1', x = 1.05, y = 0.8)

print(data_list[3])
exit()

graph[1].plot(data_list[1].index, data_list[1][3])
graph[1].plot(data_list2[1].index, data_list2[1][3], '-.')
graph[1].plot(data_list3[1].index, data_list3[1][3], '.')
graph[1].set_title('Day 2', x = 1.05, y = 0.8)

graph[2].plot(data_list[2].index, data_list[2][3])
graph[2].plot(data_list2[2].index, data_list2[2][3], '-.')
graph[2].plot(data_list3[2].index, data_list3[2][3], '.')
graph[2].set_title('Day 3', x = 1.05, y = 0.8)

graph[3].plot(data_list[3].index, data_list[3][3])
graph[3].plot(data_list2[3].index, data_list2[3][3], '-.')
graph[3].plot(data_list3[3].index, data_list3[3][3], '.')
graph[3].set_title('Day 4', x = 1.05, y = 0.8)

graph[4].plot(data_list[4].index, data_list[4][3])
graph[4].plot(data_list2[4].index, data_list2[4][3], '-.')
graph[4].plot(data_list3[4].index, data_list3[4][3], '.')
graph[4].set_title('Day 5', x = 1.05, y = 0.8)

# graph[2][1].plot(data_list[5].index, data_list[5][3])
# graph[2][1].plot(data_list2[5].index, data_list2[5][3], '-.')
# graph[2][1].plot(data_list3[5].index, data_list3[5][3], '.')
# graph[2][1].set_title('Day 6', x = 1.05, y = 0.8)

# graph[3][0].plot(data_list[6].index, data_list[6][3])
# graph[3][0].plot(data_list2[6].index, data_list2[6][3], '-.')
# graph[3][0].plot(data_list3[6].index, data_list3[6][3], '.')
# graph[3][0].set_title('Day 7', x = 1.05, y = 0.8)

# graph[3][1].plot(data_list[7].index, data_list[7][3])
# graph[3][1].plot(data_list2[7].index, data_list2[7][3], '-.')
# graph[3][1].plot(data_list3[7].index, data_list3[7][3], '.')
# graph[3][1].set_title('Day 8', x = 1.05, y = 0.8)

for i in range(5) :
    graph[i].set_ylim(0,1)
    graph[i].tick_params(axis='x',labelsize=7)    


# graph[1][0].set_ylim(0, 1)
# graph[2][0].set_ylim(0, 1)
# graph[3][0].set_ylim(0, 1)


lgd = ['avgMap', 'soft_vote', 'hard_vote' ]
plt.legend(lgd, bbox_to_anchor = (1, 0.5), loc = 'right')
plt.show()
