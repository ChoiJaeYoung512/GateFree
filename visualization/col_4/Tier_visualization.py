import pandas as pd
import matplotlib.pyplot as plt

# Read CSV files and create dataframes
path = '/media/krri/T7/gatefree/GF/data/col_4/Tier_acc/'
csv_files = [path + 'avgTier_s_4_4D_100ms.csv', 
             path + 'Soft_s_4_4D_100ms.csv', 
             path + 'Hard_s_4_4D_100ms.csv'] 

dfs = [pd.read_csv(filename, header=None) for filename in csv_files]

fig, axes = plt.subplots(5, 8, figsize=(40, 40))

x_labels = ['Tier0', 'Tier1', 'Tier2', 'Tier3', 'Tier4', 'Tier5', 'Else']

for a in range(5) :
    for b in range(8) :
        ax = axes[a,b]
        data_list = [df.iloc[a * 8 + b,1:]for df in dfs]
    
        for data, label in zip(data_list, ['avgTier', 'Soft', 'Hard']):
            ax.plot(x_labels, data, label=label)

        ax.set_xlabel('Tier')
        ax.set_ylabel('Values')
        
        ax.set_ylim(0, 1)  # Set the y limit to 0~1        
ax.legend()
plt.tight_layout()
plt.show()