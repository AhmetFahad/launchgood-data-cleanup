import pandas as pd
from pathlib import Path
import os
from checkdir import checkdir
from export import exportcsv

directory = str(Path(__file__).resolve().parent)
all_files = os.listdir(directory)    
csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))
dateofcreation = '07/11/2021'

checkdir(directory)
exportcsv(directory, csv_files, dateofcreation)

