# -*- coding: utf-8 -*-
# pre-processing
# author: Sunny Qu

import os
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset
from sklearn.model_selection import train_test_split # used for splitting training and testing data
from sklearn.preprocessing import StandardScaler # used for feature scaling

# Getting the file directory to find the excel
path_current = os.getcwd() # get current path, i.e this python file directory
path_project = os.path.dirname(path_current) # go up one directory; find the project directory

dataset = pd.read_excel(path_project + '/BDS/aveTotalArea_MVPA.xlsx') # to import the dataset into a variable

# Splitting the attributes into independent and dependent attributes
X = pd.DataFrame(dataset.iloc[:,0]) # Total Area
Y = pd.DataFrame(dataset.iloc[:,1]) # MVPA_minutes.week

# Splitting the dataset into training and testing datasets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0) # taking training set to be 80% of the original data set and testing set to be 20% of the original data set

# Feature Scaling (convert different scales to a standard scale to make it easier for Machine Learning algorithms)
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

'''
Question: 
1. Why we will have X_Train, X_Test, Y_Train, Y_Test during data pre-processing? 
    Shouldn't we have it later in the leave-one-out cross-validation?
2. When we are building models using different Machine Learning algorithms, 
    how should we fit using X_Train, X_Test, Y_Train, Y_Test?
    Are our codes doing okay? Cheng is extremely confused, because she still cannot have a picture in what she is doing.
'''

# dataset = pd.read_excel('/Users/zclalala/Documents/GitHub/project-posture/BDS/aveTotalArea_MVPA.xlsx')

# learning 
# author: Cheng Zheng

###################

# Ridge regression
from sklearn import linear_model 

model_1 = linear_model.Ridge(alpha=1.0) # define model
model_1.fit(X_train, Y_train)
model_1.coef_ # output: array([[-0.02550975]])
model_1.intercept_ # output: array([6.51089032e-19])

# leave-one-out Cross-Validation

model_1_cv = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
model_1_cv.fit(X_train, Y_train)
model_1_cv.alpha_ # output: 1000000.0

# optimization

###################

#  Kernel ridge regression
from sklearn import kernel_ridge

model_2 = kernel_ridge.KernelRidge(alpha=1.0)
model_2.fit(X_train, Y_train)

# leave-one-out Cross-Validation ???
# How to do this???

# optimization

###################

#  Adaboost
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

model_3 = AdaBoostClassifier(n_estimators=100)

# leave-one-out Cross-Validation

model_3_cvscores = cross_val_score(model_3, X, Y)
model_3_cvscores.mean() # output: 0.03416908914728682

# optimization

###################

#  Random Forest
from sklearn.ensemble import RandomForestClassifier

model_4 = RandomForestClassifier(n_estimators=10)

# leave-one-out Cross-Validation???

model_4_cvscores = cross_val_score(model_4, X, Y)
model_4_cvscores.mean() # output: 0.0170906007751938

# optimization

###################

#  Neural network
from sklearn.neural_network import MLPRegressor 

model_5 = MLPRegressor(random_state=1, max_iter=500)
model_5 = model_5.fit(X_train, Y_train)
model_5.predict(X_test[:2]) # output: array([0.04133816, 0.04021619])
model_5.score(X_test, Y_test) # output: -0.01871909192521093

# leave-one-out Cross-Validation???

# optimization

###################

#  Support vector machine
from sklearn import svm

model_6 = svm.SVR()
model_6.fit(X, Y)

# leave-one-out Cross-Validation

model_1_crossValid = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
model_1_crossValid.fit(X_train, Y_train)
model_1_crossValid.alpha_ # output: 1000000.0

# optimization

###################