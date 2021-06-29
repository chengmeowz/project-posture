# -*- coding: utf-8 -*-
# To get average values in 3 trials for each condition
# author: Sunny Qu
# modified by: Cheng Zheng

import os
import pandas as pd
import numpy as np

# Get the project directory
path_current = os.getcwd() # get current path, aka this python file directory
path_project = os.path.dirname(path_current) # go up one directory, aka find the project directory

experiment = pd.read_excel(path_project + '/BDS/BDSinfo_modified.xlsx') # read first sheet from xlsx
column = ['Total Area (cm²)', 'AP RMS (cm)', 'ML RMS (cm)', 'Total Displacement (cm)', 'Total Velocity (cm/s)', 'MVPA_minutes.week', 'IPAQ_Category', 'Subject', 'Vision', 'Surface']
column_index = [list(experiment.columns).index(i) for i in column]
exp_ = np.array(experiment.iloc[:, column_index]).tolist()


for j in np.arange(0, 5, 1):
    outline = list() # create empty list
    ave_dict = dict()
    ave_num = dict() # create empty dict
    for i in exp_:
        if tuple(i[5:]) in ave_dict.keys():
            ave_dict[tuple(i[5:])] = ave_dict[tuple(i[5:])] + i[j]
            ave_num[tuple(i[5:])] += 1
        else:
            ave_dict[tuple(i[5:])] = i[j]
            ave_num[tuple(i[5:])] = 1

    for i in ave_dict.keys():
        outline += [ave_dict[i]/ave_num[i]] # calculate the averaged value
    
    exec('a%s = %s' %(j, outline)) # save averaged value for each variable in parameters, i.e. a0 for aveTotalArea.
    
outline = list(ave_dict.keys()) # save the key values

df1 = pd.DataFrame({'aveTotalArea': a0, 'aveAP_RMS': a1, 'aveML_RMS': a2, 'aveDisplacement': a3, 'aveVelocity': a4})
df2 = pd.DataFrame(outline, columns=['MVPA_minutes.week', 'IPAQ_Category', 'Subject', 'Vision', 'Surface']) 
df2['IPAQ_Category'] = df2.IPAQ_Category.map(lambda x: 3 if x == 'High' else (2 if x == 'Moderate' else 1)) # change low to 1, etc.

result = pd.concat([df1, df2], axis=1) # combine df1 with df2 (no axis means increasing row)
result = result.drop(index=(result.loc[(result['Subject'] == 36)].index))
result.rename(columns={'MVPA_minutes.week':'MVPA', 'IPAQ_Category':'IPAQ'}, inplace=True)
result.sort_values(by=['Subject', 'Vision', 'Surface'], axis=0, ascending=True) # sort the dataframe
result.to_excel(excel_writer=path_project+'/BDS/variables.xlsx', index=False)