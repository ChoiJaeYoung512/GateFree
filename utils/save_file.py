import csv
import os

def saveFile(path, filename, data_list):
    os.makedirs(path, exist_ok=True)
    f = open(os.path.join(path, filename), 'a')
    writer = csv.writer(f)
    
    for data in data_list:
        writer.writerow(data)
    f.close()
    
    # with open(os.path.join(path, filename), 'a') as f:
    #     f.writerows(data_list)
