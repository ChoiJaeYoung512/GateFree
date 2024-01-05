import pandas as pd
import numpy as np

# Front Gate
def front_load_file(data, loc):
    # K006 ~ K015만 추출
    column_arr = []

    for i in range(6, 16, 1):
        for j in range(1, 5, 1):
            column_arr.append(f"K0{i:02d}-{j}")

    df = data[column_arr]
    
    # NaN 값 변경 & flot 변환
    df = df.replace("non",np.nan)
    df = df.apply(pd.to_numeric)

    # 조건 만족 인덱스 반환
    condition = np.where(df > 0)
    
    # 데이터 프레임에 condition 인덱스에 맞는 값 변환
    df.iloc[condition] = np.nan
    
    # location 추가
    if loc == True:
        df.insert(0, 'location', data['location'])
    
    return df, column_arr

# Back Gate
def back_load_file(data):
    column_arr = []

    for i in range(6, 16, 1):
        for j in range(1, 5, 1):
            column_arr.append(f"0{i:02d}-{j}")

    df = data[column_arr]

    df = df.replace("non",np.nan)
    df = df.apply(pd.to_numeric)

    condition = np.where(df > 0)
    df.iloc[condition] = np.nan
    
    return df, column_arr
    
# 시각화 -> %matplotlib inline(코드 내부), qt5(외부 창)
# plt.figure(figsize = [15, 40])

# for i in range(0, len(column_arr)//4):
#     plt.subplot(10, 1, i+1)
#     lgd = []
#     for c in range(i*4,(i*4)+4):
#         plt.title(column_arr[c][:-2])
#         plt.ylim(-40, -100)
#         plt.plot(df[column_arr[c]].dropna(axis=0))
#         lgd.append(column_arr[c])
#     plt.legend(lgd, loc = 'lower left')
# plt.show()