import pandas as pd
import numpy as np

def random(path, data, frac):
    # test셋
    rd_test = data.sample(frac=frac, random_state=1)
    rd_test = rd_test.sort_index()
    rd_test.to_csv(path + 'rd_test.csv', index=False)
    
    # map
    for i in rd_test.index:
        print(i, end='\r')
        idx = data[data.index == i].index
        data.drop(idx, inplace=True)
    data.to_csv(path + 'rd_map.csv', index=False)


def k_prttn(path, data, k):
    # test셋
    k_test = pd.DataFrame()
    
    for i in range(0, len(data), k):
        print(i, end='\r')
        k_test = pd.concat([k_test, data.iloc[i]], axis=1, sort=False)
    
    k_test = k_test.transpose()
    k_test.to_csv(path + 'k_test.csv') #, index=False)
    
    # map
    for i in k_test.index:
        print(i, end='\r')
        idx = data[data.index == i].index
        data.drop(idx, inplace=True)
    data.to_csv(path + 'k_map.csv') #, index=False)