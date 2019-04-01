import os
import pandas as pd


path = "E:\\Xiaoxia\\py\\dax2"


# get filename under folder
dirs = os.listdir(path)
for filename in dirs:
    # filter csv files
    if os.path.splitext(filename)[1] == ".csv":
        print(filename)
        file = pd.read_csv(path + "\\" + filename, header=0, sep='\t*\;',engine='python')
        file.to_csv(filename, index=False)
