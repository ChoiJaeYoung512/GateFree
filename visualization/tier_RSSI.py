import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils import load_data

data_path_N = '/home/krri/GH/RSSI_visualize/front_gate/N/data__all.csv'
data_path_E = '/home/krri/GH/RSSI_visualize/front_gate/E/data__all.csv'
data_path_S = '/home/krri/GH/RSSI_visualize/front_gate/S/data__all.csv'
data_path_W = '/home/krri/GH/RSSI_visualize/front_gate/W/data__all.csv'

data = pd.concat(map(pd.read_csv, [data_path_N, data_path_E, data_path_S, data_path_W]))

# Front
tier1_group = ['K007-3', 'K008-1', 'K008-3', 'K013-1']
tier2_group = ['K007-4', 'K008-4', 'K012-4', 'K013-4']
tier3_group = ['K007-2', 'K009-2', 'K013-2']
tier4_group = ['K007-1', 'K009-1', 'K012-1', 'K012-3', 'K013-3', 'K014-1']
tier5_group = ['K012-2', 'K014-2']

# Back
# tier1_group = ['007-4', '012-2', '012-4', '013-2']
# tier2_group = ['007-1', '008-1', '012-1', '013-1']
# tier3_group = ['007-3', '011-3', '013-3']
# tier4_group = ['006-4', '007-2', '008-2', '008-4', '011-4', '013-4']
# tier5_group = ['006-3', '008-3']

tier_arr = [tier1_group, tier2_group, tier3_group, tier4_group, tier5_group]

# file load
df, column_arr = load_data.front_load_file(data)

def vis(tier_group, c):
    for i in tier_group:
        print(i)
        sns.kdeplot(df[i], color = c)
        
    plt.title('The distribution of RSSI counts')
    plt.xlabel('RSSI')
    
color = ['r', 'y', 'b', 'g', 'purple']

for i in range(len(tier_arr)):
    vis(tier_arr[i], color[i])

plt.show()