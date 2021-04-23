
# -*- coding: utf-8 -*-
# pre-processing
# author: Sunny Qu

import os
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset
from openpyxl import load_workbook
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # used for encoding categorical data
from sklearn.model_selection import train_test_split # used for splitting training and testing data
from sklearn.preprocessing import StandardScaler # used for feature scaling

path = os.getcwd()#get current path
path_up1Dir = os.path.dirname(path)#go up one directory

dataset = pd.read_excel(path_up1Dir +'/BDS/aveTotalArea_MVPA.xlsx')#to import the dataset into a variable
column = ['aveTotalArea', 'MVPA_minutes.week', 'Subject', 'Vision', 'Surface']
column_index = [list(dataset.columns).index(i) for i in column]
exp_ = np.array(dataset.iloc[:,column_index]).tolist() #change data frame to to list

# Splitting the attributes into independent and dependent attributes

X = pd.DataFrame(dataset.iloc[:,1])
Y = pd.DataFrame(dataset.iloc[:,0])
other = pd.DataFrame(dataset.iloc[:,2:])


sc_X = StandardScaler()
X_ = sc_X.fit_transform(X)
sc_Y = StandardScaler()
Y_ = sc_Y.fit_transform(Y)

other['X'] = X_
other['Y'] = Y_


other.to_excel(path_up1Dir + '/y_TotalArea_x_MVPA/y_TotalArea_x_MVPA.xlsx')

