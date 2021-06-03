# -*- coding: utf-8 -*-
# pre-processing: RobustScaler
# author: Sunny Qu

import os
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset
from sklearn import preprocessing

path = os.getcwd()#get current path
path_up1Dir = os.path.dirname(path)#go up one directory
dataset = pd.read_excel(path_up1Dir +'/BDS/variables.xlsx')#to import the dataset into a variable

output = dataset.iloc[:,-3:]
clean = np.array(dataset.iloc[:,:-3]) 
robust_scaler = preprocessing.RobustScaler()
clean_robust = robust_scaler.fit_transform(clean)
#check
#x = np.array(dataset.iloc[:,:1]) 
#print(x)
#Q1 = np.percentile(x, 25)
#Q2 = np.percentile(x, 50)
#Q3 = np.percentile(x, 75)
#robust_scaler_test = (x - Q2)/(Q3 - Q1)
#print('rst = ', robust_scaler_test)

new_df = pd.DataFrame(clean_robust, columns=dataset.columns[:-3])

result = pd.concat([output, new_df], axis=1)
result.rename(columns={'MVPA_minutes.week':'MVPA'}, inplace=True)
result.to_excel(path_up1Dir + '/robustScaler/robustScaler.xlsx')
