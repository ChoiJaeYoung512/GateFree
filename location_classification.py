import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import utils.load_data as load_data
import os
import math
import csv
import glob
import sys
import natsort

# Data 불러오기
# path = '/home/krri/GH/RSSI_visualize/FP/gatefree/0428_DY_MAP/'
path = '/media/krri/4E17-D17F/GateFree/Data/0601/1/'
save_path = '/media/krri/4E17-D17F/GateFree/Data/0601/1/group/'
file_list = glob.glob(path + 'data' + '*one.csv')
# file_list = glob.glob(path + '*.csv')
file_list = natsort.natsorted(file_list)

df = pd.DataFrame()

for f in file_list:
    data = pd.read_csv(f, index_col=0)
    df = pd.concat([df, data])
    
    df, column_arr = load_data.front_load_file(df, True)    # T: location 사용 / F: location 사용 X

# df = df.reset_index()
loc = df['location'].drop_duplicates()

for l in loc:
    groups = df.groupby('location')
    groups_data = groups.get_group(l)
    print(groups_data)
    
    # csv 파일로 변경
    groups_data.to_csv(save_path + f'{l}_group.csv', index=False, na_rep='non')
