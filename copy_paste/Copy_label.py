import openpyxl
import pandas as pd
from decimal import Decimal
from pandas import DataFrame,read_excel
import MySQLdb

db1 = MySQLdb.connect("202.4.155.100", "root", "*", "*", charset='utf8')
db2 = MySQLdb.connect("202.4.155.100", "root", "*", "*", charset='utf8')

cursor1 = db1.cursor()
cursor2 = db2.cursor()


cid = '2315'

data_path1 = r'../excel/7-' + cid + '/' + cid +'_label.xlsx'
data1 = DataFrame(read_excel(data_path1, sheet_name='Sheet2'))

saveFile = r'../excel/7-' + cid + '/' + cid +'_label_end.xlsx'

resultnum1 = pd.DataFrame(columns=["用户名", "竞赛", "总相似度", "个数", "平均相似度", "相似度矩阵"])

userlists = []
sql = "SELECT DISTINCT user_id FROM solution WHERE contest_id = '2315'"
cursor2.execute(sql)
results = cursor2.fetchall()
for row in results:
    username = str(row[0])
    userlists.append(username)
print(len(userlists))

for userlist in userlists:
    simicount = 0
    username = list(data1['用户'])
    similiar = list(data1['具体结果'])
    print(userlist)
    similist = []
    counts = 0
    for user, simi in zip(list(username), list(similiar)):
        if(str(user) == str(userlist)):
            counts = counts + 1
            similist.append(simi)
            simi = Decimal(str(simi))
            simicount = Decimal(str(simicount))
            simicount = simicount + simi

            print(simi)
    print(simicount)
    if(counts == 0):
        avesimi = 0
    else:
        avesimi = round(simicount / counts, 2)
    resultnum1 = resultnum1.append(
        {"用户名": userlist, "竞赛": cid, "总相似度": simicount, "个数": counts, "平均相似度": avesimi, "相似度矩阵": similist}, ignore_index=True)

    resultnum1.to_excel(saveFile, index=False)





