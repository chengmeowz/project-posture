# -*- coding: utf-8 -*-
# pre-processing
# author: Sunny Qu

import os
import pandas as pd # used for handling the dataset
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # used for encoding categorical data
from sklearn.model_selection import train_test_split # used for splitting training and testing data
from sklearn.preprocessing import StandardScaler # used for feature scaling

path_current = os.getcwd() # get current path, i.e this python file directory
path_project = os.path.dirname(path_current) # go up one directory; find the project directory

dataset = pd.read_excel(path_project + '/BDS/aveTotalArea_MVPA.xlsx') # to import the dataset into a variable

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

path = path_project + '/x_TotalArea_y_MVPA'

pd.DataFrame(X_train).to_excel(path + '/X_Train.xlsx')
pd.DataFrame(X_test).to_excel(path + '/X_Test.xlsx')
pd.DataFrame(Y_train).to_excel(path + '/Y_Train.xlsx')
pd.DataFrame(Y_test).to_excel(path + '/Y_Test.xlsx')
