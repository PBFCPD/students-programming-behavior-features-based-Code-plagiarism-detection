import numpy as np
import pandas as pd
import openpyxl

import matplotlib.pyplot as plt
import scipy.stats as ss

data_path = r'../excel/relation.xlsx'
data_frame = pd.read_excel(data_path, sheet_name='Sheet3')

normal = data_frame['平时']
final = data_frame['期末']
copy2262 = data_frame['2262抄袭率85']
copy2315 = data_frame['2315抄袭率85']
copyave = data_frame['平均抄袭率85']

result1 = ss.pearsonr(normal, copy2262)
result2 = ss.pearsonr(normal, copy2315)
result3 = ss.pearsonr(normal, copyave)
print(result1)
print(result2)
print(result3)

result4 = ss.pearsonr(final, copy2262)
result5 = ss.pearsonr(final, copy2315)
result6 = ss.pearsonr(final, copyave)
print(result4)
print(result5)
print(result6)

# figure, ax = plt.subplots(figsize=(12, 12))
# sns.heatmap(df.corr(), square=True, annot=True, ax=ax)

