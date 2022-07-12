import pandas as pd
import numpy as np
import pandas as pd
import openpyxl
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from collections import Counter

data_path = r'../excel/6-2262/2262_total_2_消融实验.xlsx'
data_frame = pd.read_excel(data_path, sheet_name='alll')


pre1 = data_frame['S1']
pre2 = data_frame['S2']
pre3 = data_frame['S3']
pre4 = data_frame['S4']
pre5 = data_frame['S5']
pre6 = data_frame['S1+2']
pre7 = data_frame['S1+3']
pre8 = data_frame['S1+4']
pre9 = data_frame['S1+5']
pre10 = data_frame['S2+3']
pre11 = data_frame['S2+4']
pre12 = data_frame['S2+5']
pre13 = data_frame['S3+4']
pre14 = data_frame['S3+5']
pre15 = data_frame['S4+5']
pre16 = data_frame['S1+2+3']
pre17 = data_frame['S1+2+4']
pre18 = data_frame['S1+2+5']
pre19 = data_frame['S2+3+4']
pre20 = data_frame['S2+4+5']
pre21 = data_frame['S3+4+5']
pre22 = data_frame['S2+3+5']
pre23 = data_frame['S1+4+5']
pre24 = data_frame['S1+3+5']
pre25 = data_frame['S1+3+4']
pre26 = data_frame['S1+2+3+4']
pre27 = data_frame['S1+2+3+5']
pre28 = data_frame['S2+3+4+5']
pre29 = data_frame['S1+2+4+5']
pre30 = data_frame['S1+3+4+5']
pre31 = data_frame['S1+2+3+4+5']

key = pre31
print(round(pre1.corr(key, method='pearson'), 2))
print(round(pre2.corr(key, method='pearson'), 2))
print(round(pre3.corr(key, method='pearson'), 2))
print(round(pre4.corr(key, method='pearson'), 2))
print(round(pre5.corr(key, method='pearson'), 2))
print(round(pre6.corr(key, method='pearson'), 2))
print(round(pre7.corr(key, method='pearson'), 2))
print(round(pre8.corr(key, method='pearson'), 2))
print(round(pre9.corr(key, method='pearson'), 2))
print(round(pre10.corr(key, method='pearson'), 2))
print(round(pre11.corr(key, method='pearson'), 2))
print(round(pre12.corr(key, method='pearson'), 2))
print(round(pre13.corr(key, method='pearson'), 2))
print(round(pre14.corr(key, method='pearson'), 2))
print(round(pre15.corr(key, method='pearson'), 2))
print(round(pre16.corr(key, method='pearson'), 2))
print(round(pre17.corr(key, method='pearson'), 2))
print(round(pre18.corr(key, method='pearson'), 2))
print(round(pre19.corr(key, method='pearson'), 2))
print(round(pre20.corr(key, method='pearson'), 2))
print(round(pre21.corr(key, method='pearson'), 2))
print(round(pre22.corr(key, method='pearson'), 2))
print(round(pre23.corr(key, method='pearson'), 2))
print(round(pre24.corr(key, method='pearson'), 2))
print(round(pre25.corr(key, method='pearson'), 2))
print(round(pre26.corr(key, method='pearson'), 2))
print(round(pre27.corr(key, method='pearson'), 2))
print(round(pre28.corr(key, method='pearson'), 2))
print(round(pre29.corr(key, method='pearson'), 2))
print(round(pre30.corr(key, method='pearson'), 2))
print(round(pre31.corr(key, method='pearson'), 2))
