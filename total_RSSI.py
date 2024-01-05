import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_path_N = '/home/krri/GH/RSSI_visualize/back_gate/N/data__all.csv'
data_path_E = '/home/krri/GH/RSSI_visualize/back_gate/E/data__all.csv'
data_path_S = '/home/krri/GH/RSSI_visualize/back_gate/S/data__all.csv'
data_path_W = '/home/krri/GH/RSSI_visualize/back_gate/W/data__all.csv'

data = pd.concat(map(pd.read_csv, [data_path_N, data_path_E, data_path_S, data_path_W]))

column_arr = []

# format -> front: f"K0{i:02d}-{j}" / back: f"0{i:02d}-{j}"
for i in range(6, 16, 1):
    for j in range(1, 5, 1):
        column_arr.append(f"0{i:02d}-{j}")

df = data[column_arr]

df = df.replace("non",np.nan)
df = df.apply(pd.to_numeric)

condition = np.where(df > 0)
df.iloc[condition] = np.nan

for i in column_arr:
    sns.kdeplot(df[i])

plt.title('The distribution of RSSI counts')
plt.show()