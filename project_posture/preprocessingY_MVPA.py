
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

dataset = pd.read_excel(path_up1Dir +'/BDS/variables.xlsx')#to import the dataset into a variable
column = ['aveTotalArea', 'aveAP_RMS','aveML_RMS','aveDisplacement','aveVelocity','MVPA_minutes.week', 'Subject', 'Vision', 'Surface']
column_index = [list(dataset.columns).index(i) for i in column]
exp_ = np.array(dataset.iloc[:,column_index]).tolist() #change data frame to to list

# Splitting the attributes into independent and dependent attributes

aveTotalArea = pd.DataFrame(dataset.iloc[:,0])
aveAP_RMS = pd.DataFrame(dataset.iloc[:,1])
aveML_RMS = pd.DataFrame(dataset.iloc[:,2])
aveDisplacement = pd.DataFrame(dataset.iloc[:,3])
aveVelocity = pd.DataFrame(dataset.iloc[:,4])
MVPA = pd.DataFrame(dataset.iloc[:,5])
other = pd.DataFrame(dataset.iloc[:,6:])


sc_aveTotalArea = StandardScaler()
aveTotalArea_ = sc_aveTotalArea.fit_transform(aveTotalArea)

sc_aveAP_RMS = StandardScaler()
aveAP_RMS_ = sc_aveTotalArea.fit_transform(aveTotalArea)

sc_aveML_RMS = StandardScaler()
aveML_RMS_ = sc_aveML_RMS.fit_transform(aveML_RMS)

sc_aveDisplacement= StandardScaler()
aveDisplacement_ = sc_aveDisplacement.fit_transform(aveDisplacement)

sc_aveVelocity = StandardScaler()
aveVelocity_ = sc_aveVelocity.fit_transform(aveVelocity)

sc_MVPA = StandardScaler()
MVPA_ = sc_MVPA.fit_transform(MVPA)

other['aveTotalArea'] = aveTotalArea_
other['aveAP_RMS'] = aveAP_RMS_
other['aveML_RMS'] = aveML_RMS_
other['aveDisplacement'] = aveDisplacement_
other['aveVelocity'] = aveVelocity_
other['MVPA'] = MVPA_


other.to_excel(path_up1Dir + '/y_MVPA/y_MVPA.xlsx')

