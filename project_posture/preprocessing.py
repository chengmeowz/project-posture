
# -*- coding: utf-8 -*-
# pre-processing
# author: Sunny Qu

import os
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # used for encoding categorical data
from sklearn.model_selection import train_test_split # used for splitting training and testing data
from sklearn.preprocessing import StandardScaler # used for feature scaling

path = os.getcwd()#get current path
path_up1Dir = os.path.dirname(path)#go up one directory

dataset = pd.read_excel(path_up1Dir + '/BDS/aveTotalArea_MVPA.xlsx') # to import the dataset into a variable



# Splitting the attributes into independent and dependent attributes

X = pd.DataFrame(dataset.iloc[:,0])
Y = pd.DataFrame(dataset.iloc[:,1])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)


sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_Y = StandardScaler()
Y_train = sc_Y.fit_transform(Y_train)
Y_test = sc_Y.transform(Y_test)


pd.DataFrame(X_train).to_excel('X_train.xlsx')
pd.DataFrame(X_test).to_excel('X_test.xlsx')
pd.DataFrame(Y_train).to_excel('Y_train.xlsx')
pd.DataFrame(Y_test).to_excel('Y_test.xlsx')

