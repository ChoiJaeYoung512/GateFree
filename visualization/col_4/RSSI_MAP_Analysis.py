import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys
import os
import natsort

rssi_path = '/media/krri/4E17-D17F/2023/GateFree/Data/map_test/'

idx = [[6, 2], [6, 3], [7, 2], [7, 3], [8, 2], [8, 3], [9, 2], [9, 3], [10, 2], [10, 3]]

file_list = glob.glob(os.path.join(rssi_path, '*.csv'))
file_list = natsort.natsorted(file_list)

block_6_2 = pd.DataFrame()
block_6_3 = pd.DataFrame()
block_7_2 = pd.DataFrame()
block_7_3 = pd.DataFrame()
block_8_2 = pd.DataFrame()
block_8_3 = pd.DataFrame()
block_9_2 = pd.DataFrame()
block_9_3 = pd.DataFrame()
block_10_2 = pd.DataFrame()
block_10_3 = pd.DataFrame()

column_arr = []
for i in idx:
    column_arr.append(f"K0{i[0]:02d}-{i[1]}")
        
for f in file_list:
    data = pd.read_csv(f, index_col = 0)
    block_6_2 = pd.concat([block_6_2, data[column_arr[0]]], axis=1, sort=True)
    block_6_3 = pd.concat([block_6_3, data[column_arr[1]]], axis=1, sort=True)
    block_7_2 = pd.concat([block_7_2, data[column_arr[2]]], axis=1, sort=True)
    block_7_3 = pd.concat([block_7_3, data[column_arr[3]]], axis=1, sort=True)
    block_8_2 = pd.concat([block_8_2, data[column_arr[4]]], axis=1, sort=True)
    block_8_3 = pd.concat([block_8_3, data[column_arr[5]]], axis=1, sort=True)
    block_9_2 = pd.concat([block_9_2, data[column_arr[6]]], axis=1, sort=True)
    block_9_3 = pd.concat([block_9_3, data[column_arr[7]]], axis=1, sort=True)
    block_10_2 = pd.concat([block_10_2, data[column_arr[8]]], axis=1, sort=True)
    block_10_3 = pd.concat([block_10_3, data[column_arr[9]]], axis=1, sort=True)

name = ['0420_st', '0427_st', '0517_st', '0517_test']
# name = ['0609_test1', '0609_test2', '0612_test1', '0612_test2', '0613_test1', '0613_test2', '0616_test1', '0616_test2']
# name = ['0609_test2', '0612_test2', '0613_test2', '0616_test2']

block_6_2.columns = name
block_6_3.columns = name
block_7_2.columns = name
block_7_3.columns = name
block_8_2.columns = name
block_8_3.columns = name
block_9_2.columns = name
block_9_3.columns = name
block_10_2.columns = name
block_10_3.columns = name

block_arr = [block_6_2, block_6_3, block_7_2, block_7_3, block_8_2, block_8_3, block_9_2, block_9_3, block_10_2, block_10_3]

sub_plots = plt.subplots(5, 2, figsize=(19, 12))
fig = sub_plots[0]
graph = sub_plots[1]

cnt = 0

for i in range(5):
    for j in range(2):
        graph[i][j].plot(block_arr[cnt])
        graph[i][j].set_title(f"{idx[cnt][0]}_{idx[cnt][1]}")
        cnt += 1

plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.2, hspace=0.45)
plt.legend(name, bbox_to_anchor = (1, 0.5), loc = 'center left')
# plt.savefig(rssi_path + 'rssi_map_app3.png')
plt.show()