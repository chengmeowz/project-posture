# -*- coding: utf-8 -*-
# pre-processing
# author: Sunny Qu
# modified by: Cheng Zheng (add checking null and dupulicate value)

import os
import pandas as pd # used for handling the dataset
from sklearn.model_selection import train_test_split # used for splitting training and testing data
from sklearn.preprocessing import StandardScaler # used for feature scaling

# Get the project directory
path_current = os.getcwd() # get current path, aka this python file directory
path_project = os.path.dirname(path_current) # go up one directory, aka find the project directory

# Upload the data from excel
dataset = pd.read_excel(path_project + '/BDS/aveTotalArea_MVPA.xlsx') # to import the dataset into a variable

# Check null value
dataset.isnull().any(axis=0)

# Check duplicate value
dataset.duplicated().any

# Splitting the attributes into independent and dependent attributes
X = pd.DataFrame(dataset.iloc[:,0])
Y = pd.DataFrame(dataset.iloc[:,1])

# Splitting the dataset into training and testing datasets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Data Standardization
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_Y = StandardScaler()
Y_train = sc_Y.fit_transform(Y_train)
Y_test = sc_Y.transform(Y_test)

# Store the datasets into excels
pd.DataFrame(X_train).to_excel(path_project + '/X_TotalArea_Y_MVPA/X_train.xlsx')
pd.DataFrame(X_test).to_excel(path_project + '/X_TotalArea_Y_MVPA/X_test.xlsx')
pd.DataFrame(Y_train).to_excel(path_project + '/X_TotalArea_Y_MVPA/Y_train.xlsx')
pd.DataFrame(Y_test).to_excel(path_project + '/X_TotalArea_Y_MVPA/Y_test.xlsx')
