
# -*- coding: utf-8 -*-
# pre-processing
# author: Sunny Qu

import os
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset
from openpyxl import load_workbook
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # used for encoding categorical data
from sklearn.model_selection import train_test_split # used for splitting training and testing data
from sklearn.preprocessing import StandardScaler # used for feature scaling

path = os.getcwd()#get current path
path_up1Dir = os.path.dirname(path)#go up one directory

dataset = pd.read_excel(path_up1Dir +'/BDS/variables.xlsx')#to import the dataset into a variable
output = dataset.iloc[:,-3:] #后三个
clean = np.array(dataset.iloc[:,:-3]) #除了后三个之外的全部
min_max_scaler = preprocessing.MinMaxScaler()
clean_minmax = min_max_scaler.fit_transform(clean)#对除了那三个之外的全部进行clean——minmax
new_df = pd.DataFrame(clean_minmax, columns=dataset.columns[:-3])
result = pd.concat([output, new_df], axis=1)
result.to_excel(path_up1Dir + '/minmax/minmax.xlsx')

