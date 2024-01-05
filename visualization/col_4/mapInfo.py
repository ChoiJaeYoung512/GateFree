import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import natsort
import sys
import glob
import os

idx = [[6, 2], [6, 3], [7, 2], [7, 3], [8, 2], [8, 3], [9, 2], [9, 3], [10, 2], [10, 3]]

path = '/media/krri/4E17-D17F/2023/GateFree/Data/0609/test1/'
path2 = '/media/krri/4E17-D17F/2023/GateFree/Data/0612/test1/'
path3 = '/media/krri/4E17-D17F/2023/GateFree/Data/0613/test1/'
path4 = '/media/krri/4E17-D17F/2023/GateFree/Data/0616/test1/'

data_list = glob.glob(path + 'data' + '*all.csv')
data_list2 = glob.glob(path2 + 'data' + '*all.csv')
data_list3 = glob.glob(path3 + 'data' + '*all.csv')
data_list4 = glob.glob(path4 + 'data' + '*all.csv')

data_list = natsort.natsorted(data_list)
data_list2 = natsort.natsorted(data_list2)
data_list3 = natsort.natsorted(data_list3)
data_list4 = natsort.natsorted(data_list4)

df_list1 = []
df_list2 = []
df_list3 = []
df_list4 = []
for f1, f2, f3, f4 in zip(data_list, data_list2, data_list3, data_list4):
    df1 = pd.read_csv(f1, index_col = 0)
    df2 = pd.read_csv(f2, index_col = 0)
    df3 = pd.read_csv(f3, index_col = 0)
    df4 = pd.read_csv(f4, index_col = 0)
    
    df_list1.append(df1)
    df_list2.append(df2)
    df_list3.append(df3)
    df_list4.append(df4)
    
column_arr = []
for i in range(len(idx)):
    column_arr.append(f"K0{idx[i][0]:02d}-{idx[i][1]}")
    
map_path1 = '/media/krri/4E17-D17F/2023/GateFree/Data/0609/'
map_file = '0609_map1.csv'
Day1_map = pd.read_csv(os.path.join(map_path1, map_file), index_col=0)

bar_width = 0.2
x = np.arange(10) # 행 개수 10개 = 블록 10개

plt.figure(figsize=(16, 8))

for i, (d1, d2, d3, d4) in enumerate(zip(df_list1, df_list2, df_list3, df_list4)):
    d1 = d1[column_arr]
    d2 = d2[column_arr]
    d3 = d3[column_arr]
    d4 = d4[column_arr]
    
    d1 = d1.replace("non", np.nan)
    d2 = d2.replace("non", np.nan)
    d3 = d3.replace("non", np.nan)
    d4 = d4.replace("non", np.nan)
    
    d1 = d1.apply(pd.to_numeric)
    d2 = d2.apply(pd.to_numeric)
    d3 = d3.apply(pd.to_numeric)
    d4 = d4.apply(pd.to_numeric)

    df_std = d1.describe().loc['std']
    df_std2 = d2.describe().loc['std']
    df_std3 = d3.describe().loc['std']
    df_std4 = d4.describe().loc['std']
    
    plt.subplot(10, 1, i+1)
    plt.bar(x, df_std, bar_width, alpha=0.8)
    plt.bar(x + bar_width, df_std2, bar_width, alpha=0.8)
    plt.bar(x + 2 * bar_width, df_std3, bar_width, alpha=0.8)
    plt.bar(x + 3 * bar_width, df_std4, bar_width, alpha=0.8)
    
    plt.xticks([])
    
plt.xticks(np.arange(bar_width, 10 + bar_width, 1), d1.columns)

plt.subplot(10, 1, 1)

lgd = ['Day_1', 'Day_2', 'Day_3', 'Day_4']
plt.legend(lgd, bbox_to_anchor = (1, 0.5), loc = 'center left')
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.95, wspace=0.2, hspace=0.5)
plt.show()