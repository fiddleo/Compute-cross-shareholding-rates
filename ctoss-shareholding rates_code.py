
'''
Created on March 23 2021
@author: Yixi Lin

'''


import os
import numpy as np 
import pandas as pd 

def load_data(file_name):
    '''load data from excel'''
    here = os.path.abspath(__file__)
    input_dir = os.path.abspath(os.path.join(here ,os.pardir))
    file_path = os.path.join(input_dir, file_name + ".xlsx")
    df = pd.read_excel(file_path)
    return df

ctrlrate = load_data('company_ctrlrate') # direct shareholding ratio dataframe

comp_names = list({comp_name for row in ctrlrate.iloc[:,[0,1]].values for comp_name in row}) # 获取控股公司和被控股公司名，集合去重，转list
                                                                                             # company name
comp_id = [i+1 for i in range(len(comp_names))]  # company id
comp_dic = {'id':comp_id, 'company_name':sorted(comp_names)}
comp_df = pd.DataFrame(comp_dic)                 # dataframe of all the companies
n = len(comp_df)
matrix = np.zeros((n,n))   # 有n家公司就创建 (n,n)的矩阵
                           # if there are n companies, create (n,n) matrix

comps = list(comp_df['company_name'])
for row in range(len(comps)):
    for col in range(len(comps)):
        value = list(ctrlrate.loc[(ctrlrate['company']==comps[row])&(ctrlrate['controlled_company']==comps[col]),'rate'])    
        if len(value)>0:
            matrix[row,col]=value[0]      

A = matrix    # 直接持股比例矩阵 direct shareholding ratio matrix
I = np.eye(n) # 对角线为1的矩阵  identity matrix

C = np.dot(A, np.linalg.inv(I-A) ) # 全部控股矩阵 total shareholding matrix; C = A*(I-A)^{-1}
B = (C-A)                          # 间接控股矩阵 indirect shareholding matrix

# 全部控股df; total shareholding dataframe
dic = {'company':[],'controlled_company':[],'total_shareholding_ratio':[]}
for row in range(len(comps)):
    for col in range(len(comps)):       
        company_name = comps[row]
        controlled_company_name = comps[col] 
        ratio = C[row,col]
        dic['company'].append(company_name)
        dic['controlled_company'].append(controlled_company_name)
        dic['total_shareholding_ratio'].append(ratio)
df = pd.DataFrame(dic) # total shareholding dataframe

# 间接控股df; indirect shareholding dataframe
indirect_dic = {'company':[],'controlled_company':[],'indirect_shareholding_ratio':[]}

for row in range(len(comps)):
    for col in range(len(comps)):       
        comp_name = comps[row]
        ctrled_company_name = comps[col] 
        indirect_ratio = B[row,col]
        indirect_dic['company'].append(comp_name)
        indirect_dic['controlled_company'].append(ctrled_company_name)
        indirect_dic['indirect_shareholding_ratio'].append(indirect_ratio)

indirect_df = pd.DataFrame(indirect_dic) # indirect shareholding dataframe

print('total shareholding dataframe',df)
print('indirect shareholding dataframe',indirect_df)
