import numpy as np
import pandas as pd
import openpyxl
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from collections import Counter

data_path = r'../excel/6-2262/2262_total_2_消融实验.xlsx'
data_frame = pd.read_excel(data_path, sheet_name='3个特征')

label = list(data_frame['二分类0.9'])
pre1 = list(data_frame['S1'])
pre2 = list(data_frame['S2'])
pre3 = list(data_frame['S3'])
pre4 = list(data_frame['S4'])
pre5 = list(data_frame['S5'])
pre6 = list(data_frame['S6'])
pre7 = list(data_frame['S7'])
pre8 = list(data_frame['S8'])
pre9 = list(data_frame['S9'])
pre10 = list(data_frame['S10'])

print("*****准确率*****")
print(accuracy_score(label, pre1))
print(accuracy_score(label, pre2))
print(accuracy_score(label, pre3))
print(accuracy_score(label, pre4))
print(accuracy_score(label, pre5))
print(accuracy_score(label, pre6))
print(accuracy_score(label, pre7))
print(accuracy_score(label, pre8))
print(accuracy_score(label, pre9))
print(accuracy_score(label, pre10))

print("*****精确率*****")
print(precision_score(label, pre1, average='weighted'))
print(precision_score(label, pre2, average='weighted'))
print(precision_score(label, pre3, average='weighted'))
print(precision_score(label, pre4, average='weighted'))
print(precision_score(label, pre5, average='weighted'))
print(precision_score(label, pre6, average='weighted'))
print(precision_score(label, pre7, average='weighted'))
print(precision_score(label, pre8, average='weighted'))
print(precision_score(label, pre9, average='weighted'))
print(precision_score(label, pre10, average='weighted'))

print("*****召回率*****")
print(recall_score(label, pre1, average='weighted'))
print(recall_score(label, pre2, average='weighted'))
print(recall_score(label, pre3, average='weighted'))
print(recall_score(label, pre4, average='weighted'))
print(recall_score(label, pre5, average='weighted'))
print(recall_score(label, pre6, average='weighted'))
print(recall_score(label, pre7, average='weighted'))
print(recall_score(label, pre8, average='weighted'))
print(recall_score(label, pre9, average='weighted'))
print(recall_score(label, pre10, average='weighted'))

print("*****F1-score*****")
print(f1_score(label, pre1, average='weighted'))
print(f1_score(label, pre2, average='weighted'))
print(f1_score(label, pre3, average='weighted'))
print(f1_score(label, pre4, average='weighted'))
print(f1_score(label, pre5, average='weighted'))
print(f1_score(label, pre6, average='weighted'))
print(f1_score(label, pre7, average='weighted'))
print(f1_score(label, pre8, average='weighted'))
print(f1_score(label, pre9, average='weighted'))
print(f1_score(label, pre10, average='weighted'))
