import pandas as pd
from cleanfunc import cleandf

def exportcsv(directory, csv_files, dot):
    for i in csv_files:
        vip, normal = cleandf(pd.read_csv(directory+'/'+i),dot)
        if len(vip) > 0:
            vip.to_csv(directory+'/vip/vip_'+i,index=False)
        if len(normal) > 0:
            normal.to_csv(directory+'/normal/normal_'+i,index=False)