# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

import numpy as np
# Enter Code Here
def get_unique_teams_set():
    array=read_ipl_data_csv(path,'S100')
    team1=np.unique(array[:,3:4])
    team2=np.unique(array[:,4:5])
    return set(np.union1d(team1,team2))


    




