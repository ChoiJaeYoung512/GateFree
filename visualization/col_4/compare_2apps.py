import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

# ======== V3 -> 스마트폰 저장 O, 서버 저장 O ========
v3_path = '/media/krri/4E17-D17F/2023/GateFree/Data/0608/7'
v3_file = 'data_7_all.csv'
v3_data = pd.read_csv(os.path.join(v3_path, v3_file))

v3_data['time'] = pd.to_datetime(v3_data['time'], format='%Y-%m-%d-%H-%M-%S.%f', errors='raise')
sec_v3 = v3_data.resample(rule='1S', on='time').count()

v3_data = v3_data.iloc[:, 2:]
v3_data = v3_data.replace("non",np.nan)
v3_data = v3_data.apply(pd.to_numeric)

v3_cnt = []
for i in range(len(v3_data)):
    print(i, end='\r')
    test = v3_data.iloc[i].dropna().count()
    v3_cnt.append(test)

pre = 0
v3_scale = []
for i in range(len(sec_v3)):
    v3_scale.append(sum(v3_cnt[pre:pre + sec_v3['time'][i]]))
    pre += sec_v3['time'][i]

# ======== V4 -> 스마트폰 저장 X, 서버 저장 O ========
v4_path = '/media/krri/4E17-D17F/2023/GateFree/Data/0608/6'
v4_file = 'data_6_all.csv'
v4_data = pd.read_csv(os.path.join(v4_path, v4_file))

v4_data['time'] = pd.to_datetime(v4_data['time'], format='%Y-%m-%d-%H-%M-%S.%f', errors='raise')
sec_v4 = v4_data.resample(rule='1S', on='time').count()

v4_data = v4_data.iloc[:, 2:]
v4_data = v4_data.replace("non",np.nan)
v4_data = v4_data.apply(pd.to_numeric)

v4_cnt = []
for i in range(len(v4_data)):
    print(i, end='\r')
    test2 = v4_data.iloc[i].dropna().count()
    v4_cnt.append(test2)
    
pre = 0
v4_cnt_sum = []
for i in range(len(sec_v4)):
    v4_cnt_sum.append(sum(v4_cnt[pre:pre + sec_v4['time'][i]]))
    pre += sec_v4['time'][i]

print(np.mean(v4_cnt_sum))
print(np.sum(v4_cnt_sum))

plt.plot(v3_scale, 'b')
plt.plot(v4_cnt_sum)
plt.show()