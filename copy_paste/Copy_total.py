import openpyxl
import pandas as pd
from decimal import Decimal
from pandas import DataFrame, read_excel

cid = '2315'

data_path1 = r'../excel/7-' + cid + '/' + cid +'_detail_end_last.xlsx'
data1 = DataFrame(read_excel(data_path1))

data_path2 = r'../excel/7-' + cid + '/' + cid +'_time_end_last.xlsx'
data2 = DataFrame(read_excel(data_path2))

data_path3 = r'../excel/7-' + cid + '/' + cid +'_abnormalpaste_last.xlsx'
data3 = DataFrame(read_excel(data_path3))

data_path4 = r'../excel/7-' + cid + '/' + cid +'_label_end.xlsx'
data4 = DataFrame(read_excel(data_path4))

saveFile = r'../excel/7-' + cid + '/' + cid +'_total.xlsx'

resultnum1 = pd.DataFrame(columns=["用户名", "竞赛", "最小化页面次数归一化", "鼠标离开页面的时间归一化", "异常粘贴次数归一化", "终端输入次数abs归一化",
                                   "终端输入次数0.2归一化", "终端输入次数0.3归一化", "终端输入次数0.4归一化", "终端输入次数0.5归一化",
                                   "timeabs", "time0.2", "time0.3", "time0.4", "time0.5", "标签"])

username = list(data1['用户名'])
mini = list(data1['最小化页面次数归一化'])
leave = list(data1['鼠标离开页面的时间归一化'])
commandabs = list(data1['终端输入次数abs归一化'])
command2 = list(data1['终端输入次数0.2归一化'])
command3 = list(data1['终端输入次数0.3归一化'])
command4 = list(data1['终端输入次数0.4归一化'])
command5 = list(data1['终端输入次数0.5归一化'])

abs = list(data2['timeabs'])
p02 = list(data2['time0.2'])
p03 = list(data2['time0.3'])
p04 = list(data2['time0.4'])
p05 = list(data2['time0.5'])

abnormalpaste = list(data3['异常粘贴次数归一化'])

label = list(data4['平均相似度'])

for user, mi, le, coa, co2, co3, co4, co5, ab, p2, p3, p4, p5, pa, la in zip(list(username), list(mini), list(leave), list(commandabs),
                                                                         list(command2),list(command3), list(command4), list(command5),
                                                                         list(abs), list(p02), list(p03), list(p04),list(p05),
                                                                         list(abnormalpaste),list(label)):
    resultnum1 = resultnum1.append(
        {"用户名": user, "竞赛": cid, "最小化页面次数归一化": mi, "鼠标离开页面的时间归一化": le, "异常粘贴次数归一化": pa,
         "终端输入次数abs归一化": coa, "终端输入次数0.2归一化": co2, "终端输入次数0.3归一化": co3, "终端输入次数0.4归一化": co4,
         "终端输入次数0.5归一化": co5,  "timeabs": ab, "time0.2": p2, "time0.3": p3, "time0.4": p4, "time0.5": p5, "标签": la},
        ignore_index=True)

resultnum1.to_excel(saveFile, index=False)





