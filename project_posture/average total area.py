import pandas as pd
import numpy as np
experiment = pd.read_excel('/Users/sunnyqu/Desktop/Project/BDSinfo_modified.xlsx')#读取xlsx中第一个sheet
column = ['Total Area (cm²)', 'MVPA_minutes.week', 'Subject', 'Vision', 'Surface']
column_index = [list(experiment.columns).index(i) for i in column]
exp_ = np.array(experiment.iloc[:,column_index]).tolist()

ave_dict = dict()
ave_num = dict() #创建空dict
for i in exp_:
    if tuple(i[1:]) in ave_dict.keys():
        ave_dict[tuple(i[1:])] = ave_dict[tuple(i[1:])] + i[0]
        ave_num[tuple(i[1:])] += 1
    else:
        ave_dict[tuple(i[1:])] = i[0]
        ave_num[tuple(i[1:])] = 1
        
        
from openpyxl import load_workbook
wb = load_workbook('/Users/sunnyqu/Desktop/Project/output.xlsx')
ws = wb.create_sheet(index = 0, title = 'Average Total Area')

ws['A1'] = 'Average Total area'
ws['B1'] = column[1]
ws['C1'] = column[2]
ws['D1'] = column[3]
ws['E1'] = column[4]

for i in ave_dict.keys():
    outline = [ave_dict[i]/ave_num[i]] + list(i)
    ws.append(outline)
wb.save('/Users/sunnyqu/Desktop/Project/output.xlsx')
