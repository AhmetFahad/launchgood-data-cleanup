import pandas as pd
from pathlib import Path
import os
from cleanfunc import cleandf
from checkdir import checkdir

directory = str(Path(__file__).resolve().parent)
all_files = os.listdir(directory)    
csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))
dateofcreation = '07/11/2021'

checkdir(directory)

print(directory)
print(all_files)
print(csv_files)

for i in csv_files:
    vip, normal = cleandf(pd.read_csv(directory+'/'+i),dateofcreation)
    print("1")
 #   vip = vip.drop(['index'], axis = 1).reset_index().drop(['index'], axis = 1)
 #   normal = normal.drop(['index'], axis = 1).reset_index().drop(['index'], axis = 1)
    if len(vip) > 0:
        vip.to_csv(directory+'/vip/vip_'+i,index=False)
    if len(normal) > 0:
        normal.to_csv(directory+'/normal/normal_'+i,index=False)