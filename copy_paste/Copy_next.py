import openpyxl
import pandas as pd
from decimal import Decimal
from pandas import DataFrame, read_excel
import MySQLdb

db1 = MySQLdb.connect("202.4.155.100", "root", "*", "*", charset='utf8')
db2 = MySQLdb.connect("202.4.155.100", "root", "*", "*", charset='utf8')

cursor1 = db1.cursor()
cursor2 = db2.cursor()
# 1.05	0.9	0.84	1.27	1.34
# 0.11	0.09	0.05	0.04	0.03	0.05	0.05

cid = '2315'

data_path1 = r'../excel/7-' + cid + '/' + cid +'_detail_end.xlsx'
data1 = DataFrame(read_excel(data_path1))

data_path2 = r'../excel/7-' + cid + '/' + cid +'_time_end.xlsx'
data2 = DataFrame(read_excel(data_path2))

data_path3 = r'../excel/7-' + cid + '/' + cid +'_abnormalpaste.xlsx'
data3 = DataFrame(read_excel(data_path3))

save1 = r'../excel/7-' + cid + '/' + cid +'_detail_end_last.xlsx'
save2 = r'../excel/7-' + cid + '/' + cid +'_time_end_last.xlsx'
save3 = r'../excel/7-' + cid + '/' + cid +'_abnormalpaste_last.xlsx'

saveFile = r'../excel/7-' + cid + '/' + cid +'_total.xlsx'

resultnumdetail = pd.DataFrame(columns=["用户名", "竞赛", "最小化页面次数归一化", "鼠标离开页面的时间归一化", "终端输入次数abs归一化",
                                   "终端输入次数0.2归一化", "终端输入次数0.3归一化", "终端输入次数0.4归一化", "终端输入次数0.5归一化"])

resultnumtime = pd.DataFrame(columns=["用户名", "竞赛", "timeabs", "time0.2", "time0.3", "time0.4", "time0.5"])

resultnumpaste = pd.DataFrame(columns=["用户名", "竞赛", "异常粘贴次数归一化"])

resultnum1 = pd.DataFrame(columns=["用户名", "竞赛", "最小化页面次数归一化", "鼠标离开页面的时间归一化", "异常粘贴次数归一化", "终端输入次数abs归一化",
                                   "终端输入次数0.2归一化", "终端输入次数0.3归一化", "终端输入次数0.4归一化", "终端输入次数0.5归一化",
                                   "timeabs", "time0.2", "time0.3", "time0.4", "time0.5"])
userlist = []
sql = "SELECT DISTINCT user_id FROM solution WHERE contest_id = '2315'"
cursor2.execute(sql)
results = cursor2.fetchall()
for row in results:
    username = str(row[0])
    userlist.append(username)
print(len(userlist))

username1 = list(data1['用户名'])
mini = list(data1['最小化页面次数归一化'])
leave = list(data1['鼠标离开页面的时间归一化'])
commandabs = list(data1['终端输入次数abs归一化'])
command2 = list(data1['终端输入次数0.2归一化'])
command3 = list(data1['终端输入次数0.3归一化'])
command4 = list(data1['终端输入次数0.4归一化'])
command5 = list(data1['终端输入次数0.5归一化'])

for user1, mi, le, coa, co2, co3, co4, co5 in zip(list(username1), list(mini), list(leave), list(commandabs),list(command2),
                                                 list(command3), list(command4), list(command5)):
    if(str(user1) in userlist):
        print(user1, "1")
        resultnumdetail = resultnumdetail.append(
            {"用户名": user1, "竞赛": cid, "最小化页面次数归一化": mi, "鼠标离开页面的时间归一化": le, "终端输入次数abs归一化": coa,
             "终端输入次数0.2归一化": co2, "终端输入次数0.3归一化": co3, "终端输入次数0.4归一化": co4, "终端输入次数0.5归一化": co5},
            ignore_index=True)
resultnumdetail.to_excel(save1,  index=False)

username2 = list(data2['用户名'])
abs = list(data2['abs'])
p02 = list(data2['0.2'])
p03 = list(data2['0.3'])
p04 = list(data2['0.4'])
p05 = list(data2['0.5'])

for user2, ab, p2, p3, p4, p5 in zip(list(username2), list(abs), list(p02), list(p03), list(p04), list(p05)):
    if (str(user2) in userlist):
        print(user2, "2")
        resultnumtime = resultnumtime.append(
            {"用户名": user2, "竞赛": cid, "timeabs": ab, "time0.2": p2, "time0.3": p3, "time0.4": p4, "time0.5": p5}, ignore_index=True)
resultnumtime.to_excel(save2,  index=False)

username3 = list(data3['学生'])
abnormalpaste = list(data3['异常粘贴次数归一化'])

for user3, pa in zip(list(username3), list(abnormalpaste)):
    if (str(user3) in userlist):
        print(user3, "3")
        pa = round(pa, 2)
        resultnumpaste = resultnumpaste.append(
            {"用户名": user3, "竞赛": cid, "异常粘贴次数归一化": pa}, ignore_index=True)
resultnumpaste.to_excel(save3, index=False)







