# -*- coding: utf-8 -*-
# pre-processing
# author: Sunny Qu

import os
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, Normalizer, OrdinalEncoder

path = os.getcwd()#get current path
path_project = os.path.dirname(path)#go up one directory

# 3Xs, w/o displacement, velocity
dataset = pd.read_excel(path_project+'/BDS/variables3.xlsx')#to import the dataset into a variable

output = dataset.iloc[:,-4:]
clean = np.array(dataset.iloc[:,:-4])

# Standard Scaler
clean_standard = StandardScaler().fit_transform(clean)
df_s = pd.DataFrame(clean_standard, columns=dataset.columns[:-4])
result_s = pd.concat([output, df_s], axis=1)
# result_s = pd.concat([output, df_s, IPAQ_Category], axis=1)
# result_s.rename(columns={'MVPA_minutes.week':'MVPA', 'IPAQ_Category':'IPAQ'}, inplace=True)
result_s.to_excel(path_project+'/IPAQ_noScaled/3/standardScaler/standardScaler.xlsx')

# MinMax Scaler
clean_minmax = MinMaxScaler().fit_transform(clean)
df_mm = pd.DataFrame(clean_minmax, columns=dataset.columns[:-4])
result_mm = pd.concat([output, df_mm], axis=1)
# result_mm = pd.concat([output, df_mm, IPAQ_Category], axis=1)
# result_mm.rename(columns={'MVPA_minutes.week':'MVPA', 'IPAQ_Category':'IPAQ'}, inplace=True)
result_mm.to_excel(path_project+'/IPAQ_noScaled/3/minMaxScaler/minMaxScaler.xlsx')

# Robust Scaler
clean_robust = RobustScaler().fit_transform(clean)
df_r = pd.DataFrame(clean_robust, columns=dataset.columns[:-4])
result_r = pd.concat([output, df_r], axis=1)
# result_r = pd.concat([output, df_r, IPAQ_Category], axis=1)
# result_r.rename(columns={'MVPA_minutes.week':'MVPA', 'IPAQ_Category':'IPAQ'}, inplace=True)
result_r.to_excel(path_project+'/IPAQ_noScaled/3/robustScaler/robustScaler.xlsx')

# 5Xs, w/ displacement, velocity

dataset = pd.read_excel(path_project+'/BDS/variables5.xlsx')#to import the dataset into a variable
output = dataset.iloc[:,-4:]
clean = np.array(dataset.iloc[:,:-4])

# Standard Scaler
clean_standard = StandardScaler().fit_transform(clean)
df_s = pd.DataFrame(clean_standard, columns=dataset.columns[:-4])
result_s = pd.concat([output, df_s], axis=1)
# result_s = pd.concat([output, df_s, IPAQ_Category], axis=1)
# result_s.rename(columns={'MVPA_minutes.week':'MVPA', 'IPAQ_Category':'IPAQ'}, inplace=True)
result_s.to_excel(path_project+'/IPAQ_noScaled/5/standardScaler/standardScaler.xlsx')

# MinMax Scaler
clean_minmax = MinMaxScaler().fit_transform(clean)
df_mm = pd.DataFrame(clean_minmax, columns=dataset.columns[:-4])
result_mm = pd.concat([output, df_mm], axis=1)
# result_mm = pd.concat([output, df_mm, IPAQ_Category], axis=1)
# result_mm.rename(columns={'MVPA_minutes.week':'MVPA', 'IPAQ_Category':'IPAQ'}, inplace=True)
result_mm.to_excel(path_project+'/IPAQ_noScaled/5/minMaxScaler/minMaxScaler.xlsx')

# Robust Scaler
clean_robust = RobustScaler().fit_transform(clean)
df_r = pd.DataFrame(clean_robust, columns=dataset.columns[:-4])
result_r = pd.concat([output, df_r], axis=1)
# result_r = pd.concat([output, df_r, IPAQ_Category], axis=1)
# result_r.rename(columns={'MVPA_minutes.week':'MVPA', 'IPAQ_Category':'IPAQ'}, inplace=True)
result_r.to_excel(path_project+'/IPAQ_noScaled/5/robustScaler/robustScaler.xlsx')

# output = dataset.iloc[:,-3:]
# clean = np.array(dataset.iloc[:,:-3])
#
# # #OrdinalEncoder
# # IPAQ = ['Low','Moderate','High']
# # oe = OrdinalEncoder(categories = [IPAQ])
# # IPAQ_Category = pd.DataFrame(oe.fit_transform(dataset[['IPAQ_Category']]))
#
# # Standard Scaler
# clean_standard = StandardScaler().fit_transform(clean)
# df_s = pd.DataFrame(clean_standard, columns=dataset.columns[:-3])
# result_s = pd.concat([output, df_s], axis=1)
# # result_s = pd.concat([output, df_s, IPAQ_Category], axis=1)
# # result_s.rename(columns={'MVPA_minutes.week':'MVPA', 'IPAQ_Category':'IPAQ'}, inplace=True)
# result_s.to_excel(path_project+'/IPAQ_Scaled/standardScaler/standardScaler.xlsx')
#
# # MinMax Scaler
# clean_minmax = MinMaxScaler().fit_transform(clean)
# df_mm = pd.DataFrame(clean_minmax, columns=dataset.columns[:-3])
# result_mm = pd.concat([output, df_mm], axis=1)
# # result_mm = pd.concat([output, df_mm, IPAQ_Category], axis=1)
# # result_mm.rename(columns={'MVPA_minutes.week':'MVPA', 'IPAQ_Category':'IPAQ'}, inplace=True)
# result_mm.to_excel(path_project+'/IPAQ_Scaled/minMaxScaler/minMaxScaler.xlsx')
#
# # Robust Scaler
# clean_robust = RobustScaler().fit_transform(clean)
# df_r = pd.DataFrame(clean_robust, columns=dataset.columns[:-3])
# result_r = pd.concat([output, df_r], axis=1)
# # result_r = pd.concat([output, df_r, IPAQ_Category], axis=1)
# # result_r.rename(columns={'MVPA_minutes.week':'MVPA', 'IPAQ_Category':'IPAQ'}, inplace=True)
# result_r.to_excel(path_project+'/IPAQ_Scaled/robustScaler/robustScaler.xlsx')


#writer=pd.ExcelWriter(path_project + '/BDS/preprocessing.xlsx')
#result_s.to_excel(writer, sheet_name='StandardScaler')
#result_mm.to_excel(writer, sheet_name='MinMaxScaler')
#result_r.to_excel(writer, sheet_name='RobustScaler')
#writer.save()