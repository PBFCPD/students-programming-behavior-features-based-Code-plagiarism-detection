import MySQLdb
import pandas as pd
from pandas import DataFrame,read_excel
from numpy import *

# db1 = MySQLdb.connect("202.4.155.100", "root", "*", "*", charset='utf8')
# db2 = MySQLdb.connect("202.4.155.100", "root", "*", "*", charset='utf8')
#
# cursor1 = db1.cursor()
# cursor2 = db2.cursor()
#
# resultnum1 = pd.DataFrame(columns=["用户名", "异常粘贴次数", "异常粘贴时间", "粘贴内容", "粘贴前后编码过程1", "粘贴前后编码过程2", "粘贴前后编码过程3", "粘贴前后编码过程4", "粘贴前后编码过程5"])
# savefile = '../excel/2322.xlsx'
#
# sql = "select DISTINCT username from `userstatus_detail` WHERE `contest_id`='2322' AND copy_label='1'"
# cursor1.execute(sql)
# results = cursor1.fetchall()
# i=0
# for row in results:
#     i = i+1
#     username = row[0]
#     sql = "SELECT COUNT(*) AS ids FROM `userstatus_detail` WHERE `contest_id`='2322' AND username = %s AND copy_label = '1'"
#     cursor1.execute(sql, (username, ))
#     resultabnormal = cursor1.fetchall()
#     abnormal_count = resultabnormal[0][0]
#
#     sql = "SELECT * FROM `userstatus_detail` WHERE `contest_id`='2322' AND username = %s AND copy_label = '1' ORDER BY updatetime DESC"
#     cursor1.execute(sql, (username,))
#     resultdetail = cursor1.fetchall()
#     j=0
#     for row1 in resultdetail:
#         j= j + 1
#         updatetime = row1[5]
#         detail = row1[7]
#         paste1 = row1[8]
#         paste2 = row1[9]
#         paste3 = row1[10]
#         paste4 = row1[11]
#         paste5 = row1[12]
#         resultnum1 = resultnum1.append(
#             {"用户名": username, "异常粘贴次数": abnormal_count, "异常粘贴时间": updatetime, "粘贴内容": detail, "粘贴前后编码过程1":paste1 ,"粘贴前后编码过程2": paste2,"粘贴前后编码过程3": paste3,"粘贴前后编码过程4": paste4,"粘贴前后编码过程5": paste5}, ignore_index=True)
#         resultnum1.to_excel(savefile, index=False)
#         print(j," / ",len(resultdetail),i," / ",len(results))
#
# db1.close()
# db2.close()

cid = '2262'
data_path1 = r'../excel/6-' + cid + '/' + cid +'_time_end.xlsx'
data1 = DataFrame(read_excel(data_path1))
abs = list(data1['abs'])
p02 = list(data1['0.2'])
p03 = list(data1['0.3'])
p04 = list(data1['0.4'])
p05 = list(data1['0.5'])

aveabs = mean(abs)
avep02 = mean(p02)
avep03 = mean(p03)
avep04 = mean(p04)
avep05 = mean(p05)
print(aveabs, avep02, avep03, avep04, avep05)

