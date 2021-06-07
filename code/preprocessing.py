# -*- coding: utf-8 -*-
# pre-processing: RobustScaler
# author: Sunny Qu

import os
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset
from sklearn import preprocessing

path = os.getcwd()#get current path
path_project = os.path.dirname(path)#go up one directory
dataset = pd.read_excel(path_project +'/BDS/variables.xlsx')#to import the dataset into a variable

output = dataset.iloc[:,-3:]
clean = np.array(dataset.iloc[:,:-3]) 

#Standard Scaler
standard_scaler = preprocessing.StandardScaler()
clean_standard = standard_scaler.fit_transform(clean)
df_s = pd.DataFrame(clean_standard, columns=dataset.columns[:-3])
result_s = pd.concat([output, df_s], axis=1)
result_s.rename(columns={'MVPA_minutes.week':'MVPA'}, inplace=True)
result_s.rename(columns={'IPAQ_Category': 'IPAQ'},inplace=True)
result_s.to_excel(path_project + '/standardScaler/standardScaler.xlsx')

#MinMax Scaler
minmax_scaler = preprocessing.MinMaxScaler()
clean_minmax = minmax_scaler.fit_transform(clean)
df_mm = pd.DataFrame(clean_minmax, columns=dataset.columns[:-3])
result_mm = pd.concat([output, df_mm], axis=1)
result_mm.rename(columns={'MVPA_minutes.week':'MVPA'}, inplace=True)
result_mm.rename(columns={'IPAQ_Category': 'IPAQ'},inplace=True)
result_mm.to_excel(path_project + '/minMaxScaler/minMaxScaler.xlsx')

# Robust Scaler
robust_scaler = preprocessing.RobustScaler()
clean_robust = robust_scaler.fit_transform(clean)
df_r = pd.DataFrame(clean_robust, columns=dataset.columns[:-3])
result_r = pd.concat([output, df_r], axis=1)
result_r.rename(columns={'MVPA_minutes.week':'MVPA'}, inplace=True)
result_r.rename(columns={'IPAQ_Category': 'IPAQ'},inplace=True)
result_r.to_excel(path_project+ '/robustScaler/robustScaler.xlsx')


#writer=pd.ExcelWriter(path_project + '/preprocessing/preprocessing.xlsx')
#result_s.to_excel(writer, sheet_name='StandardScaler')
#result_mm.to_excel(writer, sheet_name='MinMaxScaler')
#result_r.to_excel(writer, sheet_name='RobustScaler')
#writer.save()



