# -*- coding: utf-8 -*-
# pre-processing
# author: Sunny Qu

import os
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset
from sklearn.impute import SimpleImputer # used for handling missing data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # used for encoding categorical data
from sklearn.model_selection import train_test_split # used for splitting training and testing data
from sklearn.preprocessing import StandardScaler # used for feature scaling

path = os.getcwd()#get current path
path_up1Dir = os.path.dirname(path)#go up one directory

dataset = pd.read_excel(path_up1Dir + '/BDS/aveTotalArea_MVPA.xlsx') # to import the dataset into a variable

# Splitting the attributes into independent and dependent attributes
X = dataset.iloc[:, 0].values # aveTotalArea = attributes to determine dependent variable / Class
Y = dataset.iloc[:, 1].values # MVP_minutes.week = dependent variable / Class
