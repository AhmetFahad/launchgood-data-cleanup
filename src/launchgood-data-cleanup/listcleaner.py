import numpy as np
import pandas as pd
import openpyxl
from cleanfunc.py import cleandf
from checkdir.py import checkdir

checkdir()

for i in csv_files:
    vip, normal = cleandf(pd.read_csv(i),dateofcreation)
 #   vip = vip.drop(['index'], axis = 1).reset_index().drop(['index'], axis = 1)
 #   normal = normal.drop(['index'], axis = 1).reset_index().drop(['index'], axis = 1)
    if len(vip) > 0:
        vip.to_csv('vip/vip_'+i,index=False)
    if len(normal) > 0:
        normal.to_csv('normal/normal_'+i,index=False)